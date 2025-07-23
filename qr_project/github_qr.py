import qrcode

# Ask user for the LinkedIn URL
url = input("Paste your github profile URL here: ")

# Generate QR code
qr = qrcode.make(url)

# Save the image
qr.save("github_qr.png")

print("✅ QR Code generated and saved as 'github_qr.png'")