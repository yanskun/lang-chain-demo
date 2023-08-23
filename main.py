from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")

OPENAI_API_KEY = config["OPENAI_API_KEY"]

llm = OpenAI(openai_api_key=OPENAI_API_KEY)
chat_model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

llm.predict("hi!")
chat_model.predict("hi!")
