import os
import openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file
key = os.environ["OPENAI_API_KEY"]


chat = ChatOpenAI(temperature=0.2, model="gpt-3.5-turbo", openai_api_key=key)

template_string = """"
You are given material in the format of {style}, genrate a {gen_type} from the text genrated from this material .
text:{text} 
"""


gen_type = [
    "questions and answers",
    "multiple choice questions",
    "explaination as if you are a teacher",
    "bullet points summary",
]
style = [
    "an educational Presentation slides",
    "an educational Presentation slides",
    "a pdf",
    "user question",
]
text = "Computer science and its part in geology"


prompt_template = ChatPromptTemplate.from_template(template_string)

customer_messages = prompt_template.format_messages(
    gen_type=gen_type[-1], style=style[-1], text=text
)


customer_response = chat(customer_messages)
print(customer_response.content)
