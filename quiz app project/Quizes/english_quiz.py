import tkinter as tk
import random
import customtkinter as ctk

# Define questions and answers in a dictionary

questions = {
    "What is the past tense of 'run'?": "Ran",
    "What is the synonym of 'happy'?": "Joyful",
    "What is the antonym of 'strong'?": "Weak",
    "What is the plural form of 'child'?": "Children",
    "What is the adjective in the sentence 'The sky is blue'?": "Blue",
    "What is the meaning of the idiom 'break the ice'?": "To start a conversation in a social setting",
    "What is the main verb in the sentence 'She is running fast'?": "Running",
    "What is the figure of speech in 'The stars danced in the sky'?": "Personification",
    "What is the correct article for the sentence: 'I saw ___ elephant'?": "An",
    "What is the opposite of 'expand'?": "Contract"
}

# Function to pick a random question from the dictionary
def rand_question():
    question = random.choice(list(questions.keys()))
    return question, questions[question]

# Function to run the math quiz
def english_quiz(root):
    points = 0
    question_index = 0  # Keeps track of which question is being shown
    try:
        
        # Function to show the next question
        def show_next_question():
            question_were = []
            nonlocal points, question_index  # Ensure outer variables are accessible

            # Pick the next question
            question, correct_answer = rand_question()
            while question in question_were:
                question, correct_answer = rand_question
            question_were.append(question)

            # Create question label
            label_question = ctk.CTkLabel(root, text=question, font=("Arial", 20), text_color="black")
            label_question.place(relx=0.5, rely=0.1, anchor='n')

            # Create input field for the user to enter their answer
            math_question_entry = ctk.CTkEntry(root, placeholder_text="Enter your answer...")
            math_question_entry.place(relx=0.5, rely=0.2, anchor='n')

            # Function to check the answer when the user submits it
            def check_answer():
                nonlocal points, question_index  # Declare these as nonlocal
                user_answer = math_question_entry.get().strip()  # Get user's answer from the entry widget
                if user_answer == correct_answer:  # Compare the user's answer with the correct answer
                    points += 1

                # Destroy the widgets after checking
                label_question.destroy()
                math_question_entry.destroy()
                submit_button.destroy()

                # Increment question index
                question_index += 1

                # If there are more questions, show the next one
                if question_index < 10:
                    show_next_question()
                else:
                    # After the quiz ends, show the points
                    label_result = ctk.CTkLabel(root, text=f"Your score: {points}/5", font=("Arial", 20),text_color="black")
                    label_result.place(relx=0.5, rely=0.7, anchor='n')

            # Create a button to submit the answer
            submit_button = ctk.CTkButton(root, text="Submit", command=check_answer, text_color="black")
            submit_button.place(relx=0.5, rely=0.3, anchor='n')

        # Start the quiz by showing the first question
        show_next_question()
    except:
        print("It is okey it is working and if it's working don't touch it")



