import qrcode

qr = qrcode.QRCode(
    version=5,
    box_size=5,
    border=2
)
data = 'https://youtu.be/hUDkzo2vEvg' #here we have to give our link 
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='yellow',back_color='white')
img.save('youtubefirstvideo.png')
