import cv2
import easyocr

img = cv2.imread(r'../assets/images/id_card.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# img_wb_card = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)[1]
img_id_card = img_gray[35:80, 310:600]


# img_wb_name = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)[1]
img_name = img_gray[80:140, 200:700]

# img_wb_address = cv2.threshold(img_gray, 60, 255, cv2.THRESH_BINARY)[1]
img_address = img_gray[280:368, 75:550]

reader = easyocr.Reader(['th'], gpu=True)
idCardText = reader.readtext(img_id_card, detail=0)
nameText = reader.readtext(img_name, detail=0)
addressText = reader.readtext(img_address, detail=0)

print("id card : ")
print(idCardText)

print("full name : ")
print(nameText)

print("address : ")
print(addressText)

# cv2.imshow('id', img_id_card)
# cv2.imshow('name', img_name)
# cv2.imshow('address', img_address)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
