# Building Agno AI Agents

Projeto de estudos para construir agentes de IA com a biblioteca `agno`, explorando modelos, ferramentas externas, memória persistente, RAG com banco vetorial, AgentOS e uma interface web para conversar com agentes.

## Objetivo

Este repositório reúne scripts simples para aprender a montar agentes com:

- chamadas diretas a modelos LLM;
- busca na web com ferramentas integradas;
- consulta a tópicos do Hacker News;
- acesso a dados financeiros (YFinance);
- leitura de transcrições de vídeos no YouTube;
- criação de ferramentas customizadas em Python;
- resumo de livros com consulta à Open Library;
- RAG (Retrieval-Augmented Generation) com PDFs e ChromaDB;
- persistência com SQLite e memória de usuário entre sessões;
- exposição de agentes via AgentOS;
- uso de uma UI em Next.js para interagir com o AgentOS.

O foco principal é didático: cada arquivo em `src/building_agno_ai_agents/` demonstra um caso de uso isolado, enquanto `agent-ui/` contém uma interface web separada para conversar com agentes servidos pelo AgentOS.

## Estrutura do projeto

```text
.
├── .env.sample
├── agent-ui/
│   ├── package.json
│   ├── src/
│   └── README.md
├── books/
│   └── *.pdf                          # livros usados no exemplo de RAG (microfrontends)
├── docs/
│   ├── PETR/*.pdf                     # relatórios da Petrobras usados no exemplo financeiro com RAG
│   └── VALE/*.pdf                     # transcrições da Vale usadas no exemplo financeiro com RAG
├── images/
│   └── context_enginneering.png
├── pyproject.toml
├── src/
│   ├── main.py
│   └── building_agno_ai_agents/
│       ├── 0.llm_call.py
│       ├── 1.1.researcher.py
│       ├── 1.2.hacker_news.py
│       ├── 1.3.finance.py
│       ├── 1.4.own_tools.py
│       ├── 1.5.youtube_assistent.py
│       ├── 1.6.resume_books.py
│       ├── 1.7.assistent_microfrontend_learning.py
│       ├── 1.8.finance_with_rag.py
│       ├── agno_assist.py
│       ├── tmp/                       # bancos SQLite e coleções ChromaDB gerados em runtime
│       └── __init__.py
└── uv.lock
```

## Requisitos

- Python 3.11 ou superior
- `uv` instalado
- Node.js e `pnpm` para rodar a UI em `agent-ui/`
- chaves de API válidas para os provedores usados nos exemplos (Groq, OpenAI, Tavily, OpenRouter)

## Instalação

Instale as dependências Python:

```bash
uv sync
```

Para usar a interface web, instale também as dependências do frontend:

```bash
cd agent-ui
pnpm install
```

## Configuração de ambiente

Copie o arquivo de exemplo e preencha suas credenciais:

```bash
cp .env.sample .env
```

Variáveis esperadas atualmente:

```env
GROQ_API_KEY=sua_chave_groq
OPENAI_API_KEY=sua_chave_openai
TAVILY_API_KEY=sua_chave_tavily
OPENROUTER_API_KEY=sua_chave_openrouter
```

A `OPENAI_API_KEY` também é usada para gerar embeddings (`OpenAIEmbedder`, modelo `text-embedding-3-small`) nos exemplos de RAG (`1.7` e `1.8`).

## Como Executar os Exemplos Python

Os scripts podem ser executados individualmente com `uv run`:

```bash
uv run python src/building_agno_ai_agents/0.llm_call.py
uv run python src/building_agno_ai_agents/1.1.researcher.py
uv run python src/building_agno_ai_agents/1.2.hacker_news.py
uv run python src/building_agno_ai_agents/1.3.finance.py
uv run python src/building_agno_ai_agents/1.4.own_tools.py
uv run python src/building_agno_ai_agents/1.5.youtube_assistent.py
uv run python src/building_agno_ai_agents/1.6.resume_books.py
uv run python src/building_agno_ai_agents/1.7.assistent_microfrontend_learning.py
uv run python src/building_agno_ai_agents/1.8.finance_with_rag.py
```

Alguns scripts fazem chamadas a APIs externas ou acessam a internet. Antes de executar, confirme se as chaves correspondentes estão configuradas no `.env`.

Os exemplos `1.6`, `1.7` e `1.8` também gravam índices vetoriais em `src/building_agno_ai_agents/tmp/chromadb/` na primeira execução; execuções seguintes reaproveitam o índice (`skip_if_exists=True` em `1.7`).

## Como Rodar o AgentOS

O arquivo `src/building_agno_ai_agents/agno_assist.py` cria um agente chamado `Agno Assist`, usa `OpenRouter(id="openai/gpt-5-mini")`, persiste dados em SQLite e expõe uma aplicação AgentOS.

Execute com:

```bash
uv run python src/building_agno_ai_agents/agno_assist.py
```

Por padrão, o AgentOS fica disponível para a UI local do Agno. A interface em `agent-ui/` espera se conectar a `http://localhost:7777`.

## Como Rodar a UI

Com o AgentOS em execução, abra outro terminal e rode:

```bash
cd agent-ui
pnpm dev
```

Acesse `http://localhost:3000` no navegador. Se necessário, ajuste o endpoint da UI para apontar para o AgentOS local.

## Exemplos Disponíveis

### `0.llm_call.py`
Faz uma chamada direta a um modelo da Groq usando `Groq(id="openai/gpt-oss-120b")` e mensagens explícitas.

### `1.1.researcher.py`
Cria um agente pesquisador com `TavilyTools`, saída em Markdown e modo de debug.

### `1.2.hacker_news.py`
Consulta tópicos em alta no Hacker News com foco em IA, startups e produtos, usando `HackerNewsTools`.

### `1.3.finance.py`
Cria um agente financeiro com `OpenAIResponses`, `YFinanceTools(all=True)` e persistência em SQLite.

Estado atual do exemplo:

- carrega variáveis com `python-dotenv`;
- cria o banco em `src/building_agno_ai_agents/tmp/data.db`;
- habilita histórico de conversa com `add_history_to_context=True`;
- limita o contexto a `num_history_runs=3`;
- ativa memória com `update_memory_on_run=True` e `add_memories_to_context=True`;
- usa `session_id` e `user_id` para testar preferências do usuário entre sessões;
- pergunta cotações da Petrobras e da Vale usando ferramentas financeiras.

### `1.4.own_tools.py`
Mostra como registrar uma função Python própria, `celsius_to_fh`, como ferramenta do agente, junto com `TavilyTools`.

### `1.5.youtube_assistent.py`
Obtém legendas de vídeos do YouTube com `YouTubeTools` e responde perguntas com base no conteúdo usando OpenRouter.

### `1.6.resume_books.py`
Agente de livros que usa uma ferramenta própria (`search_book`) para consultar metadados na Open Library (título, autores, ano, assuntos) antes de gerar resumos. Persiste histórico e memória do usuário em `tmp/books.db` e responde em português.

### `1.7.assistent_microfrontend_learning.py`
Assistente de estudo baseado em RAG sobre o livro de microfrontends em `books/`. Usa `Knowledge` + `ChromaDb` (com `OpenAIEmbedder`) para indexar os PDFs via `PDFReader`/`RecursiveChunking`, e responde perguntas sobre o conteúdo com `search_knowledge=True`. Indexação e memória são persistidas em `tmp/microfrontend_learning.db` e `tmp/chromadb/`.

### `1.8.finance_with_rag.py`
Combina análise financeira (`YFinanceTools`) com RAG sobre relatórios em PDF das empresas Petrobras (`docs/PETR/`) e Vale (`docs/VALE/`), indexados em ChromaDB. Permite responder tanto a cotações em tempo real quanto a perguntas sobre o conteúdo dos relatórios (ex.: lucro líquido, CAPEX), com memória agentic habilitada (`enable_agentic_memory=True`).

### `agno_assist.py`
Define um agente básico com `AgentOS`, `OpenRouter` e `SqliteDb`, expondo uma aplicação para consumo pela UI em `agent-ui/`.

## Observações

- Não versione o arquivo `.env` com credenciais reais.
- Alguns exemplos dependem de acesso à internet e de APIs de terceiros.
- O exemplo financeiro (`1.3`) grava estado em `src/building_agno_ai_agents/tmp/data.db`.
- Os exemplos de RAG (`1.7`, `1.8`) gravam bancos SQLite e coleções ChromaDB em `src/building_agno_ai_agents/tmp/`.
- O `agno_assist.py` usa `agno.db` como banco SQLite local quando executado.
- Os PDFs em `books/` e `docs/` são material de apoio usado apenas para alimentar os exemplos de RAG.
- O projeto ainda não possui uma suíte formal de testes; a validação atual é feita executando os scripts individualmente e, quando necessário, com uma checagem de sintaxe.

## Validação

Para uma checagem rápida de sintaxe nos arquivos Python:

```bash
uv run python -m compileall src
```
</content>
