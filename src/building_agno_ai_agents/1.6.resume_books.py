from pathlib import Path
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openrouter import OpenRouter

from dotenv import load_dotenv
import httpx
load_dotenv()

db_path = Path(__file__).resolve().parent / "tmp" / "books.db"
db_path.parent.mkdir(exist_ok=True)

db = SqliteDb(db_file=str(db_path))

def search_book(title: str) -> dict:
    """Busca metadados de um livro na Open Library.
    Args:
        title: Título do livro.
    Returns:
        Título, autores, ano e assuntos, ou um aviso se não achar.
    """
    response = httpx.get(
        "https://openlibrary.org/search.json",
        params={"title": title, "limit": 1},
        timeout=20,
    )
    response.raise_for_status()
    docs = response.json().get("docs") or []
    if not docs:
        return {"found": False, "message": f"Nenhum livro encontrado para '{title}'."}
    doc = docs[0]
    return {
        "found": True,
        "title": doc.get("title"),
        "authors": doc.get("author_name", []),
        "first_publish_year": doc.get("first_publish_year"),
        "subjects": (doc.get("subject") or [])[:8],
    }

agent = Agent(
    model=OpenRouter(id="openai/gpt-5-mini"),
    tools=[search_book],
    description="Você é um agente de livros. Você pode resumir livros e responder perguntas sobre eles.",
    instructions=[
        "Antes de resumir, use search_book para confirmar título, autor e temas.",
        "Baseie o resumo nesses metadados e no que o cliente já pediu.",
        "Lembre-se de cada cliente, suas informações e preferências.",
        "Responda em português brasileiro.",
    ],
    db=db,
    add_history_to_context=True,
    num_history_runs=3,
    update_memory_on_run=True,
    add_memories_to_context=True,
)

user_id = "gabriel"

agent.print_response(
    "Meu nome é Gabriel e prefiro resumos em tópicos curtos.",
    session_id="books_onboarding",
    user_id=user_id,
    stream=True,
)

agent.print_response(
    "Qual formato de resumo eu prefiro?",
    session_id="books_preferences",
    user_id=user_id,
    stream=True,
)

agent.print_response(
    "Resuma o livro 'Arquitetura Limpa: Codificação, Refatoração e Design de Código de Alto Desempenho'.",
    session_id="books_summary",
    user_id=user_id,
    stream=True,
)

print("\nMemories gravadas:")
for memory in agent.get_user_memories(user_id=user_id) or []:
    print(f"- {memory.memory_id}: {memory.memory}")