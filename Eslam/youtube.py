from typing import Tuple
from youtube_transcript_api import YouTubeTranscriptApi


def generate_transcript(id: str) -> Tuple[str, int]:
    try:
        transcript = YouTubeTranscriptApi.get_transcript(id)
        script = ""
        for text in transcript:
            t = text["text"]
            if t != "[Music]":
                script += t + " "
        return script, len(script.split())
    except:
        return None , None


id = "N2PpRnFqnqY"
transcript, no_of_words = generate_transcript(id)

print(transcript)
