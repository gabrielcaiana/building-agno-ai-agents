import os
from pathlib import Path
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openrouter import OpenRouter
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.knowledge.chunking.recursive import RecursiveChunking
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.vectordb.chroma import ChromaDb

from dotenv import load_dotenv
load_dotenv()

base_dir = Path(__file__).resolve().parent
project_root = base_dir.parent.parent
books_dir = project_root / "books"

db_path = base_dir / "tmp" / "microfrontend_learning.db"
chroma_path = base_dir / "tmp" / "chromadb"
db_path.parent.mkdir(exist_ok=True)
chroma_path.mkdir(exist_ok=True)

db = SqliteDb(db_file=str(db_path))

knowledge = Knowledge(
    name="microfrontend_learning",
    description="Livro de aprendizado de microfrontends.",
    vector_db=ChromaDb(
        collection="microfrontend_learning",
        path=str(chroma_path),
        persistent_client=True,
        embedder=OpenAIEmbedder(
            id="text-embedding-3-small",
            api_key=os.getenv("OPENAI_API_KEY"),
        ),
    ),
)

pdf_reader = PDFReader(
    chunking_strategy=RecursiveChunking(
        chunk_size=2000,
        overlap=200,
    ),
)

ebooks = sorted(books_dir.glob("*.pdf"))

if not ebooks:
    raise FileNotFoundError(f"Nenhum PDF encontrado em {books_dir}")

knowledge.insert(
    path=str(books_dir),
    reader=pdf_reader,
    metadata={"doc_type": "ebook", "topic": "microfrontends"},
    include=["*.pdf"],
    skip_if_exists=True,
)

agent = Agent(
    model=OpenRouter(id="openai/gpt-5-mini"),
    knowledge=knowledge,
    search_knowledge=True,
    description="Você é um assistente de aprendizado de microfrontends. Você pode responder perguntas sobre microfrontends a partir de um livro de aprendizado.",
    instructions=[
        "Use o knowledge (RAG) para responder as perguntas com base no livro indexado.",
        "Responda em português brasileiro.",
        "Seja didático e explique de forma clara e objetiva.",
        "Se a informação não estiver no livro, diga isso explicitamente.",
    ],
    db=db,
    add_history_to_context=True,
    num_history_runs=3,
    update_memory_on_run=True,
    add_memories_to_context=True,
)

user_id = "gabriel"
session_id = "microfrontend_learning"

agent.print_response(
    "Quais capítulos o livro tem?",
    session_id=session_id,
    user_id=user_id,
    stream=True,
)

agent.print_response(
    "Resuma o capítulo Client-Side Rendering Micro-Frontends (Micro‑Frontends com Client‑Side Rendering)",
    session_id=session_id,
    user_id=user_id,
    stream=True,
)
