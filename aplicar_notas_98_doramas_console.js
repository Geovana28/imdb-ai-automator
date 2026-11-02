// === AUTOMATIZADOR IMDB: 98 DORAMAS DO NOTION (COM BARRA VISUAL NA TELA) ===
// Como usar:
// 1. Abra https://www.imdb.com no navegador (logado na sua conta)
// 2. Aperte F12 -> Clique na aba "Console"
// 3. Cole todo este código e aperte Enter!
// 4. Espere a barra amarela no topo do site ficar VERDE antes de mudar de página!

(async () => {
  const items = [
  {
    "id": "tt13274038",
    "title": "True Beauty",
    "notion_name": "True Beauty",
    "rating": 8
  },
  {
    "id": "tt12451520",
    "title": "It's Okay to Not Be Okay",
    "notion_name": "Tudo bem não ser normal",
    "rating": 10
  },
  {
    "id": "tt5646594",
    "title": "Hwarang: The Poet Warrior Youth",
    "notion_name": "Hwarang",
    "rating": 8
  },
  {
    "id": "tt4799574",
    "title": "Oh My Ghost",
    "notion_name": "Oh my ghostess",
    "rating": 8
  },
  {
    "id": "tt13642264",
    "title": "A Love So Beautiful",
    "notion_name": "A Love So Beautiful",
    "rating": 8
  },
  {
    "id": "tt14819828",
    "title": "Business Proposal",
    "notion_name": "Pretendente Surpresa",
    "rating": 8
  },
  {
    "id": "tt13273946",
    "title": "Live On",
    "notion_name": "Live On",
    "rating": 6
  },
  {
    "id": "tt10850932",
    "title": "Crash Landing on You",
    "notion_name": "Pousando no amor",
    "rating": 8
  },
  {
    "id": "tt9899340",
    "title": "Her Private Life",
    "notion_name": "Her Private Life",
    "rating": 8
  },
  {
    "id": "tt8242904",
    "title": "What's Wrong with Secretary Kim",
    "notion_name": "What’s wrong with Secretary Kim",
    "rating": 8
  },
  {
    "id": "tt9130542",
    "title": "Romance Is a Bonus Book",
    "notion_name": "Romance is a bonus book",
    "rating": 8
  },
  {
    "id": "tt5994364",
    "title": "Guardian: The Lonely and Great God",
    "notion_name": "Goblin",
    "rating": 8
  },
  {
    "id": "tt6263222",
    "title": "Strong Girl Bong-soon",
    "notion_name": "Strong Woman Do Bong Soon",
    "rating": 10
  },
  {
    "id": "tt26693803",
    "title": "King the Land",
    "notion_name": "Sorriso Real",
    "rating": 8
  },
  {
    "id": "tt21627438",
    "title": "A Time Called You",
    "notion_name": "O tempo traz você pra mim",
    "rating": 8
  },
  {
    "id": "tt20869502",
    "title": "Extraordinary Attorney Woo",
    "notion_name": "Uma Advogada Extraordinária",
    "rating": 10
  },
  {
    "id": "tt13885302",
    "title": "Navillera",
    "notion_name": "Naviellera",
    "rating": 8
  },
  {
    "id": "tt14609428",
    "title": "The King's Affection",
    "notion_name": "O Rei de Porcelana",
    "rating": 8
  },
  {
    "id": "tt10919420",
    "title": "Squid Game",
    "notion_name": "Round 6",
    "rating": 8
  },
  {
    "id": "tt7094780",
    "title": "Mr. Sunshine",
    "notion_name": "Mr. Sunshine",
    "rating": 8
  },
  {
    "id": "tt13433812",
    "title": "Vincenzo",
    "notion_name": "Vincenzo",
    "rating": 10
  },
  {
    "id": "tt11228748",
    "title": "The King: Eternal Monarch",
    "notion_name": "O rei eterno",
    "rating": 8
  },
  {
    "id": "tt15026724",
    "title": "Our Beloved Summer",
    "notion_name": "Our Beloved Summer",
    "rating": 10
  },
  {
    "id": "tt10795658",
    "title": "Alice in Borderland",
    "notion_name": "Alice In Borderland",
    "rating": 10
  },
  {
    "id": "tt11239552",
    "title": "Itaewon Class",
    "notion_name": "Itaewon Class",
    "rating": 8
  },
  {
    "id": "tt27838483",
    "title": "See You in My 19th Life",
    "notion_name": "See you in my 19th life",
    "rating": 8
  },
  {
    "id": "tt8648696",
    "title": "Still 17",
    "notion_name": "Thirty But Seventeen",
    "rating": 8
  },
  {
    "id": "tt6157190",
    "title": "Dr. Romantic",
    "notion_name": "Dr. Romantic",
    "rating": 10
  },
  {
    "id": "tt10055734",
    "title": "Abyss",
    "notion_name": "O Abismo Mágico",
    "rating": 6
  },
  {
    "id": "tt13669128",
    "title": "Doom at Your Service",
    "notion_name": "Doom At your service",
    "rating": 10
  },
  {
    "id": "tt15181094",
    "title": "Thirty Nine",
    "notion_name": "Thirty-Nine",
    "rating": 8
  },
  {
    "id": "tt18926162",
    "title": "Tomorrow",
    "notion_name": "Tomorrow",
    "rating": 10
  },
  {
    "id": "tt10826102",
    "title": "Extraordinary You",
    "notion_name": "Extraordinary You",
    "rating": 10
  },
  {
    "id": "tt15672294",
    "title": "Crazy Love",
    "notion_name": "Crazy Love",
    "rating": 8
  },
  {
    "id": "tt20859920",
    "title": "Alchemy of Souls",
    "notion_name": "Alchemy of souls",
    "rating": 10
  },
  {
    "id": "tt24640580",
    "title": "Moving",
    "notion_name": "Moving",
    "rating": 10
  },
  {
    "id": "tt27203727",
    "title": "My Lovely Liar",
    "notion_name": "My lovely Liar",
    "rating": 10
  },
  {
    "id": "tt26085372",
    "title": "Heartbeat",
    "notion_name": "Heartbeat",
    "rating": 6
  },
  {
    "id": "tt15181018",
    "title": "Secret Royal Inspector Joy",
    "notion_name": "Inspetor Real Secreto e Joy",
    "rating": 8
  },
  {
    "id": "tt27042206",
    "title": "The Good Bad Mother",
    "notion_name": "The Good Bad Mother",
    "rating": 10
  },
  {
    "id": "tt15327230",
    "title": "Love Under the Full Moon",
    "notion_name": "Love Under the Full Moon",
    "rating": 6
  },
  {
    "id": "tt22873700",
    "title": "Gaus Electronics",
    "notion_name": "Gaus Eletronics",
    "rating": 10
  },
  {
    "id": "tt22184998",
    "title": "Picnic Shelter Rain 9 Hours",
    "notion_name": "Island",
    "rating": 8
  },
  {
    "id": "tt6256484",
    "title": "While You Were Sleeping",
    "notion_name": "While you were sleeping",
    "rating": 8
  },
  {
    "id": "tt15146202",
    "title": "Bad and Crazy",
    "notion_name": "Bad and crazy",
    "rating": 8
  },
  {
    "id": "tt6157148",
    "title": "Weightlifting Fairy Kim Bok-Joo",
    "notion_name": "Weightlifting Fairy Kim Bok Joo",
    "rating": 10
  },
  {
    "id": "tt18970038",
    "title": "Soundtrack #1",
    "notion_name": "Soundtrack #1",
    "rating": 6
  },
  {
    "id": "tt13304700",
    "title": "Snowdrop",
    "notion_name": "Snowdrop",
    "rating": 8
  },
  {
    "id": "tt19115260",
    "title": "Our Blues",
    "notion_name": "Our Blues",
    "rating": 10
  },
  {
    "id": "tt12867810",
    "title": "Start-Up",
    "notion_name": "Apostando alto",
    "rating": 5
  },
  {
    "id": "tt20869584",
    "title": "Link: Eat, Love, Kill",
    "notion_name": "Link: eat, love, kill",
    "rating": 7
  },
  {
    "id": "tt21049186",
    "title": "Cafe Minamdang",
    "notion_name": "Café Minamdang",
    "rating": 6
  },
  {
    "id": "tt26228426",
    "title": "The Heavenly Idol",
    "notion_name": "The Heavenly Idol",
    "rating": 6
  },
  {
    "id": "tt5797194",
    "title": "W",
    "notion_name": "W - Dois mundos",
    "rating": 8
  },
  {
    "id": "tt14979052",
    "title": "Happiness",
    "notion_name": "Happiness",
    "rating": 10
  },
  {
    "id": "tt14735382",
    "title": "Glitch",
    "notion_name": "Anomalia",
    "rating": 8
  },
  {
    "id": "tt27440576",
    "title": "My Lovely Boxer",
    "notion_name": "My Lovely Boxer",
    "rating": 8
  },
  {
    "id": "tt27974068",
    "title": "Destined with You",
    "notion_name": "Destined with you",
    "rating": 6
  },
  {
    "id": "tt24245988",
    "title": "Doona!",
    "notion_name": "Doona",
    "rating": 8
  },
  {
    "id": "tt7020532",
    "title": "Save Me",
    "notion_name": "Save me",
    "rating": 6
  },
  {
    "id": "tt29225198",
    "title": "Strong Girl Nam-soon",
    "notion_name": "Strong Girl Nam Soon",
    "rating": 6
  },
  {
    "id": "tt25900250",
    "title": "Our Blooming Youth",
    "notion_name": "Our Blooming Youth",
    "rating": 8
  },
  {
    "id": "tt29657033",
    "title": "Perfect Marriage Revenge",
    "notion_name": "Perfect Marriage Revenge",
    "rating": 8
  },
  {
    "id": "tt26225038",
    "title": "Death's Game",
    "notion_name": "Death’s Game",
    "rating": 9
  },
  {
    "id": "tt26679485",
    "title": "The Story of Park's Marriage Contract",
    "notion_name": "The Story Of Park's Marriage Contract",
    "rating": 8
  },
  {
    "id": "tt27446493",
    "title": "Twinkling Watermelon",
    "notion_name": "Twinkling Watermelon",
    "rating": 8
  },
  {
    "id": "tt29569035",
    "title": "My Demon",
    "notion_name": "My Demon",
    "rating": 8
  },
  {
    "id": "tt30333634",
    "title": "Queen of Divorce",
    "notion_name": "Queen of divorce",
    "rating": 6
  },
  {
    "id": "tt27135274",
    "title": "Doctor Slump",
    "notion_name": "Doctor Slump",
    "rating": 8
  },
  {
    "id": "tt27668559",
    "title": "Queen of Tears",
    "notion_name": "Queen of Tears",
    "rating": 10
  },
  {
    "id": "tt31324295",
    "title": "Lovely Runner",
    "notion_name": "Lovely Runner",
    "rating": 10
  },
  {
    "id": "tt15201944",
    "title": "Moonshine",
    "notion_name": "Moonshine",
    "rating": 8
  },
  {
    "id": "tt32380398",
    "title": "My Sweet Mobster",
    "notion_name": "My Sweet Mobster",
    "rating": 8
  },
  {
    "id": "tt32914942",
    "title": "Serendipity's Embrace",
    "notion_name": "Serendipity’s Embrace",
    "rating": 8
  },
  {
    "id": "tt27554432",
    "title": "Queen Woo",
    "notion_name": "Queen Woo",
    "rating": 8
  },
  {
    "id": "tt32981987",
    "title": "No Gain No Love",
    "notion_name": "No love no gain",
    "rating": 8
  },
  {
    "id": "tt33143834",
    "title": "Spice Up Our Love",
    "notion_name": "Spice Up our love",
    "rating": 10
  },
  {
    "id": "tt30446769",
    "title": "Love Next Door",
    "notion_name": "Love Next Door",
    "rating": 8
  },
  {
    "id": "tt27539317",
    "title": "Mr. Plankton",
    "notion_name": "Mr. Plankton",
    "rating": 8
  },
  {
    "id": "tt33503491",
    "title": "When the Phone Rings",
    "notion_name": "Quando o telefone toca",
    "rating": 8
  },
  {
    "id": "tt30365813",
    "title": "Family by Choice",
    "notion_name": "Family by Choice",
    "rating": 9
  },
  {
    "id": "tt35304338",
    "title": "Study Group",
    "notion_name": "Study Group",
    "rating": 9
  },
  {
    "id": "tt33364760",
    "title": "Undercover High School",
    "notion_name": "Undercover High School",
    "rating": 10
  },
  {
    "id": "tt33578048",
    "title": "Way Back Love",
    "notion_name": "Way Back Love",
    "rating": 9
  },
  {
    "id": "tt27554348",
    "title": "Dear Hongrang",
    "notion_name": "Hongrang",
    "rating": 6
  },
  {
    "id": "tt31171500",
    "title": "Resident Playbook",
    "notion_name": "Resident Playbook",
    "rating": 10
  },
  {
    "id": "tt29927351",
    "title": "Nine Puzzles",
    "notion_name": "Nine Puzzle",
    "rating": 10
  },
  {
    "id": "tt20234568",
    "title": "Weak Hero Class 1",
    "notion_name": "Weak Hero Class",
    "rating": 10
  },
  {
    "id": "tt32361930",
    "title": "Good Boy",
    "notion_name": "Good boy",
    "rating": 8
  },
  {
    "id": "tt32409807",
    "title": "Genie, Make a Wish",
    "notion_name": "Genie Make a Wish",
    "rating": 9
  },
  {
    "id": "tt28036189",
    "title": "When I Fly Towards You",
    "notion_name": "When I fly towards you",
    "rating": 9
  },
  {
    "id": "tt37146661",
    "title": "Head Over Heels",
    "notion_name": "Head Over Heels",
    "rating": 8
  },
  {
    "id": "tt28076458",
    "title": "Hidden Love",
    "notion_name": "Hidden Love",
    "rating": 6
  },
  {
    "id": "tt38353551",
    "title": "Dynamite Kiss",
    "notion_name": "Beijo Explosivo",
    "rating": 6
  },
  {
    "id": "tt30293074",
    "title": "Can This Love Be Translated?",
    "notion_name": "Can this love be translate",
    "rating": 8
  },
  {
    "id": "tt34440854",
    "title": "The Wonderfools",
    "notion_name": "SuperTontos",
    "rating": 8
  },
  {
    "id": "tt33429144",
    "title": "No Tail to Tell",
    "notion_name": "De repente Humana",
    "rating": 7
  },
  {
    "id": "tt35051401",
    "title": "The East Palace",
    "notion_name": "A leste do Palácio",
    "rating": 10
  }
];
  const START_FROM = 45; // Começa do 45 para continuar de onde parou! (Mude para 1 se quiser rodar todos de novo)

  const banner = document.createElement("div");
  banner.style = "position:fixed;top:0;left:0;width:100%;z-index:999999;background:#f5c518;color:#000;padding:16px;font-size:18px;font-weight:bold;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.4);font-family:sans-serif;";
  document.body.appendChild(banner);

  console.log(`🎬 Continuando envio de notas do item ${START_FROM} até ${items.length} no IMDb...`);
  const sleep = (ms) => new Promise(r => setTimeout(r, ms));
  let ok = 0;

  for (let i = START_FROM - 1; i < items.length; i++) {
    const item = items[i];
    banner.innerText = `⏳ Atualizando IMDb: [${i+1}/${items.length}] ${item.notion_name} (Nota ${item.rating}/10) — NÃO mude de página!`;
    try {
      const res = await fetch("https://api.graphql.imdb.com/", {
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
      const data = await res.json();
      ok++;
      console.log(`✅ [${i+1}/${items.length}] Nota ${item.rating}/10 -> ${item.notion_name} (${item.title} - ${item.id})`);
      await sleep(600);
    } catch (err) {
      console.error(`❌ Erro em ${item.notion_name} (${item.id}):`, err);
    }
  }
  banner.style.background = "#16a34a";
  banner.style.color = "#fff";
  banner.innerText = `🎉 PRONTO! Todos os 98 Doramas foram avaliados na sua conta do IMDb! Já pode navegar normalmente!`;
  console.log(`🎉 Concluído! ${ok} doramas restantes avaliados na sua conta do IMDb!`);
})();
