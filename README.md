Python LSB Steganography Tool

A simple command-line tool to hide and extract secret messages inside PNG images using Least Significant Bit (LSB) steganography.

Features
**Encoder**: Secretly embeds a text message into the pixels of a PNG image without visibly altering it.
 **Decoder**: Reads a stego-image and extracts the hidden message.

 Prerequisites
You need Python installed on your system along with the `Pillow` library for image processing. 

You can install the required library using pip:
```bash
python3 -m pip install Pillow
```
How to use:
Step 1: Run the encoder script from your terminal and insert the secret message. For example:
python3 encoder.py original_image.png

Step 2: Run the decoder script passing the image that contains the hidden text:
python3 decoder.py result.png

Example:
In this repository, you can find test.png (the original image) and risultato.png (an image containing a hidden message). Try running the decoder on risultato.png to test the script!
