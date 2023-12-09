import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from gtts import gTTS
import os
import pygame
import time
 
 
# Define a dictionary mapping text to image file paths
image_map = {
    "A": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\A_E_I.jpeg",
    "B": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\B_M_P.jpeg",
    "C": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "D": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "E": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\A_E_I.jpeg",
    "F": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\F_V.jpeg",
    "G": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "H": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\TH.jpeg",
    "I": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\A_E_I.jpeg",
    "J": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\CH_J_SH.jpeg",
    "K": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "L": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\L.jpeg",
    "M": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\B_M_P.jpeg",
    "N": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\N.jpeg",
    "O": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\O.jpeg",
    "P": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\B_M_P.jpeg",
    "Q": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\Q_W.jpeg",
    "R": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "S": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "T": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "U": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\U.jpeg",
    "V": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\F_V.jpeg",
    "W": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\Q_W.jpeg",
    "X": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "Y": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "Z": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "CH": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\CH_J_SH.jpeg",
    "SH": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\CH_J_SH.jpeg",
    "TH": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\TH.jpeg",
    "a": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\A_E_I.jpeg",
    "b": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\B_M_P.jpeg",
    "c": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "d": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "e": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\A_E_I.jpeg",
    "f": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\F_V.jpeg",
    "g": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "h": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\TH.jpeg",
    "i": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\A_E_I.jpeg",
    "j": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\CH_J_SH.jpeg",
    "k": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "l": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\L.jpeg",
    "m": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\B_M_P.jpeg",
    "n": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\N.jpeg",
    "o": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\O.jpeg",
    "p": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\B_M_P.jpeg",
    "q": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\Q_W.jpeg",
    "r": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "s": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "t": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "u": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\U.jpeg",
    "v": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\F_V.jpeg",
    "w": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\Q_W.jpeg",
    "x": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "y": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "z": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\C_D_G_K_N_R_S_T_X_Y_Z.jpeg",
    "ch": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\CH_J_SH.jpeg",
    "sh": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\CH_J_SH.jpeg",
    "th": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\TH.jpeg",
    "face": "C:\\Users\\I527297\\Desktop\\CPAD\\Lips\\fac.png"

}
 
 
# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))  # Correct the reference to __file__
audio_folder = os.path.join(script_dir, "Audio")
 
# Variable to store the last entered text
last_entered_text = ""
 
 
def speech_update():
    global last_entered_text
    text = text_entry.get()
 
    if text != last_entered_text:
        last_entered_text = text
 
        # Create the "Audio" folder if it doesn't exist
        try:
            if not os.path.exists(audio_folder):
                os.makedirs(audio_folder)
        except OSError as e:
            print(f"Error creating the 'Audio' folder: {e}")
 
        # Create a unique audio filename based on a timestamp
        timestamp = int(time.time())
        audio_filename = os.path.join(audio_folder, f"output_{timestamp}.mp3")
 
        # Create a gTTS object and save the text as audio
        try:
            tts = gTTS(text)
            tts.save(audio_filename)
        except Exception as e:
            print(f"Error creating audio: {e}")
 
 
def show_lips():
    text = text_entry.get()
    VISEME(text)
    play_audio()
 
 
def VISEME(text):
    # Remove any existing images
    image_label.pack_forget()
 
    # Split the text into individual letters
    letters = [letter for letter in text if letter in image_map]
 
    if letters:
        display_images(letters, 0)
 
 
def display_images(letters, index):
    if index < len(letters):
        letter = letters[index]
        image_path = image_map.get(letter)
        if image_path:
            try:
                face_path = image_map.get("face")
                face_image = Image.open(face_path).convert("RGBA")
                new_size = (600, 600)
                resized_face_image = face_image.resize(new_size)
                print(resized_face_image.mode)
                print(resized_face_image.info)
                # image_label1.config(image=face_photo)
                # image_label1.image = face_photo
                
                image = Image.open(image_path).convert("RGBA")
                new_size = (400, 400)
                resized_image = image.resize(new_size)
                print(resized_image.mode)
                print(resized_image.info)
                # photo = ImageTk.PhotoImage(resized_image)
                resized_face_image.paste(resized_image,(113,178),resized_image)
                face_photo = ImageTk.PhotoImage(resized_face_image)
 
                image_label.config(image=face_photo)
                image_label.image = face_photo
                # image_label1.pack()
                image_label.pack()
 
                # Schedule the next image after a delay (e.g., 500 milliseconds)
                app.after(100, display_images, letters, index + 1)
            except Exception as e:
                print(f"Error displaying image: {e}")
        else:
            print(f"Image not found for letter: {letter}")
 
    else:
        # Display the final image
        final_image_path = ""  # Replace with the path to your final image
        final_image = Image.open(final_image_path)
        new_size = (100, 100)
        resized_final_image = final_image.resize(new_size)
        final_photo = ImageTk.PhotoImage(resized_final_image)
 
        image_label.config(image=final_photo)
        image_label.image = final_photo
        image_label.pack()
 
 
def play_audio():
    speech_update()
    play_speech()
 
 
def play_speech():
    # List audio files in ascending order
    audio_files = sorted([f for f in os.listdir(audio_folder) if f.endswith(".mp3")])
 
    if audio_files:
        latest_audio_file = os.path.join(audio_folder, audio_files[-1])
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(latest_audio_file)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Error playing audio: {e}")
 
 
# Create the main application window
app = tk.Tk()
app.title("Modern Image Viewer")
 
# Set the initial size of the window
app.geometry("600x400")  # Width x Height
 
# Use themed widgets (ttk)
style = ttk.Style()
style.configure('TButton', foreground='blue', padding=10)
style.configure('TLabel', foreground='green')
 
# Create a text input field
text_label = ttk.Label(app, text="Enter text:")
text_label.pack()
text_entry = ttk.Entry(app)
text_entry.pack()
 
# Bind the update_audio function to the <<FocusOut>> event
text_entry.bind("<FocusOut>", lambda e: speech_update())
 
# Create a label to display the image
image_label = ttk.Label(app)
 
# Create a button with updated style
speak_button = ttk.Button(app, text="Speak", command=show_lips, style='TButton')
speak_button.pack()
 
app.mainloop()