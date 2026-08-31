from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    model=OpenAIChat(id="gpt-5.4-mini"),
    tools=[YFinanceTools(all=True)],
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
)
agent.print_response("Share the NVDA stock price and analyst recommendations", markdown=True)

