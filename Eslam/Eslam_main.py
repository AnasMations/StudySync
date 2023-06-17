from summary import answer
from youtube import generate_transcript

# Input Type
styles = [
    "an educational Presentation slides",
    "a PDF or Word document",
    "a video transcript",
    "a user question",
]

# Output Type
gen_types = [
    "questions and answers",
    "a multiple choice questions",
    "a detailed and simple explaination of the concepts and ideas",
    "a bullet points summary",
]


def GenerateSummary(input_type = 0, output_type = 0, input = None, tokens = 250):

    response = None
    if input_type == 0: # Slides
        response = answer(style=styles[input_type], gen_type=gen_types[output_type], text=input, tokens=tokens)

    elif input_type == 1: # PDF
        response = answer(style=styles[input_type], gen_type=gen_types[output_type], text=input, tokens=tokens)
    
    elif input_type == 2: # video transcript
        # Change user input from video link to transcript
        transcript, no_of_words = generate_transcript(input)
        input = transcript # change the input to the video transcript
        response = answer(style=styles[input_type], gen_type=gen_types[output_type], text=input, tokens=tokens)

    elif input_type == 3: # user question
        response = answer(style=styles[input_type], gen_type=gen_types[output_type], text=input, tokens=tokens)

    return response


    
#video_link = "https://www.youtube.com/watch?v=N2PpRnFqnqY" # an example link
#transcript, no_of_words = generate_transcript(video_link)
#response = answer(gen_type=gen_type_choice, style=style_choice, text=transcript)
#print(response)




