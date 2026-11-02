# 🎬 IMDb AI Automator — Filmes, Séries, Doramas e Animes

> Pipeline automatizado em Python que utiliza **IA Generativa (Google Gemini API com Structured Outputs)** e **engenharia reversa da API GraphQL do IMDb** para transformar qualquer lista desestruturada de obras (Notion, WhatsApp, Notas) em avaliações em lote (*bulk rating*) e listas personalizadas oficiais, **sem necessidade de APIs pagas (OMDb/TMDB) e sem bloqueios de Captcha/Cloudflare**.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Google Gemini API](https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-orange.svg?logo=google&logoColor=white)](https://aistudio.google.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI%20Dashboard-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![IMDb](https://img.shields.io/badge/IMDb-GraphQL%20Integration-F5C518.svg?logo=imdb&logoColor=black)](https://www.imdb.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 💡 O Problema que Resolve

Quem consome muitos filmes, séries, doramas (K-dramas/C-dramas) e animes costuma manter registros descentralizados (tabelas no Notion, anotações de celular ou conversas). Migrar manualmente centenas de itens para o IMDb exige:
1. Buscar título por título na barra de pesquisa;
2. Descobrir a versão exata do ano de lançamento;
3. Clicar nas estrelas de avaliação (1 a 10) e adicionar à Watchlist.

Para centenas de itens, esse processo manual leva dias. Além disso, automações convencionais via Selenium/Playwright falham rapidamente por proteções de login, 2FA e Captcha do IMDb.

---

## 🛠️ Arquitetura da Solução

O **IMDb AI Automator** resolve o problema através de 3 pilares de engenharia:

```
[ Texto Bagunçado / Notion / WhatsApp ]
                 │
                 ▼
     [ Google Gemini 2.5 Flash ]
     (Pydantic Schema: MediaItem)
                 │
                 ├── Extrai Título Canônico / Oficial
                 ├── Identifica Ano, Categoria e Status
                 └── Normaliza Notas de 1 a 10
                 │
                 ▼
     [ IMDb Internal Suggestions Engine ]
     (Busca heurística sem chaves de API pagas)
                 │
                 ▼
     [ Resolvedor de IDs 'ttXXXXXXX' ]
                 │
        ┌────────┴────────┐
        ▼                 ▼
[ Export CSV Oficial ]   [ Script GraphQL de 1-Clique ]
(Importação de Listas)   (Injeção autenticada no Console)
```

1. **Parser Inteligente com Gemini API (`google.genai` + Pydantic)**:
   - Extrai nomes canônicos em inglês/original mesmo a partir de títulos traduzidos, apelidos ou nomes parciais em português.
   - Força tipagem e esquema estrito (`MediaListResponse`) com `response_schema`.
2. **Motor de Descoberta de IDs (`ttXXXXXXX`) Sem Custos**:
   - Consulta o endpoint de autocompletar do ecossistema IMDb, filtrando por ano de lançamento e categoria sem consumir cotas pagas de OMDb ou TMDB.
3. **Injeção de GraphQL no Navegador (Client-Side Batch Mutation)**:
   - Gera um snippet assíncrono em JavaScript para execução no Console do DevTools com a sessão do usuário já autenticada.
   - Executa a mutação GraphQL oficial do IMDb (`rateTitle(input: { rating: $rating, titleId: $titleId })`), com *banner* visual de progresso e *throttle* anti-rate-limit.

---

## 🖥️ Como Executar

### 1. Clonar e Instalar Dependências

```bash
git clone https://github.com/Geovana28/imdb-ai-automator.git
cd imdb-ai-automator

# Criar ambiente virtual
python -m venv .venv
# Ativar no Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# Ou no Linux/macOS:
# source .venv/bin/activate

pip install -r requirements.txt
```

### 2. Configurar a Chave da API Gemini

Copie o `.env.example` para `.env` e insira sua chave gratuita obtida no [Google AI Studio](https://aistudio.google.com/):

```env
GEMINI_API_KEY=sua_chave_aqui
```

### 3. Executar o Painel Interativo (Streamlit)

```bash
streamlit run app.py
```

### 4. Ou usar via CLI (Linha de Comando)

```bash
# Processamento inteligente com Gemini:
python cli.py -i minha_lista.txt -o imdb_pronto.csv

# Modo Direto (sem necessidade de chave de IA):
python cli.py -i minha_lista.txt -o imdb_pronto.csv --sem-ia
```

---

## 📊 Caso Real de Teste: 98 Doramas do Notion

A ferramenta foi validada migrando **98 Doramas catalogados no Notion** para o perfil do IMDb:
- Extração de nomes em português e coreano -> Mapeamento de 100% dos IDs `tt` correspondentes.
- Aplicação das 98 avaliações individuais via GraphQL em menos de 2 minutos.

---

## 📄 Licença

Distribuído sob a licença MIT. Consulte `LICENSE` para obter mais detalhes.
