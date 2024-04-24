
# Overview

Consider a situation where a reporter needs to send some secret message to news studio or consider a situation of war where soldier needs to pass some secret information to the base. How will they do ?  
One way they can do is by concealing the message into a non-secret Text, Image, Audio or Video file, that will be later used to extract the message.  

The practice of concealing messages or information within other non-secret data, such as text, image, audio, or video files, to avoid detection is known as **Steganography**. This project facilitates the same. It provides the capability to _hide text message in five different file formats_ i,e. `Text` `Image` `Audio` `Gif` and `Video`.


## How to use ?

- Get the repo codes down to your work environment
- Install required python libraries - `tkinter` `os` `numpy` `termcolor` `pyfiglet` `cv2` `pillow` `wave`
- Run any steganography file - `TextStegano.py` `ImageStegano.py` `AudioStegano.py` or `VideoStegano.py`
- All the files that are going to be embed are present in 'sample_files' folder. And after embedding the message output file gets saved in 'Result_files' folder with name as "<file_name>_embeded".
Note that ImageStegHelper.py is a helper file to ImageStegano, that does nothing when compiled. And for embedding in gif use VideoStegno.py


## Working Mechanism of Text Steganography

Text steganography involves hiding secret messages within text files by manipulating the text's content while maintaining its readability. This project provides functionalities for both encoding (embedding) and decoding (extracting) secret messages within text files using a combination of encoding techniques and Zero-Width Characters (ZWC).

### Program Components

#### *Encoding*: 

1. Input Acquisition: The user selects a cover text file and provides the message to be encoded.
2. Binary Conversion: Each character of the input message is converted into binary format, and various transformations are applied based on the character's ASCII value.
3. Embedding: The binary representation of the encoded message is embedded into the cover text file using Zero-Width Characters (ZWC). Each ZWC sequence corresponds to a binary bit.
4. Output Generation: The modified text is written to a new text file, which is saved in the specified directory.

#### *Decoding* 

1. Input Acquisition: The user selects the stego text file from which to extract the hidden message.
2. Data Extraction: ZWC sequences are identified and converted back into binary format to reconstruct the encoded message.
3. Character Reconstruction: The binary-encoded characters are transformed back into ASCII characters to obtain the original message.
4. Output Display: The decoded message is displayed to the user.



## Working Mechanism of Image Steganography


Image steganography involves concealing confidential messages within image files by altering the image's pixel data while preserving its visual integrity. This project facilitates encoding (embedding) and decoding (extracting) of secret messages within images through a combination of techniques such as Least Significant Bit (LSB) encoding, Huffman coding and Run length algorithm. 

By modifying LSB of specific pixel (*as it do not contribute much to image visual* ) and employing compression algorithms, the program seamlessly integrates hidden messages into images, ensuring minimal perceptible changes. Upon decoding, the hidden messages are extracted without compromising the image's appearance, thereby enabling secure communication through covert channels.

### Program Components

#### *Encoding* 

1. Input Acquisition: The user selects an image file and inputs the message to be hidden within it.
2. Text Compression: The message is compressed using Huffman coding to reduce its size.
3. LSB Encoding: Each bit of the compressed message is sequentially embedded into the least significant bit of the image's pixel values. The embedding process alters the pixel values slightly to encode the message without significantly altering the image's appearance.
4. Output Generation: The modified image is saved as a new file in specified directory.

#### *Decoding*

1. Input Acquisition: The user selects the image containing the hidden message.
2. LSB Extraction: The LSB of each pixel in the image is extracted to reconstruct the binary representation of the hidden message.
3. Text Decompression: The extracted binary message is decompressed using Huffman decoding to retrieve the original message.
4. Output Display: The decoded message is displayed to the user.



## Working Mechanism of Audio Steganography

Audio steganography involves embedding and extracting data within audio files without perceptibly altering the audio quality. To embed data, the audio file's binary representation is manipulated by replacing the least significant bits (LSBs) of selected bytes with the binary representation of the secret message. This process subtly modifies the audio data, making it imperceptible to human listeners. 

During extraction, the LSBs of the audio bytes are examined to reconstruct the binary representation of the hidden message. By identifying and decoding the embedded data, the original message can be retrieved without affecting the audio's audible characteristics. This process allows for covert communication through seemingly innocuous audio files, enabling secure transmission of sensitive information while maintaining the integrity of the audio content.

### Program Components

#### *Encoding* 

1. Input Acquisition: The user selects an audio file to encode and inputs the secret message.
2. Data Preparation: The audio file is opened in binary mode, and its frames are read. The frames are then converted into a list of bytes.
3. Message Encoding: The secret message is converted into binary format. A special delimiter (`*^*^*`) is added to mark the end of the message. Each character of the message is encoded into binary format and then embedded into the LSBs of the audio file's byte data.
4. Output Generation: The modified byte data is written back to a new audio file, which is saved in the specified directory.

#### *Decoding*

1. Input Acquisition: The user selects the audio file from which to extract the hidden message.
2. Data Preparation: Similar to the encoding process, the selected audio file's frames are read and converted into byte data.
3. Message Extraction: The LSBs of each byte in the audio data are examined to reconstruct the binary representation of the hidden message. The message extraction continues until the special delimiter (`*^*^*`) is encountered.
4. Output Display: The extracted message is displayed to the user.


## Working Mechanism of Video Steganography

Video steganography involves embedding secret data within video files without significantly affecting the video's visual and auditory quality. Internally, during the embedding process, the program first encrypts the data using a secure encryption algorithm to ensure confidentiality. Then, it divides the encrypted data into binary format and embeds it into the least significant bits (LSBs) of the RGB pixel values in each frame of the video. This process ensures that the changes made to the video are imperceptible to the human eye.
 
During extraction, the LSBs of the RGB pixel values in each frame are extracted, and the embedded data is reconstructed. Subsequently, the extracted data is decrypted using the same encryption key used during embedding, thereby retrieving the original secret message from the video. This combination of encryption and LSB embedding ensures both security and stealthiness in the process of embedding and extracting data from video files.

### Program Components

#### *Encryption*

1. Key Scheduling Algorithm (KSA): Generates the key stream based on the provided encryption key using the RC4 algorithm.
2. Pseudo-Random Generation Algorithm (PRGA): Generates a pseudo-random sequence of bytes based on the key stream and the length of the plaintext.
3. Encryption: Encrypts the plaintext message using the key stream generated by PRGA.

#### *Encoding*

1. The user selects a video file, the data to be embedded, and an encryption key.
2. The provided data is encrypted using the encryption function.
3. The encrypted data is embedded into the LSBs (Least Significant Bits) of the video frames. Each bit of the encrypted data is substituted for the LSB of the RGB pixel values.
4. The modified frames are written to a new video file, which is saved in the specified directory. Additionally, the secret frame is saved as a NumPy array in a text file with the same name as the embedded video.

#### *Decoding*

1. The user provides the required inputs - embeded_video, secret code, secret frame array and frame number.
2. The LSBs of the RGB pixel values are extracted from the video frames to reconstruct the encrypted data.
3. The extracted encrypted data is decrypted using the same encryption key.
4.The decrypted message is displayed to the user.

## User Interface

The program provides a command-line interface (CLI) for users to perform various file steganography operations. Users can choose between encoding a message into a file or decoding a message from a file. The process continues until the user chooses to exit the program. 

Additionally, the program utilizes the tkinter library in Python to present GUI dialogue boxes for selecting (opening) files, enhancing user convenience.


## Team 

- Viswanadha Sai Nissankararao _ 'ME'
- [Nishant Kumar](https://github.com/nishant-kumarr)
