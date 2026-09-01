from pathlib import Path
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openrouter import OpenRouter

from dotenv import load_dotenv
load_dotenv()

db_path = Path(__file__).resolve().parent / "tmp" / "books.db"
db_path.parent.mkdir(exist_ok=True)

db = SqliteDb(db_file=str(db_path))

agent = Agent(
    model=OpenRouter(id="openai/gpt-5-mini"),
    tools=[],
    description="Você é um agente de livros. Você pode resumir livros e responder perguntas sobre eles.	",
    instructions=[
        "Você é um agente de livros. Você pode resumir livros e responder perguntas sobre eles.",
        "Lembre-se de cada cliente, suas informações e preferências.",
        "Responda em português brasileiro.",
    ],
    db=db,
    add_history_to_context=True,
    num_history_runs=10,
    update_memory_on_run=True,
    add_memories_to_context=True,
)

agent.print_response("Resuma o livro 'The Product-Minded Engineer: Building Impactful Software for Your Users' e responda perguntas sobre ele.", stream=True)