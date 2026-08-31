from agno.models.groq import Groq
from agno.models.message import Message

# ===================
# Carregando as Envs
# ===================
from dotenv import load_dotenv

load_dotenv()

# ===================================
# Selecionando o Modelo de Linguagem
# ===================================
model = Groq(id="openai/gpt-oss-120b")

# ================================
# Inserindo a mensagem do usuário
# ================================
user_message = Message(role="user", content="Olá, meu nome é Gabriel Caiana.")

# =======================
# Mensagem do Assistente
# =======================
assistant_message = Message(role="assistant", content="")

# ==========
# Invocar
# ==========
response = model.invoke(
    messages=[user_message],
    assistant_message=assistant_message)

print(response.content)