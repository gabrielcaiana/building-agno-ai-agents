from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.youtube import YouTubeTools

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    model=OpenRouter(id="openai/gpt-5-mini"),
    tools=[YouTubeTools()],
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
)

agent.print_response("Summarize this video https://www.youtube.com/watch?v=Iv9dewmcFbs&t", markdown=True)