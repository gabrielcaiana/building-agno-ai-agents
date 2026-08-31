"""
Exemplo de um agente pesquisador com Agno.

Este script cria um Agent capaz de responder perguntas usando:
- um modelo LLM hospedado pela Groq;
- uma ferramenta de busca na web via Tavily;
- saida em Markdown;
- modo de debug para estudar o que acontece durante a execucao.

Antes de executar, garanta que o arquivo .env tenha as chaves necessarias,
por exemplo GROQ_API_KEY e TAVILY_API_KEY.
"""

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools

from dotenv import load_dotenv

# Carrega variaveis de ambiente definidas no arquivo .env.
# Isso evita deixar chaves de API diretamente no codigo.
load_dotenv()

agent = Agent(
    # Define qual modelo sera usado pelo agente.
    # Neste caso, a Groq executa o modelo openai/gpt-oss-120b.
    model=Groq(id="openai/gpt-oss-120b"),

    # Adiciona a Tavily como ferramenta externa.
    # Com ela, o agente pode pesquisar informacoes atualizadas na web
    # antes de formular a resposta.
    tools=[TavilyTools()],

    # Faz a resposta ser formatada em Markdown.
    # Isso melhora listas, links, titulos e outros elementos textuais.
    markdown=True,

    # Exibe informacoes internas da execucao.
    # E util para estudar chamadas ao modelo, ferramentas usadas e fluxo geral.
    debug_mode=True
)

# Envia uma pergunta ao agente e imprime a resposta no terminal.
agent.print_response("Quem e o Gabriel Caiana")
