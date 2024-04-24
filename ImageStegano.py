from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog
from imageStegHelper import ImageSteg

import termcolor
from termcolor import colored
from pyfiglet import figlet_format

def encode_message():
    img = ImageSteg()
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask user to select an image file
    print("\tSelect the file")
    # Hide the window
    root.attributes('-alpha', 0.0)
    # Always have it on top
    root.attributes('-topmost', True)
    image_path = filedialog.askopenfilename(title="Select an image to hide the message")

    if image_path:
        msg = input("Enter the message to hide in the image: ")
        print("\n\tEncoding underway ! Please wait ... \n\n")
        target_path = "C:\\Users\\nisha\\OneDrive\\Desktop\\Steno_Final\\Result_files"
        img.encrypt_text_in_image(image_path, msg, target_path)
        print("Message hidden in the image.")

def decode_message():
    img = ImageSteg()
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask user to select an image file
    print("\tSelect the file")
    # Hide the window
    root.attributes('-alpha', 0.0)
    # Always have it on top
    root.attributes('-topmost', True)
    image_path = filedialog.askopenfilename(title="Select an image to decode the message")

    if image_path:
        decoded_msg = img.decrypt_text_in_image(image_path)
        print("\n\tDecoded message:", decoded_msg)

def main():

    print(colored(figlet_format("Hidden Layers"), color='red'))
    while True:
        print("\nSELECT THE IMAGE STEGANOGRAPHY OPERATION\n")
        print("1. Encode message into an image")
        print("2. Decode message from an image")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            encode_message()
        elif choice == "2":
            decode_message()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
