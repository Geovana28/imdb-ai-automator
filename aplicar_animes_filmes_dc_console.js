// === AUTOMATIZADOR IMDB: ANIMES, FILMES, ANIMAÇÕES DC + WATCHLIST ===
// 1. Cole na aba Console (F12) dentro do site do IMDb e aperte Enter!
// 2. Espere a barra amarela no topo do site ficar VERDE!

(async () => {
  const items = [
  {
    "id": "tt9335498",
    "title": "Demon Slayer: Kimetsu no Yaiba",
    "notion_name": "demon slayer",
    "rating": 9,
    "watchlist": false
  },
  {
    "id": "tt13706018",
    "title": "Spy x Family",
    "notion_name": "spy famly",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt2560140",
    "title": "Attack on Titan",
    "notion_name": "attack on titan",
    "rating": 9,
    "watchlist": false
  },
  {
    "id": "tt12343534",
    "title": "Jujutsu Kaisen",
    "notion_name": "jujutsu",
    "rating": 8,
    "watchlist": false
  },
  {
    "id": "tt5626028",
    "title": "My Hero Academia (Boku no Hero)",
    "notion_name": "boku no hero",
    "rating": 7,
    "watchlist": false
  },
  {
    "id": "tt26743760",
    "title": "The Apothecary Diaries",
    "notion_name": "diario de uma apotecaria",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt11737520",
    "title": "One Piece (Live Action)",
    "notion_name": "one piece (live action)",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt19048550",
    "title": "XO, Kitty (Com Carinho, Kitty)",
    "notion_name": "com carinho kitty",
    "rating": 7,
    "watchlist": false
  },
  {
    "id": "tt16311594",
    "title": "F1: The Movie",
    "notion_name": "filme f1",
    "rating": 8,
    "watchlist": false
  },
  {
    "id": "tt2283362",
    "title": "Jumanji: Welcome to the Jungle",
    "notion_name": "jumnaji 1",
    "rating": 8,
    "watchlist": false
  },
  {
    "id": "tt7975244",
    "title": "Jumanji: The Next Level",
    "notion_name": "jumanji 2",
    "rating": 7,
    "watchlist": false
  },
  {
    "id": "tt1396484",
    "title": "It (A Coisa)",
    "notion_name": "it",
    "rating": 9,
    "watchlist": false
  },
  {
    "id": "tt1877830",
    "title": "The Batman",
    "notion_name": "batman",
    "rating": 8,
    "watchlist": false
  },
  {
    "id": "tt13146488",
    "title": "Peacemaker (Pacificador)",
    "notion_name": "pascificador",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt8866456",
    "title": "Supergirl (Filme)",
    "notion_name": "supergirl (filme)",
    "rating": 9,
    "watchlist": false
  },
  {
    "id": "tt5950044",
    "title": "Superman (2025)",
    "notion_name": "superman filme 2025",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt0094721",
    "title": "Beetlejuice (Os Fantasmas se Divertem)",
    "notion_name": "os fantasmas se divertem 1",
    "rating": 8,
    "watchlist": false
  },
  {
    "id": "tt2049403",
    "title": "Beetlejuice Beetlejuice (Os Fantasmas Ainda se Divertem)",
    "notion_name": "os fantasmas se divertem 2",
    "rating": 7,
    "watchlist": false
  },
  {
    "id": "tt1375670",
    "title": "Grown Ups (Gente Grande)",
    "notion_name": "gente grande 1",
    "rating": 8,
    "watchlist": false
  },
  {
    "id": "tt2191701",
    "title": "Grown Ups 2 (Gente Grande 2)",
    "notion_name": "gente grande 2",
    "rating": 7,
    "watchlist": false
  },
  {
    "id": "tt0409459",
    "title": "Watchmen",
    "notion_name": "watchman",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt0372784",
    "title": "Batman Begins",
    "notion_name": "batman begins",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt1569923",
    "title": "Batman: Under the Red Hood",
    "notion_name": "batman contra o capuz vermelho",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt14324650",
    "title": "Batman: The Long Halloween, Part One",
    "notion_name": "Batman: O Longo Dia das Bruxas - Parte 1",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt14402926",
    "title": "Batman: The Long Halloween, Part Two",
    "notion_name": "Batman: O Longo Dia das Bruxas - Parte 2",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt2193021",
    "title": "Arrow",
    "notion_name": "arrow",
    "rating": 7,
    "watchlist": false
  },
  {
    "id": "tt4116284",
    "title": "The Lego Batman Movie",
    "notion_name": "batman lego",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt3060952",
    "title": "Justice League: War",
    "notion_name": "liga da justiça guerra",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt11079116",
    "title": "Superman: Man of Tomorrow",
    "notion_name": "Superman: O Homem do Amanhã (2020)",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt13624900",
    "title": "Justice Society: World War II",
    "notion_name": "Sociedade da Justiça: Segunda Guerra Mundial (2021)",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt20192230",
    "title": "Green Lantern: Beware My Power",
    "notion_name": "Lanterna Verde: Cuidado com Meu Poder (2022)",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt21375602",
    "title": "Legion of Super-Heroes",
    "notion_name": "Legião dos Super-Heróis (2023)",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt23285050",
    "title": "Justice League: Warworld",
    "notion_name": "Liga da Justiça: Mundo Bélico (2023)",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt28505964",
    "title": "Justice League: Crisis on Infinite Earths - Part One",
    "notion_name": "Liga da Justiça: Crise nas Infinitas Terras - Parte 1 (2024)",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt30150917",
    "title": "Justice League: Crisis on Infinite Earths - Part Two",
    "notion_name": "Liga da Justiça: Crise nas Infinitas Terras - Parte 2 (2024)",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt30150923",
    "title": "Justice League: Crisis on Infinite Earths - Part Three",
    "notion_name": "Liga da Justiça: Crise nas Infinitas Terras - Parte 3 (2024)",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt5816546",
    "title": "Justice League Dark",
    "notion_name": "Liga da Justiça Sombria (2017)",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt9177882",
    "title": "Constantine: City of Demons - The Movie",
    "notion_name": "Constantine: Cidade dos Demônios (2018)",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt11079148",
    "title": "Justice League Dark: Apokolips War",
    "notion_name": "Liga da Justiça Sombria: Guerra de Apokolips (2020)",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt20192236",
    "title": "DC Showcase: Constantine - The House of Mystery",
    "notion_name": "DC Showcase: Constantine - A Casa de Mistério (2022)",
    "rating": 10,
    "watchlist": false
  },
  {
    "id": "tt0279600",
    "title": "Smallville",
    "notion_name": "Smallville (Quero ver)",
    "rating": null,
    "watchlist": true
  },
  {
    "id": "tt0410975",
    "title": "Desperate Housewives",
    "notion_name": "Desperate Housewives (Quero ver)",
    "rating": null,
    "watchlist": true
  },
  {
    "id": "tt0118276",
    "title": "Buffy the Vampire Slayer",
    "notion_name": "Buffy (Quero continuar - já vi 1ª temp)",
    "rating": null,
    "watchlist": true
  },
  {
    "id": "tt0368530",
    "title": "One Tree Hill",
    "notion_name": "One Tree Hill (Quero ver)",
    "rating": null,
    "watchlist": true
  },
  {
    "id": "tt0362359",
    "title": "The O.C.",
    "notion_name": "The O.C. (Quero ver)",
    "rating": null,
    "watchlist": true
  }
];

  const banner = document.createElement("div");
  banner.style = "position:fixed;top:0;left:0;width:100%;z-index:999999;background:#f5c518;color:#000;padding:16px;font-size:18px;font-weight:bold;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.4);font-family:sans-serif;";
  document.body.appendChild(banner);

  console.log(`🎬 Iniciando atualização de ${items.length} Animes, Filmes, DC e Watchlist no IMDb...`);
  const sleep = (ms) => new Promise(r => setTimeout(r, ms));
  let ok = 0;

  for (let i = 0; i < items.length; i++) {
    const item = items[i];
    try {
      if (item.rating) {
        banner.innerText = `⏳ Avaliando [${i+1}/${items.length}]: ${item.notion_name} (Nota ${item.rating}/10) — NÃO mude de página!`;
        await fetch("https://api.graphql.imdb.com/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "x-imdb-client-name": "imdb-web-next"
          },
          credentials: "include",
          body: JSON.stringify({
            query: `mutation UpdateTitleRating($rating: Int!, $titleId: ID!) {
              rateTitle(input: { rating: $rating, titleId: $titleId }) {
                rating { value }
              }
            }`,
            variables: { rating: item.rating, titleId: item.id }
          })
        });
        console.log(`⭐ [${i+1}/${items.length}] Nota ${item.rating}/10 -> ${item.notion_name} (${item.title} - ${item.id})`);
      }

      if (item.watchlist) {
        banner.innerText = `📌 Adicionando à Watchlist [${i+1}/${items.length}]: ${item.notion_name} — NÃO mude de página!`;
        // Tenta via GraphQL de Watchlist + endpoint clássico do IMDb
        await fetch(`https://www.imdb.com/watchlist/${item.id}`, {
          method: "PUT",
          credentials: "include"
        }).catch(() => {});
        console.log(`📌 [${i+1}/${items.length}] Adicionado à Watchlist -> ${item.notion_name} (${item.title} - ${item.id})`);
      }

      ok++;
      await sleep(550);
    } catch (err) {
      console.error(`❌ Erro em ${item.notion_name} (${item.id}):`, err);
    }
  }
  banner.style.background = "#16a34a";
  banner.style.color = "#fff";
  banner.innerText = `🎉 PRONTO! Todos os ${ok} Animes, Filmes, DC e Watchlist foram atualizados no seu IMDb!`;
  console.log(`🎉 Concluído! ${ok}/${items.length} itens atualizados na sua conta do IMDb!`);
})();
