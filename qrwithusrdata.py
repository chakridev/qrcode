import qrcode
qr = qrcode.QRCode(
    version=5,
    box_size=5,
    border=2
)
name = input('Enter Name:')
age = int(input('Enter Age:'))
Education = input('Enter Ed.Qualification:')
data = {'My name is':name,
'I am':age,'Qualification':Education}
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='black',back_color='white')
img.save('student.png')
img.show()