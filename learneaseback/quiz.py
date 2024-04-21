import google.generativeai as genai
import json


def generate_quiz(transript):    
    genai.configure(api_key="AIzaSyCGQkTdQD38UawvKumJ2HLzk1y5pBqngJo")

    # Set up the model
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    convo = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["hii"]
    },
    {
        "role": "model",
        "parts": ["Hello! How can I help you today?"]
    },
    ])

    prompt = transript
    prompt += """

    Create a quiz of ten multiple choice questions from the prompt text with their answers reply only json object in following format:
    [
        {
            "question" : <Question Goes Here>,
            "options" : <List of 4 options, do not write ABCD or 1234 before options >,
            "answer" : <Correct answer as number from 1 to 4>
        }
    ]

    I only want json as reply, if you want to write anything then write it comment in json
    """

    convo.send_message(prompt)
    json_string = convo.last.text[8:-3]
    questions = json.loads(json_string)
    return questions