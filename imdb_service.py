import os
import json
import urllib.request
import urllib.parse
import re
from typing import List, Dict, Any, Optional
from google import genai
from google.genai import types
from pydantic import BaseModel, Field


class MediaItem(BaseModel):
    titulo_original_ou_conhecido: str = Field(
        description="Título principal da obra (filme, série, dorama ou anime)"
    )
    ano_aproximado: Optional[int] = Field(
        default=None, description="Ano de lançamento se mencionado ou conhecido"
    )
    tipo: str = Field(
        description="Categoria: 'Filme', 'Série', 'Dorama' ou 'Anime'"
    )
    status: str = Field(
        description="'Watchlist' (quero ver) ou 'Assistido' (já vi)"
    )
    nota_usuario: Optional[int] = Field(
        default=None,
        description="Nota de 1 a 10 dada pelo usuário, se mencionada (arredonde se for decimal)",
    )
    lista_personalizada: str = Field(
        description="Nome sugerido da lista personalizada (ex: 'Doramas', 'Animes', 'Séries', 'Filmes')"
    )
    comentario: Optional[str] = Field(
        default=None, description="Observação ou comentário extra do usuário"
    )


class MediaListResponse(BaseModel):
    itens: List[MediaItem]


def parse_text_with_gemini(raw_text: str, api_key: str) -> List[Dict[str, Any]]:
    """
    Usa o Gemini para transformar um texto livre/bagunçado em uma lista estruturada de obras.
    """
    client = genai.Client(api_key=api_key)

    prompt = f"""
Você é um assistente especialista em cinema, séries, doramas (K-dramas, J-dramas, C-dramas) e animes.
O usuário colou uma lista bagunçada de títulos que ele já assistiu ou quer assistir.
Extraia TODOS os títulos mencionados e classifique cada um corretamente.

Regras:
1. Se o título estiver abreviado ou em português, identifique o nome oficial mais conhecido (ou título em inglês/original que facilite a busca no IMDb).
2. Classifique `tipo` estritamente entre: 'Filme', 'Série', 'Dorama' ou 'Anime'.
3. Classifique `status`:
   - Se o usuário deu nota, disse que já viu, ou não especificou que é para ver depois, marque como 'Assistido' (ou se o contexto indicar quero ver, marque 'Watchlist').
   - Se o usuário disser "quero ver", "para assistir", "watchlist", marque como 'Watchlist'.
4. Se houver nota (ex: "nota 9", "10/10", "8.5"), converta para um inteiro de 1 a 10 em `nota_usuario`.
5. Em `lista_personalizada`, agrupe em listas lógicas como 'Meus Doramas', 'Meus Animes', 'Minhas Séries', 'Meus Filmes', ou se for Watchlist, 'Watchlist'.

Texto do usuário:
---
{raw_text}
---
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=MediaListResponse,
            temperature=0.1,
        ),
    )

    data = json.loads(response.text)
    return data.get("itens", [])


def search_imdb_suggestion(query: str, year: Optional[int] = None) -> Dict[str, Any]:
    """
    Busca o ID do IMDb (ttXXXXXXX) diretamente na API pública de sugestões do IMDb (sem precisar de chave!).
    """
    clean_query = query.strip()
    if not clean_query:
        return {}

    # A API de suggestion do IMDb usa a primeira letra minúscula (ou _ se especial)
    first_char = re.sub(r"[^a-zA-Z0-9]", "", clean_query.lower())
    first_letter = first_char[0] if first_char else "a"

    encoded_query = urllib.parse.quote(clean_query)
    url = f"https://v3.sg.media-imdb.com/suggestion/{first_letter}/{encoded_query}.json"

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Accept": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            results = data.get("d", [])
            # Filtra apenas títulos do IMDb que começam com 'tt' (ignora atores 'nm')
            titles = [r for r in results if r.get("id", "").startswith("tt")]
            if not titles:
                return {}

            # Se temos ano aproximado, tenta achar o mais próximo
            best_match = titles[0]
            if year:
                for t in titles:
                    t_year = t.get("y")
                    if t_year and abs(int(t_year) - int(year)) <= 1:
                        best_match = t
                        break

            imdb_id = best_match.get("id", "")
            return {
                "Const": imdb_id,
                "Title": best_match.get("l", clean_query),
                "Year": best_match.get("y", year or ""),
                "IMDb_Type": best_match.get("q", ""),
                "Poster": best_match.get("i", {}).get("imageUrl", "")
                if isinstance(best_match.get("i"), dict)
                else "",
                "URL": f"https://www.imdb.com/title/{imdb_id}/" if imdb_id else "",
            }
    except Exception as e:
        return {"error": str(e)}


def enrich_items_with_imdb(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Para cada item extraído pela IA, busca o ID real (`tt...`) no IMDb.
    """
    enriched = []
    for item in items:
        titulo = item.get("titulo_original_ou_conhecido", "")
        ano = item.get("ano_aproximado")
        imdb_info = search_imdb_suggestion(titulo, ano)

        row = {
            "Const": imdb_info.get("Const", ""),
            "Your Rating": item.get("nota_usuario") or "",
            "Date Rated": "",
            "Title": imdb_info.get("Title") or titulo,
            "Original Input": titulo,
            "URL": imdb_info.get("URL", ""),
            "Title Type": imdb_info.get("IMDb_Type") or item.get("tipo", ""),
            "IMDb Rating": "",
            "Runtime (mins)": "",
            "Year": imdb_info.get("Year") or (ano if ano else ""),
            "Genres": item.get("tipo", ""),
            "Num Votes": "",
            "Release Date": "",
            "Directors": "",
            # Campos extras de controle para o nosso painel
            "Categoria": item.get("tipo", "Série"),
            "Status": item.get("status", "Watchlist"),
            "Lista": item.get("lista_personalizada", "Geral"),
            "Comentario": item.get("comentario") or "",
            "Poster": imdb_info.get("Poster", ""),
        }
        enriched.append(row)
    return enriched

