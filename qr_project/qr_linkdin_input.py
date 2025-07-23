import qrcode

# Ask user for the LinkedIn URL
url = input("Paste your LinkedIn profile URL here: ")

# Generate QR code
qr = qrcode.make(url)

# Save the image
qr.save("linkedin_qr.png")

print("✅ QR Code generated and saved as 'linkedin_qr.png'")