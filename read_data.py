import cv2
import easyocr
from flask import jsonify


def reader(path, lang, isDetail, isGpu):
    image = cv2.imread(fr'{path}')
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    img_id_card = img_gray[35:80, 310:600]
    img_fullname = img_gray[80:140, 200:700]
    img_address = img_gray[280:368, 75:550]

    easyReader = easyocr.Reader([lang], gpu=isGpu)
    idCardData = easyReader.readtext(img_id_card, detail=isDetail)
    fullNameData = easyReader.readtext(img_fullname, detail=isDetail)
    addressData = easyReader.readtext(img_address, detail=isDetail)
    return jsonify({"IdCard": ''.join(idCardData), "FullName": ''.join(fullNameData), "Address": ''.join(addressData)})
