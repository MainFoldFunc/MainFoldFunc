import tkinter as tk
import customtkinter as ctk
from Quizes.math_quiz import math_quiz
from Quizes.physics_quiz import physics_quiz
from Quizes.Chemistry_quiz import chemistry_quiz
from Quizes.english_quiz import english_quiz
from Quizes.History_quiz import history_quiz


def button_m_command():
    # Create a new top-level window
    new_window = tk.Tk()
    new_window.geometry("400x300")  # Size of the new window
    new_window.title("Math quiz")
    points = math_quiz(new_window)
    new_window.mainloop()
def button_p_command():
    # Create a new top-level window
    new_window = tk.Tk()
    new_window.geometry("400x300")  # Size of the new window
    new_window.title("Physics quiz")
    physics_quiz(new_window)
    new_window.mainloop()
def button_c_command():
    # Create a new top-level window
    new_window = tk.Tk()
    new_window.geometry("400x300")  # Size of the new window
    new_window.title("Chemistry")
    chemistry_quiz(new_window)
    new_window.mainloop()
def button_e_command():
    # Create a new top-level window
    new_window = tk.Tk()
    new_window.geometry("400x300")  # Size of the new window
    new_window.title("English")
    english_quiz(new_window)
    new_window.mainloop()
def button_h_command():
    # Create a new top-level window
    new_window = tk.Tk()
    new_window.geometry("400x300")  # Size of the new window
    new_window.title("History")
    history_quiz(new_window)
    new_window.mainloop()



def buttons_q(root, starting_rely):
    # Define a function to reduce space around the buttons
    def create_button(text, command, y_offset):
        button = ctk.CTkButton(root, text=text, command=command, 
                               width=200, height=40,  # Set a specific size for the button
                               corner_radius=0,  # Square corners to remove extra space
                               fg_color="gray",  # Background color of the button
                               border_width=0)  # Remove border width for a clean look
        button.place(relx=0.75, rely=starting_rely + y_offset, anchor='w')
        return button

    # Create buttons with minimal white space
    create_button("Go to quiz", button_m_command, 0)
    create_button("Go to quiz", button_p_command, 0.1)
    create_button("Go to quiz", button_c_command, 0.2)
    create_button("Go to quiz", button_e_command, 0.3)
    create_button("Go to quiz", button_h_command, 0.4)

