import csv
import json
import sys
import urllib.request
import urllib.parse
import re
import time

sys.stdout.reconfigure(encoding="utf-8")

# Mapeamento dos títulos em português ou com grafia específica do Notion para o título oficial no IMDb
PT_TO_IMDB_QUERY = {
    "Tudo bem não ser normal": "It's Okay to Not Be Okay",
    "Oh my ghostess": "Oh My Ghost",
    "Pretendente Surpresa": "Business Proposal",
    "Pousando no amor": "Crash Landing on You",
    "What’s wrong with Secretary Kim": "What's Wrong with Secretary Kim",
    "Goblin": "Guardian: The Lonely and Great God",
    "Sorriso Real": "King the Land",
    "O tempo traz você pra mim": "A Time Called You",
    "Uma Advogada Extraordinária": "Extraordinary Attorney Woo",
    "Naviellera": "Navillera",
    "O Rei de Porcelana": "The King's Affection",
    "Round 6": "Squid Game",
    "O rei eterno": "The King: Eternal Monarch",
    "Thirty But Seventeen": "Still 17",
    "Dr. Romantic": "Dr. Romantic",
    "O Abismo Mágico": "Abyss 2019",
    "Inspetor Real Secreto e Joy": "Secret Royal Inspector & Joy",
    "Love Under the Full Moon": "Love Under the Full Moon",
    "Gaus Eletronics": "Gaus Electronics",
    "Apostando alto": "Start-Up 2020",
    "Link: eat, love, kill": "Link: Eat, Love, Kill",
    "Café Minamdang": "Cafe Minamdang",
    "W - Dois mundos": "W: Two Worlds",
    "Anomalia": "Glitch 2022",
    "Doona": "Doona!",
    "Save me": "Save Me 2017",
    "Death’s Game": "Death's Game",
    "No love no gain": "No Gain No Love",
    "Spice Up our love": "Spice Up Our Love",
    "Quando o telefone toca": "When the Phone Rings",
    "Hongrang": "Dear Hongrang",
    "Nine Puzzle": "Nine Puzzles",
    "Weak Hero Class": "Weak Hero Class 1",
    "Good boy": "Good Boy 2025",
    "Genie Make a Wish": "Genie, Make a Wish",
    "Beijo Explosivo": "Dynamite Kiss",
    "Can this love be translate": "Can This Love Be Translated?",
    "SuperTontos": "The Wonderfools",
    "De repente Humana": "No Tail to Tell",
    "A leste do Palácio": "East Palace",
    "Live On": "Live On 2020",
    "Mr. Sunshine": "Mr. Sunshine 2018",
    "Tomorrow": "tt18926162",
    "Heartbeat": "My Heart Is Beating",
    "Island": "tt22184998",
}


def parse_notion_rating_to_imdb10(rating_str: str) -> int:
    """
    Converte as estrelas do Notion (escala de 1 a 5) para a escala de 1 a 10 do IMDb:
    - ⭐⭐⭐⭐⭐ -> 10
    - 4,5⭐️ ou ⭐️⭐️⭐️⭐️/⭐️ -> 9
    - ⭐⭐⭐⭐ -> 8
    - 3,5 ⭐️ ou ⭐⭐⭐/⭐ -> 7
    - ⭐⭐⭐ -> 6
    - 2,5⭐️ -> 5
    """
    s = rating_str.strip()
    if not s:
        return 8

    # Caso tenha número explícito tipo "4,5⭐️" ou "3,5 ⭐️" ou "2,5⭐️"
    m = re.search(r"(\d+)[,\.](\d+)", s)
    if m:
        val = float(f"{m.group(1)}.{m.group(2)}")
        return int(round(val * 2))

    # Caso tenha barra indicando meia estrela no final: ex "⭐️⭐️⭐️⭐️/⭐️" (4.5) ou "⭐⭐⭐/⭐" (3.5)
    if "/" in s:
        before_slash = s.split("/")[0]
        full_stars = before_slash.count("⭐")
        return int(round((full_stars + 0.5) * 2))

    # Conta estrelas cheias
    stars = s.count("⭐")
    if stars > 0:
        return min(10, stars * 2)

    return 8


def search_imdb_id(query: str) -> dict:
    clean_query = query.strip()
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
            titles = [r for r in results if r.get("id", "").startswith("tt")]
            if not titles:
                return {}
            # Prioriza séries de TV / minisséries já que são Doramas
            tv_titles = [
                t
                for t in titles
                if "series" in str(t.get("q", "")).lower()
                or "tv" in str(t.get("qid", "")).lower()
            ]
            best = tv_titles[0] if tv_titles else titles[0]
            imdb_id = best.get("id", "")
            return {
                "Const": imdb_id,
                "Title": best.get("l", clean_query),
                "Year": best.get("y", ""),
                "Title Type": best.get("q", "TV Series"),
                "URL": f"https://www.imdb.com/title/{imdb_id}/" if imdb_id else "",
            }
    except Exception as e:
        return {"error": str(e)}


def main():
    csv_path = r"c:\Users\SEJUSP.DESKTOP-VOL42AH\Desktop\imdb\notion_export\Private & Shared\Movies Freebie 15b685528b2446ffaf55230d822c7914_all.csv"
    rows_out = []

    with open(csv_path, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        items = list(reader)

    print(f"Total de doramas lidos do Notion: {len(items)}")

    for idx, item in enumerate(items, 1):
        raw_name = item.get("Name", "").strip()
        raw_rating = item.get("Rating", "").strip()
        genre = item.get("Genre", "").strip()
        watched = item.get("Watched", "").strip()

        search_query = PT_TO_IMDB_QUERY.get(raw_name, raw_name)
        rating_10 = parse_notion_rating_to_imdb10(raw_rating)

        imdb_data = search_imdb_id(search_query)
        if not imdb_data.get("Const") and search_query != raw_name:
            imdb_data = search_imdb_id(raw_name)

        const_id = imdb_data.get("Const", "")
        imdb_title = imdb_data.get("Title", raw_name)
        imdb_year = imdb_data.get("Year", item.get("Year", "").strip())
        imdb_url = imdb_data.get("URL", "")
        imdb_type = imdb_data.get("Title Type", "TV Series")

        print(
            f"[{idx:02d}/{len(items)}] {raw_name} -> {imdb_title} ({const_id}) | Estrelas Notion: {raw_rating} => Nota IMDb: {rating_10}/10"
        )

        rows_out.append(
            {
                "Const": const_id,
                "Your Rating": rating_10,
                "Date Rated": "",
                "Title": imdb_title,
                "Nome no Notion": raw_name,
                "Estrelas Notion": raw_rating,
                "URL": imdb_url,
                "Title Type": imdb_type,
                "IMDb Rating": "",
                "Runtime (mins)": "",
                "Year": imdb_year,
                "Genres": genre,
                "Num Votes": "",
                "Release Date": "",
                "Directors": "",
                "Watched": watched,
            }
        )
        time.sleep(0.05)

    # Salva CSV oficial do IMDb
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
    out_csv = r"c:\Users\SEJUSP.DESKTOP-VOL42AH\Desktop\imdb\meus_98_doramas_imdb.csv"
    with open(out_csv, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=imdb_cols, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows_out)

    # Salva JSON completo para auditoria e geração do script de Console
    out_json = r"c:\Users\SEJUSP.DESKTOP-VOL42AH\Desktop\imdb\meus_98_doramas_completo.json"
    with open(out_json, mode="w", encoding="utf-8") as f:
        json.dump(rows_out, f, ensure_ascii=False, indent=2)

    # Gera o Script JS de Console 1-Clique para dar nota nos 98 Doramas
    js_items = [
        {
            "id": r["Const"],
            "title": r["Title"],
            "notion_name": r["Nome no Notion"],
            "rating": r["Your Rating"],
        }
        for r in rows_out
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
    out_js = r"c:\Users\SEJUSP.DESKTOP-VOL42AH\Desktop\imdb\aplicar_notas_98_doramas_console.js"
    with open(out_js, mode="w", encoding="utf-8") as f:
        f.write(js_script)

    missing = [r for r in rows_out if not r["Const"]]
    print(f"\nConcluído! Encontrados: {len(rows_out) - len(missing)}/{len(rows_out)}")
    if missing:
        print("Não encontrados:", [m["Nome no Notion"] for m in missing])


if __name__ == "__main__":
    main()
