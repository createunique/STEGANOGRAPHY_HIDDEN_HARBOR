from PIL import Image
import numpy as np
import heapq
from collections import defaultdict
import os

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class ImageSteg:
    def __init__(self):
        pass

    # Methods for Huffman Coding
    def build_huffman_tree(self, text):
        frequency = defaultdict(int)
        for char in text:
            frequency[char] += 1

        priority_queue = [HuffmanNode(char, freq) for char, freq in frequency.items()]
        heapq.heapify(priority_queue)

        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)
            merged = HuffmanNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(priority_queue, merged)

        return priority_queue[0]

    def build_huffman_codes(self, root, prefix="", codes=None):
        if codes is None:
            codes = {}
        if root is not None:
            if root.char is not None:
                codes[root.char] = prefix
            self.build_huffman_codes(root.left, prefix + "0", codes)
            self.build_huffman_codes(root.right, prefix + "1", codes)
        return codes

    def huffman_compress(self, text):
        root = self.build_huffman_tree(text)
        codes = self.build_huffman_codes(root)
        encoded_text = "".join(codes[char] for char in text)
        return encoded_text, codes

    def huffman_decompress(self, text, codes):
        decoded_text = ""
        current_code = ""
        for bit in text:
            current_code += bit
            for char, code in codes.items():
                if code == current_code:
                    decoded_text += char
                    current_code = ""
                    break
        return decoded_text

    # Method for Run-Length Encoding
    def rle_compress(self, text):
        encoded_text = ""
        count = 1
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                count += 1
            else:
                encoded_text += str(count) + text[i - 1]
                count = 1
        encoded_text += str(count) + text[-1]
        return encoded_text

    def rle_decompress(self, text):
        decoded_text = ""
        i = 0
        while i < len(text):
            count = int(text[i])
            char = text[i + 1]
            decoded_text += char * count
            i += 2
        return decoded_text

    def __fillMSB(self, inp):
        '''
        0b01100 -> [0,0,0,0,1,1,0,0]
        '''
        inp = inp.split("b")[-1]
        inp = '0'*(7-len(inp))+inp
        return [int(x) for x in inp]

    def __decrypt_pixels(self, pixels):
        '''
        Given list of 7 pixel values -> Determine 0/1 -> Join 7 0/1s to form binary -> integer -> character
        '''
        pixels = [str(x%2) for x in pixels]
        bin_repr = "".join(pixels)
        return chr(int(bin_repr,2))

    def encrypt_text_in_image(self, image_path, msg, target_path=""):
        '''
        Read image -> Flatten -> encrypt images using LSB -> reshape and repack -> return image
        '''
        img = np.array(Image.open(image_path))
        imgArr = img.flatten()
        msg += "<-END->"
        msgArr = [self.__fillMSB(bin(ord(ch))) for ch in msg]
        
        idx = 0
        for char in msgArr:
            for bit in char:
                if bit==1:
                    if imgArr[idx]==0:
                        imgArr[idx] = 1
                    else:
                        imgArr[idx] = imgArr[idx] if imgArr[idx]%2==1 else imgArr[idx]-1
                else: 
                    if imgArr[idx]==255:
                        imgArr[idx] = 254
                    else:
                        imgArr[idx] = imgArr[idx] if imgArr[idx]%2==0 else imgArr[idx]+1   
                idx += 1
            
        filename = os.path.basename(image_path)
        savePath = os.path.join(target_path, filename.split(".")[0] + "_embedded.png")

        resImg = Image.fromarray(np.reshape(imgArr, img.shape))
        resImg.save(savePath)
        return savePath

    def decrypt_text_in_image(self, image_path):
        '''
        Read image -> Extract Text -> Return
        '''
        img = np.array(Image.open(image_path))
        imgArr = np.array(img).flatten()
        
        decrypted_message = ""
        for i in range(7,len(imgArr),7):
            decrypted_char = self.__decrypt_pixels(imgArr[i-7:i])
            decrypted_message += decrypted_char

            if len(decrypted_message)>10 and decrypted_message[-7:] == "<-END->":
                break

        return decrypted_message[:-7]
