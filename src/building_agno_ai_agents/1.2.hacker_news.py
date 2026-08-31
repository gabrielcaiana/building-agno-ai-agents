from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.hackernews import HackerNewsTools

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    model=Groq(id="openai/gpt-oss-120b"),
    tools=[HackerNewsTools()],
    markdown=True
)

agent.print_response("Escreva sobre os temas em alta sobre AI, startups e produtos", stream=True)
