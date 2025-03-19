# Language Translation
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import uvicorn
from langserve import add_routes
from fastapi import FastAPI
load_dotenv()
groq_key = os.getenv("GROQ")

groq_model = ChatGroq(
    model="llama3-70b-8192",
    groq_api_key=groq_key)

parser = StrOutputParser()
system_template = "Translate the following into {language}:"
prompt_tamplate = ChatPromptTemplate.from_messages(
    [
        (
            "system", system_template
        ),
        (
            "user", "{text}"
        )
    ]
)
chain = prompt_tamplate | groq_model | parser
app = FastAPI(
    title="Translator",
    version="1.0",
    description="A simple API server using Langchain's Runnable interfaces"
)
add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5001)