import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from prompts import linkedin_prompt

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

def generate_post(
        topic,
        industry,
        tone,
        length,
        audience,
        emoji):

    prompt = linkedin_prompt.format(
        topic=topic,
        industry=industry,
        tone=tone,
        length=length,
        audience=audience,
        emoji=emoji
    )

    response = llm.invoke(prompt)

    return response.content