from pathlib import Path

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIResponses
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

db_path = Path(__file__).resolve().parent / "tmp" / "data.db"
db_path.parent.mkdir(exist_ok=True)

db = SqliteDb(db_file=str(db_path))

agent = Agent(
    model=OpenAIResponses(id="gpt-5.6-luna"),
    db=db,
    tools=[YFinanceTools(all=True)],
    instructions=[
        "Você é um analista financeiro. Lembre-se de cada cliente, suas informações e preferências."
    ],
    add_history_to_context=True,
    num_history_runs=3,
    update_memory_on_run=True,
    add_memories_to_context=True,
)

agent.print_response(
    "Meu nome é Gabriel e prefiro análises financeiras em tabela.",
    session_id="finance_session_1",
    user_id="gabriel",
)

agent.print_response(
    "Qual formato de resposta eu prefiro?",
    session_id="finance_session_2",
    user_id="gabriel",
)

agent.print_response(
    "Qual a cotação da Petrobrás?",
    session_id="finance_session_3",
    user_id="gabriel",
)

agent.print_response(
    "Qual a cotação da Vale?",
    session_id="finance_session_4",
    user_id="gabriel",
)

agent.print_response(
    "Qual o formato de resposta que eu gosto?",
    session_id="finance_session_6",
    user_id="gabriel",
)

