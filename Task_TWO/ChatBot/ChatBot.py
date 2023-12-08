import spacy
from DataBase import data

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# This is will help your that how they can use this
print("Welcome, How can i assest you? \n Note: \n If you want to qute please type q and enter.")


loop = 0  # variable for while loop

# Start while loop
while loop != 1:

    # Input from user
    input_text = input("User: ").lower()

    # Add question mark in user input
    data_with_question_mark = f"{input_text}?"

    # Process the input text with spaCy
    doc = nlp(input_text)

    # Response: Check if input_text is in the database
    if input_text == "q":
        break

    # Response: Check if input_text is in the database
    elif input_text in data:
        response = data[input_text]
        print("Bot:", response)

    # Response: Check if input_text is in the database with ?
    elif data_with_question_mark in data:
        response = data[data_with_question_mark]
        print("Bot:", response)

    # If answer of the question is not available
    else:
        response = "Sorry I don't known answer of that question."
        print("Bot:", response)
