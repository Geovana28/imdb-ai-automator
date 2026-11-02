import json

rows = json.load(open("meus_98_doramas_completo.json", encoding="utf-8"))
js_items = [
    {
        "id": r["Const"],
        "title": r["Title"],
        "notion_name": r["Nome no Notion"],
        "rating": r["Your Rating"],
    }
    for r in rows
    if r["Const"]
]

js_script = f"""// === AUTOMATIZADOR IMDB: 98 DORAMAS DO NOTION (COM BARRA VISUAL NA TELA) ===
// Como usar:
// 1. Abra https://www.imdb.com no navegador (logado na sua conta)
// 2. Aperte F12 -> Clique na aba "Console"
// 3. Cole todo este código e aperte Enter!
// 4. Espere a barra amarela no topo do site ficar VERDE antes de mudar de página!

(async () => {{
  const items = {json.dumps(js_items, ensure_ascii=False, indent=2)};
  const START_FROM = 45; // Começa do 45 para continuar de onde parou! (Mude para 1 se quiser rodar todos de novo)

  const banner = document.createElement("div");
  banner.style = "position:fixed;top:0;left:0;width:100%;z-index:999999;background:#f5c518;color:#000;padding:16px;font-size:18px;font-weight:bold;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.4);font-family:sans-serif;";
  document.body.appendChild(banner);

  console.log(`🎬 Continuando envio de notas do item ${{START_FROM}} até ${{items.length}} no IMDb...`);
  const sleep = (ms) => new Promise(r => setTimeout(r, ms));
  let ok = 0;

  for (let i = START_FROM - 1; i < items.length; i++) {{
    const item = items[i];
    banner.innerText = `⏳ Atualizando IMDb: [${{i+1}}/${{items.length}}] ${{item.notion_name}} (Nota ${{item.rating}}/10) — NÃO mude de página!`;
    try {{
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
      ok++;
      console.log(`✅ [${{i+1}}/${{items.length}}] Nota ${{item.rating}}/10 -> ${{item.notion_name}} (${{item.title}} - ${{item.id}})`);
      await sleep(600);
    }} catch (err) {{
      console.error(`❌ Erro em ${{item.notion_name}} (${{item.id}}):`, err);
    }}
  }}
  banner.style.background = "#16a34a";
  banner.style.color = "#fff";
  banner.innerText = `🎉 PRONTO! Todos os 98 Doramas foram avaliados na sua conta do IMDb! Já pode navegar normalmente!`;
  console.log(`🎉 Concluído! ${{ok}} doramas restantes avaliados na sua conta do IMDb!`);
}})();
"""

with open("aplicar_notas_98_doramas_console.js", "w", encoding="utf-8") as f:
    f.write(js_script)
print("Atualizado!")

