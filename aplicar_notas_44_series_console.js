// === AUTOMATIZADOR IMDB: 44 SÉRIES ===
// 1. Cole na aba Console (F12) dentro do site do IMDb e aperte Enter!
// 2. Espere a barra amarela no topo do site ficar VERDE!

(async () => {
  const items = [
  {
    "id": "tt3107288",
    "title": "The Flash",
    "notion_name": "The Flash",
    "rating": 8
  },
  {
    "id": "tt5706996",
    "title": "Girlboss",
    "notion_name": "Girlboss",
    "rating": 6
  },
  {
    "id": "tt2632424",
    "title": "The Originals",
    "notion_name": "The originals",
    "rating": 8
  },
  {
    "id": "tt4574334",
    "title": "Stranger Things",
    "notion_name": "Stranger Things",
    "rating": 8
  },
  {
    "id": "tt4276624",
    "title": "Krypton",
    "notion_name": "Krypton",
    "rating": 7
  },
  {
    "id": "tt4016454",
    "title": "Supergirl",
    "notion_name": "Supergirl",
    "rating": 7
  },
  {
    "id": "tt5753856",
    "title": "Dark",
    "notion_name": "Dark",
    "rating": 10
  },
  {
    "id": "tt4667888",
    "title": "Slasher",
    "notion_name": "Slasher",
    "rating": 7
  },
  {
    "id": "tt5420376",
    "title": "Riverdale",
    "notion_name": "Riverdale",
    "rating": 6
  },
  {
    "id": "tt1405406",
    "title": "The Vampire Diaries",
    "notion_name": "The Vampire Diares",
    "rating": 7
  },
  {
    "id": "tt4532368",
    "title": "DC's Legends of Tomorrow",
    "notion_name": "Dc's Legends of Tomorrow",
    "rating": 8
  },
  {
    "id": "tt0413573",
    "title": "Grey's Anatomy",
    "notion_name": "Grey's Anatomy",
    "rating": 7
  },
  {
    "id": "tt6461812",
    "title": "Deception",
    "notion_name": "Deception",
    "rating": 5
  },
  {
    "id": "tt4145054",
    "title": "Shadowhunters",
    "notion_name": "Shadowhunters",
    "rating": 6
  },
  {
    "id": "tt6468322",
    "title": "Money Heist (La Casa de Papel)",
    "notion_name": "La casa de papel",
    "rating": 7
  },
  {
    "id": "tt1830617",
    "title": "Grimm",
    "notion_name": "Grimm",
    "rating": 8
  },
  {
    "id": "tt6128300",
    "title": "Dynasty",
    "notion_name": "Dynasty",
    "rating": 9
  },
  {
    "id": "tt2306299",
    "title": "Vikings",
    "notion_name": "Vikings",
    "rating": 10
  },
  {
    "id": "tt3501584",
    "title": "iZombie",
    "notion_name": "izombie",
    "rating": 9
  },
  {
    "id": "tt1837492",
    "title": "13 Reasons Why",
    "notion_name": "13 Reasons Why",
    "rating": 7
  },
  {
    "id": "tt0460681",
    "title": "Supernatural",
    "notion_name": "Supernatural",
    "rating": 9
  },
  {
    "id": "tt4052886",
    "title": "Lucifer",
    "notion_name": "Lucifer",
    "rating": 8
  },
  {
    "id": "tt4834206",
    "title": "A Series of Unfortunate Events",
    "notion_name": "Desventuras em séries",
    "rating": 7
  },
  {
    "id": "tt6257970",
    "title": "The End of the F***ing World",
    "notion_name": "The End Of The Fucking World",
    "rating": 8
  },
  {
    "id": "tt1567432",
    "title": "Teen Wolf",
    "notion_name": "Teen Wolf",
    "rating": 9
  },
  {
    "id": "tt6884380",
    "title": "The Protector (O Último Guardião)",
    "notion_name": "O último guardião",
    "rating": 8
  },
  {
    "id": "tt2467372",
    "title": "Brooklyn Nine-Nine",
    "notion_name": "Brooklyn nine nine",
    "rating": 10
  },
  {
    "id": "tt1043813",
    "title": "Titans",
    "notion_name": "Titans",
    "rating": 7
  },
  {
    "id": "tt7335184",
    "title": "You",
    "notion_name": "You",
    "rating": 7
  },
  {
    "id": "tt6487482",
    "title": "Insatiable",
    "notion_name": "Insatiable",
    "rating": 7
  },
  {
    "id": "tt2661044",
    "title": "The 100",
    "notion_name": "The 100",
    "rating": 9
  },
  {
    "id": "tt7645192",
    "title": "Baby",
    "notion_name": "Baby",
    "rating": 5
  },
  {
    "id": "tt7134908",
    "title": "Elite",
    "notion_name": "Elite",
    "rating": 6
  },
  {
    "id": "tt9421868",
    "title": "Go! Live Your Way",
    "notion_name": "Go! Viva a tu maneira",
    "rating": 7
  },
  {
    "id": "tt8778064",
    "title": "The Society",
    "notion_name": "The society",
    "rating": 9
  },
  {
    "id": "tt7767422",
    "title": "Sex Education",
    "notion_name": "Sex education",
    "rating": 9
  },
  {
    "id": "tt7569592",
    "title": "Chilling Adventures of Sabrina",
    "notion_name": "O mundo sombrio de Sabrina",
    "rating": 8
  },
  {
    "id": "tt5180504",
    "title": "The Witcher",
    "notion_name": "The Witcher",
    "rating": 8
  },
  {
    "id": "tt3007572",
    "title": "Locke & Key",
    "notion_name": "Lokce&Key",
    "rating": 6
  },
  {
    "id": "tt1312171",
    "title": "The Umbrella Academy",
    "notion_name": "The umbrella academy",
    "rating": 8
  },
  {
    "id": "tt9446688",
    "title": "I Am Not Okay with This",
    "notion_name": "i am not okay with this",
    "rating": 7
  },
  {
    "id": "tt10795658",
    "title": "Alice in Borderland",
    "notion_name": "Alice in Borderland",
    "rating": 10
  },
  {
    "id": "tt8878862",
    "title": "Invisible City (Cidade Invisível)",
    "notion_name": "Cidade Invisível",
    "rating": 8
  },
  {
    "id": "tt2403776",
    "title": "Shadow and Bone (Sombra e Ossos)",
    "notion_name": "Sombra e ossos",
    "rating": 8
  }
];

  const banner = document.createElement("div");
  banner.style = "position:fixed;top:0;left:0;width:100%;z-index:999999;background:#f5c518;color:#000;padding:16px;font-size:18px;font-weight:bold;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.4);font-family:sans-serif;";
  document.body.appendChild(banner);

  console.log(`🎬 Iniciando envio de notas para ${items.length} Séries no IMDb...`);
  const sleep = (ms) => new Promise(r => setTimeout(r, ms));
  let ok = 0;

  for (let i = 0; i < items.length; i++) {
    const item = items[i];
    banner.innerText = `⏳ Avaliando Séries: [${i+1}/${items.length}] ${item.notion_name} (Nota ${item.rating}/10) — NÃO mude de página!`;
    try {
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
      ok++;
      console.log(`✅ [${i+1}/${items.length}] Nota ${item.rating}/10 -> ${item.notion_name} (${item.title} - ${item.id})`);
      await sleep(550);
    } catch (err) {
      console.error(`❌ Erro em ${item.notion_name} (${item.id}):`, err);
    }
  }
  banner.style.background = "#16a34a";
  banner.style.color = "#fff";
  banner.innerText = `🎉 PRONTO! Todas as ${ok} Séries foram avaliadas no seu IMDb!`;
  console.log(`🎉 Concluído! ${ok}/${items.length} séries avaliadas na sua conta do IMDb!`);
})();
