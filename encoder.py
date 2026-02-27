from PIL import Image
import sys

def modify_lsb(colour, bit):
    colour_bin = bin(colour)[2:].zfill(8)
    modified = colour_bin[:-1] + bit

    return int(modified, 2)

secret_message = input('Enter the secret message: ') + '###'
bin_secret_lst = []
for i in secret_message:
    bin_secret_lst.append(bin(ord(i)))
bin_secret = ''
for i in bin_secret_lst:
    to_add = i[2:]
    to_add_ = to_add.zfill(8)
    bin_secret += to_add_

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
    count = 0
    for i in range(height):
        if count == len(bin_secret):
            break
        for j in range(width):
            if count == len(bin_secret):
                break
            r, g, b = px[i,j]
            if count < len(bin_secret):
                r = modify_lsb(r, bin_secret[count])
                count += 1

            if count < len(bin_secret):
                g = modify_lsb(g, bin_secret[count])
                count += 1

            if count < len(bin_secret):
                b = modify_lsb(b, bin_secret[count])
                count += 1

            px[i,j] = (r,g,b)

    image.save('risultato.png')