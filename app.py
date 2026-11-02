import os
import io
import json
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from imdb_service import parse_text_with_gemini, enrich_items_with_imdb, search_imdb_suggestion

load_dotenv()

st.set_page_config(
    page_title="IMDb AI Automator — Séries, Doramas, Animes & Filmes",
    page_icon="🎬",
    layout="wide",
)

st.title("🎬 IMDb AI Automator")
st.markdown(
    "Cole sua lista bagunçada de **Filmes, Séries, Doramas e Animes** (com ou sem notas) e transforme tudo em pacotes prontos para o **IMDb** sem precisar digitar um por um!"
)

# Sidebar - Configurações
with st.sidebar:
    st.header("⚙️ Configuração")
    default_key = os.getenv("GEMINI_API_KEY", "")
    api_key = st.text_input(
        "🔑 Gemini API Key",
        value=default_key,
        type="password",
        help="Pegue sua chave gratuita no Google AI Studio (aistudio.google.com)",
    )
    st.caption(
        "💡 **Busca de IDs do IMDb (`ttXXXXXXX`)**: Automática e gratuita (não precisa de chave do TMDB/OMDb!)."
    )
    st.divider()
    st.subheader("📌 O que esta ferramenta faz:")
    st.markdown(
        """
1. **Lê qualquer formato de texto** (bloco de notas, WhatsApp, listas numeradas) usando IA.
2. **Encontra o ID oficial (`tt...`)** de cada obra no IMDb.
3. **Separa em listas** (Watchlist, Doramas, Animes, Séries, Filmes) e **Notas (1 a 10)**.
4. **Exporta CSV oficial do IMDb** + **Script de Console 1-Clique** para aplicar Notas e Watchlist direto na sua conta!
"""
    )

# Estado da sessão
if "df_items" not in st.session_state:
    st.session_state.df_items = None

# Exemplo padrão
exemplo_texto = """Doramas que já vi:
- Pousando no Amor (nota 10, perfeito)
- Alquimia das Almas 9.5
- Vincenzo (nota 9)
- Pretendente Surpresa 8/10
- Goblin (quero ver)

Animes:
- Attack on Titan 10/10
- Solo Leveling nota 9
- Frieren (quero assistir)
- Death Note 10

Séries e Filmes:
- Breaking Bad 10
- The O.C. nota 8
- Tudo em Todo o Lugar ao Mesmo Tempo 9
- Duna Parte 2 (watchlist)"""

col1, col2 = st.columns([2, 1])

with col1:
    raw_text = st.text_area(
        "📝 Cole sua lista de Filmes, Séries, Doramas e Animes aqui:",
        value=exemplo_texto,
        height=270,
    )

with col2:
    st.info(
        "**Dicas de como você pode escrever:**\n"
        "- Pode misturar português e inglês (*Pousando no Amor* ou *Crash Landing on You*)\n"
        "- Pode colocar notas (*nota 10*, *9/10*, *8.5*)\n"
        "- Pode marcar o que ainda não viu (*quero ver*, *watchlist*)\n"
        "- Ou use a busca rápida sem IA abaixo se quiser só buscar títulos separados por linha!"
    )
    modo_sem_ia = st.checkbox(
        "⚡ Modo Direto (1 título por linha, sem usar Gemini API)",
        value=False,
        help="Marque se quiser apenas buscar os IDs no IMDb de uma lista simples sem usar chave do Gemini.",
    )

if st.button("🚀 Processar Lista e Buscar IDs no IMDb", type="primary", use_container_width=True):
    if not raw_text.strip():
        st.warning("Por favor, cole pelo menos um título na caixa de texto.")
    elif not modo_sem_ia and not api_key:
        st.error(
            "⚠️ Informe sua **Gemini API Key** na barra lateral esquerda (ou marque a opção 'Modo Direto' ao lado para testar sem chave de IA)."
        )
    else:
        with st.spinner("🤖 Analisando títulos e buscando IDs oficiais no IMDb..."):
            try:
                if modo_sem_ia:
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
                    items_parsed = parse_text_with_gemini(raw_text, api_key)

                enriched = enrich_items_with_imdb(items_parsed)
                st.session_state.df_items = pd.DataFrame(enriched)
                st.success(f"✅ {len(enriched)} títulos encontrados e vinculados ao IMDb!")
            except Exception as e:
                st.error(f"Erro ao processar: {e}")

# Exibição dos resultados e exportação
if st.session_state.df_items is not None and not st.session_state.df_items.empty:
    st.divider()
    st.subheader("📋 1. Revise e Edite seus Títulos Encontrados")
    st.caption(
        "Você pode editar qualquer célula abaixo (trocar a Nota, mudar de Watchlist para Assistido, ou ajustar o ID `tt...`)."
    )

    df = st.session_state.df_items

    edited_df = st.data_editor(
        df[
            [
                "Const",
                "Title",
                "Original Input",
                "Year",
                "Categoria",
                "Status",
                "Your Rating",
                "Lista",
                "URL",
            ]
        ],
        column_config={
            "Const": st.column_config.TextColumn("IMDb ID (Const)", width="small"),
            "Title": st.column_config.TextColumn("Título Oficial IMDb", width="medium"),
            "Original Input": st.column_config.TextColumn("Texto Extraído", width="medium"),
            "Year": st.column_config.TextColumn("Ano", width="small"),
            "Categoria": st.column_config.SelectboxColumn(
                "Categoria", options=["Filme", "Série", "Dorama", "Anime"], width="small"
            ),
            "Status": st.column_config.SelectboxColumn(
                "Status", options=["Assistido", "Watchlist"], width="small"
            ),
            "Your Rating": st.column_config.NumberColumn(
                "Sua Nota (1-10)", min_value=1, max_value=10, step=1, width="small"
            ),
            "Lista": st.column_config.TextColumn("Lista Personalizada", width="medium"),
            "URL": st.column_config.LinkColumn("Link IMDb", width="small"),
        },
        use_container_width=True,
        num_rows="dynamic",
    )

    st.divider()
    st.subheader("📦 2. Exportar / Atualizar seu IMDb")

    tab_csv, tab_console, tab_trakt = st.tabs(
        [
            "📥 Importar Listas via CSV (Nativo do IMDb)",
            "⚡ Automação 1-Clique (Dar Notas + Watchlist no Navegador)",
            "🔄 JSON / Trakt.tv / MyAnimeList",
        ]
    )

    # Colunas oficiais que o importador de listas do IMDb reconhece
    imdb_cols = [
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

    def to_imdb_csv(sub_df: pd.DataFrame) -> bytes:
        out = pd.DataFrame()
        for c in imdb_cols:
            if c in sub_df.columns:
                out[c] = sub_df[c]
            else:
                out[c] = ""
        return out.to_csv(index=False).encode("utf-8")

    with tab_csv:
        st.markdown(
            """
            ### Como importar um arquivo CSV direto no IMDb (sem precisar instalar nada no navegador):
            1. Faça login na sua conta em [imdb.com](https://www.imdb.com).
            2. Crie uma lista nova em **[Suas Listas -> Criar Lista](https://www.imdb.com/list/create)** (ex: *Meus Doramas*, *Meus Animes*).
            3. Dentro da lista criada ou da sua conta, use a opção **Import** (ou cole os IDs `Const`) / carregue o CSV abaixo!
            """
        )

        col_a, col_b, col_c = st.columns(3)

        with col_a:
            st.download_button(
                "📥 Baixar CSV Completo (Todos os Itens)",
                data=to_imdb_csv(edited_df),
                file_name="imdb_todos_itens.csv",
                mime="text/csv",
                use_container_width=True,
            )

        with col_b:
            watchlist_df = edited_df[edited_df["Status"] == "Watchlist"]
            st.download_button(
                f"📥 Baixar CSV — Watchlist ({len(watchlist_df)} itens)",
                data=to_imdb_csv(watchlist_df),
                file_name="imdb_watchlist.csv",
                mime="text/csv",
                use_container_width=True,
            )

        with col_c:
            assistidos_df = edited_df[edited_df["Status"] == "Assistido"]
            st.download_button(
                f"📥 Baixar CSV — Já Assistidos ({len(assistidos_df)} itens)",
                data=to_imdb_csv(assistidos_df),
                file_name="imdb_assistidos.csv",
                mime="text/csv",
                use_container_width=True,
            )

        st.markdown("#### 📂 Baixar separado por Categoria (Doramas, Animes, Séries, Filmes):")
        categorias = edited_df["Categoria"].unique().tolist()
        cols_cat = st.columns(max(len(categorias), 1))
        for idx, cat in enumerate(categorias):
            cat_df = edited_df[edited_df["Categoria"] == cat]
            with cols_cat[idx]:
                st.download_button(
                    f"📥 Lista: {cat} ({len(cat_df)})",
                    data=to_imdb_csv(cat_df),
                    file_name=f"imdb_{cat.lower()}.csv",
                    mime="text/csv",
                    use_container_width=True,
                )

    with tab_console:
        st.markdown(
            """
            ### ⚡ Quer aplicar todas as **Notas (1 a 10)** e **Watchlist** de uma vez sem abrir página por página?
            Como o IMDb bloqueia robôs externos com Captcha, o jeito mais inteligente e **100% imune a bloqueios** é rodar este mini-script **dentro da sua própria aba já logada do IMDb** (usando a API GraphQL interna do IMDb)!
            
            1. Abra [imdb.com](https://www.imdb.com) no seu navegador (já logado na sua conta).
            2. Aperte **F12** (ou `Ctrl + Shift + I`), clique na aba **Console**, cole o código abaixo e aperte **Enter**!
            """
        )

        # Prepara payload para o script JS
        valid_rows = edited_df[edited_df["Const"].astype(str).str.startswith("tt")]
        js_items = []
        for _, r in valid_rows.iterrows():
            rating_val = r["Your Rating"]
            rating_int = None
            if pd.notna(rating_val) and str(rating_val).strip() != "":
                try:
                    rating_int = int(float(rating_val))
                except ValueError:
                    rating_int = None
            js_items.append(
                {
                    "id": str(r["Const"]).strip(),
                    "title": str(r["Title"]),
                    "status": str(r["Status"]),
                    "rating": rating_int,
                }
            )

        js_payload = json.dumps(js_items, ensure_ascii=False, indent=2)

        js_code = f"""// === AUTOMATIZADOR IMDB (RODE NO CONSOLE F12 DENTRO DE IMDB.COM) ===
(async () => {{
  const items = {js_payload};
  console.log(`🎬 Iniciando atualização de ${{items.length}} títulos no IMDb...`);

  const sleep = (ms) => new Promise(r => setTimeout(r, ms));

  for (const item of items) {{
    try {{
      // 1. Se tiver nota (1 a 10), envia a avaliação oficial via GraphQL do IMDb
      if (item.rating && item.rating >= 1 && item.rating <= 10) {{
        const res = await fetch("https://api.graphql.imdb.com/", {{
          method: "POST",
          headers: {{
            "Content-Type": "application/json",
            "x-imdb-client-name": "imdb-web-next"
          }},
          credentials: "include",
          body: JSON.stringify({{
            query: `mutation UpdateTitleRating($rating: Int!, $titleId: ID!) {{
              rateTitle(input: {{ rating: $rating, titleId: $titleId }}) {{
                rating {{ value }}
              }}
            }}`,
            variables: {{ rating: item.rating, titleId: item.id }}
          }})
        }});
        const data = await res.json();
        console.log(`⭐ Nota ${{item.rating}}/10 aplicada em: ${{item.title}} (${{item.id}})`, data);
        await sleep(900);
      }}

      // 2. Se for Watchlist, adiciona na Watchlist oficial da conta
      if (item.status === "Watchlist") {{
        const wlRes = await fetch(`https://www.imdb.com/watchlist/${{item.id}}`, {{
          method: "PUT",
          credentials: "include"
        }});
        console.log(`📌 Adicionado à Watchlist: ${{item.title}} (${{item.id}}) - Status: ${{wlRes.status}}`);
        await sleep(900);
      }}
    }} catch (err) {{
      console.error(`❌ Erro em ${{item.title}} (${{item.id}}):`, err);
    }}
  }}
  console.log("✅ Automação concluída! Atualize sua página do IMDb para ver as notas e listas.");
}})();"""

        st.code(js_code, language="javascript")

    with tab_trakt:
        st.markdown(
            "Se também quiser importar no **Trakt.tv**, **Letterboxd** ou guardar em JSON estruturado:"
        )
        st.download_button(
            "📥 Baixar JSON Estruturado",
            data=edited_df.to_json(orient="records", force_ascii=False, indent=2).encode("utf-8"),
            file_name="meus_filmes_series_doramas_animes.json",
            mime="application/json",
        )
        st.json(edited_df.to_dict(orient="records"), expanded=False)

