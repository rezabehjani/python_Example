#!/usr/bin/python3
#https://note.nkmk.me/en/python-pillow-qrcode/
import qrcode
from PIL import Image

face = Image.open('8.jpg')
new_width  = 80
new_height = 100
face = face.resize((new_width, new_height), Image.ANTIALIAS)

qr_big = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr_big.add_data('I am Lena')
qr_big.make()
img_qr_big = qr_big.make_image().convert('RGB')

pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)

img_qr_big.paste(face, pos)
img_qr_big.save('qr_lena2.png')