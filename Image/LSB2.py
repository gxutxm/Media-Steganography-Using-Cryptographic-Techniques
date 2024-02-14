from tkinter import filedialog
from tkinter import *
from PIL import Image

def select_image():
    root = Tk()
    root.withdraw()  # Hide the main window

    # Open a file dialog to select the image file
    file_path = filedialog.askopenfilename()
    return file_path

def Encode(img_path, msg):
    img = Image.open(img_path)
    length = len(msg)
    if length > 255:
        print("Text too long! (don't exceed 255 characters)")
        return False
    if img.mode != 'RGB':
        print("Image mode needs to be RGB")
        return False
    encoded_img = img.copy()
    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            if row == 0 and col == 0 and index < length:
                asc = length
            else:
                asc = r
            encoded_img.putpixel((col, row), (asc, g, b))
            index += 1
    return encoded_img

def Decode(img_path):
    img = Image.open(img_path)
    width, height = img.size
    msg_length = 0
    decoded_msg = ""
    index = 0
    for row in range(height):
        for col in range(width):
            r, _, _ = img.getpixel((col, row))
            if row == 0 and col == 0:
                msg_length = r
            elif index < msg_length:
                decoded_msg += chr(r)
            index += 1
    return decoded_msg

# Example usage:
image_path = select_image()
msg_to_encode = "Hello, World!"
encoded_image = Encode(image_path, msg_to_encode)
encoded_image.save("encoded_image.png")  # Save the encoded image
decoded_msg = Decode("encoded_image.png")
print("Decoded message:", decoded_msg)
