import tkinter as tk
import customtkinter as ctk
from main_quiz_labels import labels_q
from Buttons_to_quiz import buttons_q
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Main function to create the Tkinter window and widgets
def main():
    # Create the main window
    root = tk.Tk()
    root.geometry("1080x720")  # Size of the window
    root.title("Quiz In Python")

    # Load a .jpg image using Pillow
    background_image = Image.open("sky.png")
    background_image = background_image.resize((1080, 720), Image.Resampling.LANCZOS)  # Resize to fit the window

    # Convert the image to a Tkinter-compatible format
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a canvas to place the background image
    canvas = ctk.CTkCanvas(root, width=1080, height=720)
    canvas.pack(fill="both", expand=True)

    # Set the background image
    canvas.create_image(0, 0, anchor="nw", image=background_photo)

    # Configure the appearance of customtkinter
    ctk.set_appearance_mode("dark")  # Light or dark mode
    ctk.set_default_color_theme("blue")  # Set the color theme

    st = 0.2
    points = 0  # Initialize the points variable
    labels_q(root, st, points)  # Pass the points variable here
    buttons_q(root, st)
    
    points_label = ctk.CTkLabel(root, text=f"Your points are: {points}",
                                font=("Aharoni", 20), fg_color="darkblue",
                                text_color="black"
                                )
    points_label.place(relx=0, rely=st - 0.1, anchor="w")

    root.mainloop()

# Run the main function
if __name__ == "__main__":
    main()

