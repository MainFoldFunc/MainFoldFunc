import tkinter as tk
import customtkinter as ctk




def labels_q(root, starting_rely, points):
    # Create a CTkLabel for the topic with rounded corners and black background
    label_topic = ctk.CTkLabel(root, text="What level do you choose", 
                               font=("Aharoni", 40), 
                               corner_radius=0,  # Rounded corners
                               text_color="white",
                               fg_color="black")  # Transparent background
    label_topic.place(relx=0.5, rely=0.05, anchor='n')  # Position at the top center

    # Create quiz labels with black background
    label_quiz_1 = ctk.CTkLabel(root, text="1. Maths", 
                                 font=("Amasis MT Pro", 30), 
                                 corner_radius=0, text_color="purple",
                                 fg_color="black")  # Transparent background
    label_quiz_1.place(relx=0.1, rely=starting_rely, anchor='w')  # Align to the left side

    label_quiz_2 = ctk.CTkLabel(root, text="2. Physics", 
                                 font=("Amasis MT Pro", 30), 
                                 corner_radius=0, text_color="red",
                                 fg_color="black")  # Transparent background
    label_quiz_2.place(relx=0.1, rely=starting_rely + 0.1, anchor='w')  # 10% below first label

    label_quiz_3 = ctk.CTkLabel(root, text="3. Chemistry", 
                                 font=("Amasis MT Pro", 30), 
                                 corner_radius=0, text_color="blue",
                                 fg_color="black")  # Transparent background
    label_quiz_3.place(relx=0.1, rely=starting_rely + 0.2, anchor='w')  # 0% below first label

    label_quiz_4 = ctk.CTkLabel(root, text="4. English", 
                                 font=("Amasis MT Pro", 30), 
                                 corner_radius=0, text_color="pink",
                                 fg_color="black")  # Transparent background
    label_quiz_4.place(relx=0.1, rely=starting_rely + 0.3, anchor='w')  # 30% below first label

    label_quiz_5 = ctk.CTkLabel(root, text="5. History", 
                                 font=("Amasis MT Pro", 30), 
                                 corner_radius=0, text_color="green",
                                 fg_color="black")  # Transparent background
    label_quiz_5.place(relx=0.1, rely=starting_rely + 0.4, anchor='w')  # 40% below first label

