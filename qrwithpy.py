import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import ast
data = decode(Image.open('student.png'))
info = data[0].data.decode('ascii')
data = ast.literal_eval(info)
#print(type(data))
print(data['My name is'].upper())
print(data['I am'])
