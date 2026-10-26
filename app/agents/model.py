from langchain_groq import ChatGroq
from app.config import settings

def get_langchain_llm() -> ChatGroq:
    
    """ Return the ChatGroq chat model"""

    return ChatGroq(
        model=settings.GROQ_MODEL,
        temperature=0
    )

llm = get_langchain_llm()
