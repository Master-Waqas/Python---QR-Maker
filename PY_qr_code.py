import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=5,)

qr.add_data("https://www.linkedin.com/in/master-waqas-2502a02a7/")
qr.make(fit=True)
img = qr.make_image(fill_color=input("Enter Fill Color :"), back_color=input("Enter Background Color :"))
img.save("python.png")
