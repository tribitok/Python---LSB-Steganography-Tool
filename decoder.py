from PIL import Image
import sys

try:
    im = sys.argv[1]
    if not im or not im.endswith('.png'):
        raise ValueError
except ValueError:
    sys.exit('Enter valid image')

with Image.open(im) as ima:
    image = ima.convert('RGB')
    width = image.size[0]
    height = image.size[1]
    px = image.load()

    secret_message = '...'
    eight_bin = ''

    for i in range(height):
        if secret_message[-3:] =='###':
            break
        for j in range(width):
            if secret_message[-3:] == '###':
                break

            for colour in px[i,j]:
                if len(eight_bin) < 8:
                    colour_bin = bin(colour)
                    eight_bin += colour_bin[-1]
                else:
                    secret_message += chr(int(eight_bin,2))
                    eight_bin = ''
                    colour_bin = bin(colour)
                    eight_bin += colour_bin[-1]

print(secret_message[3:-3])