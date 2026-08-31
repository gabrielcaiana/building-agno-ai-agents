# Building Agno AI Agents

Projeto de estudos para construir agentes de IA com a biblioteca `agno`, explorando modelos, ferramentas externas e exemplos práticos de automação com Python.

## Objetivo

Este repositório reúne scripts simples para aprender a montar agentes com:

- chamadas diretas a modelos LLM;
- busca na web com ferramentas integradas;
- acesso a dados financeiros;
- leitura de transcrições de vídeos no YouTube;
- criação de ferramentas customizadas em Python.

O foco aqui é didático: cada arquivo em `src/building_agno_ai_agents/` demonstra um caso de uso isolado.

## Estrutura do projeto

```text
.
├── pyproject.toml
├── .env.sample
├── src/
│   └── building_agno_ai_agents/
│       ├── 0.llm_call.py
│       ├── 1.1.researcher.py
│       ├── 1.2.hacker_news.py
│       ├── 1.3.finance.py
│       ├── 1.4.own_tools.py
│       ├── 1.5.youtube_assistent.py
│       └── __init__.py
└── uv.lock
```

## Requisitos

- Python 3.11 ou superior
- `uv` instalado
- chaves de API válidas para os provedores usados nos exemplos

## Instalação

Clone o projeto e instale as dependências:

```bash
uv sync
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

## Como executar

Os scripts podem ser executados individualmente com `uv run`:

```bash
uv run python src/building_agno_ai_agents/0.llm_call.py
uv run python src/building_agno_ai_agents/1.1.researcher.py
uv run python src/building_agno_ai_agents/1.2.hacker_news.py
uv run python src/building_agno_ai_agents/1.3.finance.py
uv run python src/building_agno_ai_agents/1.4.own_tools.py
uv run python src/building_agno_ai_agents/1.5.youtube_assistent.py
```

## Exemplos disponíveis

### `0.llm_call.py`
Faz uma chamada direta a um modelo da Groq usando mensagens explícitas.

### `1.1.researcher.py`
Cria um agente pesquisador com `TavilyTools`, saída em Markdown e modo de debug.

### `1.2.hacker_news.py`
Consulta tópicos em alta no Hacker News com foco em IA, startups e produtos.

### `1.3.finance.py`
Usa `YFinanceTools` para buscar preço de ações e recomendações de analistas.

### `1.4.own_tools.py`
Mostra como registrar uma função Python própria como ferramenta do agente.

### `1.5.youtube_assistent.py`
Obtém legendas de vídeos do YouTube e responde perguntas com base no conteúdo.

## Observações

- Não versione o arquivo `.env` com credenciais reais.
- Alguns exemplos dependem de acesso à internet e de APIs de terceiros.
- O projeto ainda não possui uma suíte formal de testes; a validação atual é feita executando os scripts individualmente.
