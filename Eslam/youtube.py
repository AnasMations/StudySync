from youtube_transcript_api import YouTubeTranscriptApi
import os

import openai
from dotenv import find_dotenv, load_dotenv


def generate_transcript(id):
    transcript = YouTubeTranscriptApi.get_transcript(id)
    script = ""

    for text in transcript:
        t = text["text"]
        if t != "[Music]":
            script += t + " "

    return script, len(script.split())


id = "ltQ9pbFukUo"
transcript, no_of_words = generate_transcript(id)


_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ["OPENAI_API_KEY"]


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model, messages=messages, temperature=0, max_tokens=250
    )
    return response.choices[0].message["content"]

print("StudySync")

ans = get_completion(
    f"""
               
               Genretate a summary of the video transcript in the format of a 5 multiple choice questions.
               transcript: {transcript}
               """
)

print(ans)
