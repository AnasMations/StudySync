import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import find_dotenv, load_dotenv
import streamlit as st

gen_type = [
    "questions and answers",
    "multiple choice questions",
    "explaination as if you are a teacher",
    "bullet points summary",
]

style = [
    "an educational Presentation slides",
    "a video",
    "a pdf",
    "a user question",
    "a text",
]

text = "Computer science and its part in geology"

def answer(gen_type: str, style:str, text:str)-> str:
    try:
        key = st.secrets["OPENAI_API_KEY"]
    except:
        try:
            _ = load_dotenv(find_dotenv())  # read local .env file
            key = os.environ["OPENAI_API_KEY"]
        except:
            return None
      
    chat = ChatOpenAI(temperature=0.2, model="gpt-3.5-turbo", openai_api_key=key, max_tokens=250)

    template_string = """"
    You are given material extracted from {style}, genrate {gen_type} from the text genrated from this material .
    text:{text} 
            
    """
    prompt_template = ChatPromptTemplate.from_template(template_string)

    message = prompt_template.format_messages(
        gen_type=gen_type, style=style, text=text
    )

    customer_response = chat(message)
    return customer_response.content
