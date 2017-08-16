import qrcode


def encode_url_and_show(url):
    img = qrcode.make(url)
    return img


def encode_words_ec(words):
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constans.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(words)
    qr.make(fit=True)
    img = qr.make_image()
    return img

if __name__ == '__main__':
    img = encode_url_and_show('http://crossincode.com/oj/practice/75/')
    img.show()
