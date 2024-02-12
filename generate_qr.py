import qrcode

# Create a QRCode object
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Add data to the QRCode object
qr.add_data("https://www.nrt-kenya.org")

# Compile the QRCode data into a QRCode image
qr.make(fit=True)

# Create an image from the QRCode data
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qr.png", "PNG")
