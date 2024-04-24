import wave
import os
import tkinter as tk
from tkinter import filedialog

import termcolor
from termcolor import colored
from pyfiglet import figlet_format

def encode_aud_data():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    print("\tSelect the file")
    # Hide the window
    root.attributes('-alpha', 0.0)
    # Always have it on top
    root.attributes('-topmost', True)
    nameoffile = filedialog.askopenfilename(title="Select Audio File to Encode")
    song = wave.open(nameoffile, mode='rb')

    nframes = song.getnframes()
    frames = song.readframes(nframes)
    frame_list = list(frames)
    frame_bytes = bytearray(frame_list)

    data = input("\nEnter the secret message :- ")

    res = ''.join(format(i, '08b') for i in bytearray(data, encoding ='utf-8'))     
    print("\nThe string after binary conversion :- " + (res))   
    length = len(res)
    print("\nLength of binary after conversion :- ",length)

    data = data + '*^*^*'

    result = []
    for c in data:
        bits = bin(ord(c))[2:].zfill(8)
        result.extend([int(b) for b in bits])

    j = 0
    for i in range(0,len(result),1): 
        res = bin(frame_bytes[j])[2:].zfill(8)
        if res[len(res)-4]== result[i]:
            frame_bytes[j] = (frame_bytes[j] & 253)      #253: 11111101
        else:
            frame_bytes[j] = (frame_bytes[j] & 253) | 2
            frame_bytes[j] = (frame_bytes[j] & 254) | result[i]
        j = j + 1
    
    frame_modified = bytes(frame_bytes)

    filename = os.path.splitext(os.path.basename(nameoffile))[0]
    stegofile = os.path.join("Result_files", filename + "_embeded.wav")

    with wave.open(stegofile, 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
    
    print("\nEncoded the data successfully in the audio file.")    
    song.close()

def decode_aud_data():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    print("\tSelect the file")
    # Hide the window
    root.attributes('-alpha', 0.0)
    # Always have it on top
    root.attributes('-topmost', True)
    nameoffile = filedialog.askopenfilename(title="Select Audio File to Decode")
    song = wave.open(nameoffile, mode='rb')

    nframes = song.getnframes()
    frames = song.readframes(nframes)
    frame_list = list(frames)
    frame_bytes = bytearray(frame_list)

    extracted = ""
    p = 0
    for i in range(len(frame_bytes)):
        if p == 1:
            break
        res = bin(frame_bytes[i])[2:].zfill(8)
        if res[len(res)-2] == '0':
            extracted += res[len(res)-4]
        else:
            extracted += res[len(res)-1]
    
        all_bytes = [ extracted[i: i+8] for i in range(0, len(extracted), 8) ]
        decoded_data = ""
        for byte in all_bytes:
            decoded_data += chr(int(byte, 2))
            if decoded_data[-5:] == "*^*^*":
                print("The Encoded data was :--", decoded_data[:-5])
                p = 1
                break  

def aud_Steg():
    print(colored(figlet_format("Hidden Layers"), color='red'))
    while True:
        print("\nSELECT AUDIO STEGANOGRAPHY OPERATION\n") 
        print("1. Embed the message")  
        print("2. Decode the message")  
        print("3. Exit")  
        choice1 = int(input("Enter the Choice: "))   
        if choice1 == 1:
            encode_aud_data()
        elif choice1 == 2:
            decode_aud_data()
        elif choice1 == 3:
            break
        else:
            print("Incorrect Choice")
        print("\n")

if __name__ == "__main__":
    aud_Steg()