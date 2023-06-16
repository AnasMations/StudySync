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


def GenerateSummary(input_type = 0, output_type = 0, input = None):

    response = None
    if input_type == 0: # Slides
        response = answer(style=styles[input_type], gen_type=gen_types[output_type], text=input)

    elif input_type == 1: # PDF
        response = answer(style=styles[input_type], gen_type=gen_types[output_type], text=input)
    
    elif input_type == 2: # video transcript
        # Change user input from video link to transcript
        transcript, no_of_words = generate_transcript(input)
        input = transcript # change the input to the video transcript
        response = answer(style=styles[input_type], gen_type=gen_types[output_type], text=input)

    elif input_type == 3: # user question
        response = answer(style=styles[input_type], gen_type=gen_types[output_type], text=input)

    return response

# style_choice = styles[2]

# gen_type_choice = gen_types[2]

# response = None

# if style_choice == styles[0] or style_choice == styles[1]:
#     pass


# elif style_choice == styles[2]:
    
#     video_link = "https://www.youtube.com/watch?v=N2PpRnFqnqY" # an example link
#     transcript, no_of_words = generate_transcript(video_link)
#     response = answer(gen_type=gen_type_choice, style=style_choice, text=transcript)
#     print(response)


# elif style_choice == styles[3]:
#     user_input = "Computer science and its part in geology"
#     response = answer(gen_type=gen_type_choice, style=style_choice, text=user_input)


