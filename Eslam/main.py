from youtube import generate_transcript
from summary import answer


styles = [
    "an educational Presentation slides",
    "a PDF or word",
    "a video transcript",
    "a user question",
]

gen_types = [
    "questions and answers",
    "a multiple choice questions",
    "a detailed and simple explaination of the concepts and ideas",
    "a bullet points summary",
]

style_choice = styles[2]

gen_type_choice = gen_types[2]


if style_choice == styles[0] or style_choice == styles[1]:
    pass


elif style_choice == styles[2]:
    
    video_link = "https://www.youtube.com/watch?v=N2PpRnFqnqY" # an example link
    transcript, no_of_words = generate_transcript(video_link)
    print(answer(gen_type=gen_type_choice, style=style_choice, text=transcript))


elif style_choice == styles[3]:
    user_input = "Computer science and its part in geology"
    answer(gen_type=gen_type_choice, style=style_choice, text=user_input)



