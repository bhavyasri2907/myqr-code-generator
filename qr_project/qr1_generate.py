import qrcode

data = input("Enter text or URL: ")

qr = qrcode.make(data)

qr.save("qr_code.png")

print("QR Code saved as qr_code.png")