from youtube_transcript_api import YouTubeTranscriptApi


def generate_transcript(link: str):
    id=link[link.rfind("v=")+2:]
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





