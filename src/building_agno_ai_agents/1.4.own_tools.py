from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools

from dotenv import load_dotenv
load_dotenv()

def celsius_to_fh(temperature_celsius: float) -> float:
    """
    Converts Celsius to Fahrenheit

    Args:
    temperature_celsius (float): Celsius to Fahrenheit

    Returns:
        float: Fahrenheit to Celsius
    """
    return (temperature_celsius * 9/5) + 32

agent = Agent(
    model=Groq(id="openai/gpt-oss-120b"),
    tools=[
        TavilyTools(),
        celsius_to_fh
    ],
    markdown=True,
    debug_mode=True
)

agent.print_response("Qual a temperatura hoje em Sao Paulo")
