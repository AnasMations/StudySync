import os
import openai
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ["OPENAI_API_KEY"]


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model, messages=messages, temperature=0, max_tokens=300 , n=1
    )
    return response.choices[0].message["content"]




ans = get_completion(
    f"""
               
               Genretate a summary of the video transcript in the format of a 5 multiple choice questions.
               transcript: {transcript}
               """
)

print(ans)