from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openrouter import OpenRouter
from agno.os import AgentOS

from dotenv import load_dotenv
load_dotenv()

db = SqliteDb(db_file="agno.db")

agent = Agent(
    name="Agno Assist",
    model=OpenRouter(id="openai/gpt-5-mini"),
    db=db,
)

agent_os = AgentOS(agents=[agent], db=db)
app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="agno_assist:app", reload=True)