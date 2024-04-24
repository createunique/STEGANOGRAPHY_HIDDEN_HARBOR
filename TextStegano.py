import os
import numpy as np
import tkinter as tk
from tkinter import filedialog

import termcolor
from termcolor import colored
from pyfiglet import figlet_format

def txt_encode(text, cover_file_path):
    l = len(text)
    i = 0
    add = ''
    while i < l:
        t = ord(text[i])
        if t >= 32 and t <= 64:
            t1 = t + 48
            t2 = t1 ^ 170  # 170: 10101010
            res = bin(t2)[2:].zfill(8)
            add += "0011" + res
        else:
            t1 = t - 48
            t2 = t1 ^ 170
            res = bin(t2)[2:].zfill(8)
            add += "0110" + res
        i += 1
    res1 = add + "111111111111"
    print("The string after binary conversion appyling all the transformation :- " + (res1))
    length = len(res1)
    print("Length of binary after conversion:- ", length)
    HM_SK = ""
    ZWC = {"00": u'\u200C', "01": u'\u202C', "11": u'\u202D', "10": u'\u200E'}
    filename = os.path.splitext(os.path.basename(cover_file_path))[0]
    
    result_folder = "Result_files"
    # Construct the stego file path
    stego_file_path = os.path.join(result_folder, filename + "_stegano.txt")
    
    with open(cover_file_path, "r+") as file1, open(stego_file_path, "w+", encoding="utf-8") as file3:
        word = []
        for line in file1:
            word += line.split()
        i = 0
        while i < len(res1):
            s = word[int(i / 12)]
            j = 0
            x = ""
            HM_SK = ""
            while j < 12:
                x = res1[j + i] + res1[i + j + 1]
                HM_SK += ZWC[x]
                j += 2
            s1 = s + HM_SK
            file3.write(s1)
            file3.write(" ")
            i += 12
        t = int(len(res1) / 12)
        while t < len(word):
            file3.write(word[t])
            file3.write(" ")
            t += 1
    
    print("\nStego file has been successfully generated at:", stego_file_path)

def encode_txt_data():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    print("\tSelect the file")
    cover_file_path = filedialog.askopenfilename(title="Select Cover Text File")
    count2 = 0
    with open(cover_file_path, "r") as file1:
        for line in file1:
            for word in line.split():
                count2 = count2 + 1
    bt = int(count2)
    print("Maximum number of words that can be inserted :- ", int(bt / 6))
    text1 = input("\nEnter data to be encoded:- ")
    l = len(text1)
    if l <= bt:
        print("\nInputed message can be hidden in the cover file\n")
        txt_encode(text1, cover_file_path)
    else:
        print("\nString is too big please reduce string size")
        encode_txt_data()

def txt_decode(stego_file_path):
    ZWC_reverse = {u'\u200C': "00", u'\u202C': "01", u'\u202D': "11", u'\u200E': "10"}
    temp = ''
    with open(stego_file_path, "r", encoding="utf-8") as file4:
        for line in file4:
            for words in line.split():
                T1 = words
                binary_extract = ""
                for letter in T1:
                    if letter in ZWC_reverse:
                        binary_extract += ZWC_reverse[letter]
                if binary_extract == "111111111111":
                    break
                else:
                    temp += binary_extract
    print("\nEncrypted message presented in code bits:", temp)
    lengthd = len(temp)
    print("\nLength of encoded bits:- ", lengthd)
    i = 0
    a = 0
    b = 4
    c = 4
    d = 12
    final = ''
    while i < len(temp):
        t3 = temp[a:b]
        a += 12
        b += 12
        i += 12
        t4 = temp[c:d]
        c += 12
        d += 12
        if t3 == '0110':
            decimal_data = BinaryToDecimal(t4)
            final += chr((decimal_data ^ 170) + 48)
        elif t3 == '0011':
            decimal_data = BinaryToDecimal(t4)
            final += chr((decimal_data ^ 170) - 48)
    print("\nMessage after decoding from the stego file:- ", final)

def decode_txt_data():
    root = tk.Tk()
    print("\tSelect the file")
    root.withdraw()  
    # Hide the window
    root.attributes('-alpha', 0.0)
    # Always have it on top
    root.attributes('-topmost', True)
    stego_file_path = filedialog.askopenfilename(title="Select Stego Text File")
    txt_decode(stego_file_path)

def txt_steg():

    # Use one of the recognized color names
    print(colored(figlet_format("Hidden Layers"), color='red'))

    while True:
        print("\nSELECT THE TEXT STEGANOGRAPHY OPERATION\n")
        print("1. Encode the Text message")
        print("2. Decode the Text message")
        print("3. Exit")
        choice1 = int(input("Enter the Choice: "))
        if choice1 == 1:
            encode_txt_data()
        elif choice1 == 2:
            decode_txt_data()
        elif choice1 == 3:
            break
        else:
            print("Incorrect Choice")
        print("\n")

def BinaryToDecimal(binary):
    string = int(binary, 2)
    return string

if __name__ == "__main__":
    txt_steg()
