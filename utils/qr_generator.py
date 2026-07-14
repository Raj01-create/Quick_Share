import qrcode
import os


def generate_qr(link, code, qr_folder):
    img = qrcode.make(link)

    qr_path = os.path.join(qr_folder, f"{code}.png")

    img.save(qr_path)

    return qr_path