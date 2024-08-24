
import qrcode

input = ""

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(input)
qr.make(fit=True)

try:
    img = qr.make_image(fill='black', back_color='white')
    img.save('qr.png')
    print("QR code generated")
except:
    print("QR code generation failed")
