import argparse
import os
import pandas as pd
from dotenv import load_dotenv
from imdb_service import parse_text_with_gemini, enrich_items_with_imdb

load_dotenv()

IMDB_COLS = [
    "Const",
    "Your Rating",
    "Date Rated",
    "Title",
    "URL",
    "Title Type",
    "IMDb Rating",
    "Runtime (mins)",
    "Year",
    "Genres",
    "Num Votes",
    "Release Date",
    "Directors",
]


def main():
    parser = argparse.ArgumentParser(
        description="Converte uma lista de texto livre de filmes, séries, doramas e animes em CSVs do IMDb."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        help="Caminho do arquivo .txt com a sua lista bagunçada",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="imdb_export.csv",
        help="Arquivo CSV de saída (padrão: imdb_export.csv)",
    )
    parser.add_argument(
        "--sem-ia",
        action="store_true",
        help="Processa 1 título por linha direto no IMDb sem precisar da API do Gemini",
    )

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"❌ Arquivo não encontrado: {args.input}")
        return

    with open(args.input, "r", encoding="utf-8") as f:
        raw_text = f.read()

    if args.sem_ia:
        print("⚡ Modo Direto ativado (1 título por linha)...")
        linhas = [
            l.strip(" -•*0123456789.")
            for l in raw_text.splitlines()
            if l.strip() and not l.strip().endswith(":")
        ]
        items_parsed = [
            {
                "titulo_original_ou_conhecido": l,
                "ano_aproximado": None,
                "tipo": "Série",
                "status": "Watchlist",
                "nota_usuario": None,
                "lista_personalizada": "Geral",
            }
            for l in linhas
        ]
    else:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print(
                "❌ Variável GEMINI_API_KEY não definida no arquivo .env! Use --sem-ia ou defina sua chave."
            )
            return
        print("🤖 Extraindo e classificando obras com o Gemini...")
        items_parsed = parse_text_with_gemini(raw_text, api_key)

    print(f"🔎 Buscando IDs oficiais (`ttXXXXXXX`) no IMDb para {len(items_parsed)} títulos...")
    enriched = enrich_items_with_imdb(items_parsed)
    df = pd.DataFrame(enriched)

    for col in IMDB_COLS:
        if col not in df.columns:
            df[col] = ""

    df[IMDB_COLS].to_csv(args.output, index=False, encoding="utf-8")
    print(f"✅ Arquivo salvo com sucesso em: {args.output}")
    print("\nResumo dos títulos encontrados:")
    for row in enriched:
        print(
            f"  - [{row['Const'] or 'N/A'}] {row['Title']} ({row['Year']}) | Categoria: {row['Categoria']} | Status: {row['Status']} | Nota: {row['Your Rating']}"
        )


if __name__ == "__main__":
    main()

