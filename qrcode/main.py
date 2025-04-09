# ToDo1
# generate a qrcode for an employee having its credentials
# import qrcode
#
# json_data = {
#     'Emp_id': 123456,
#     'Name': 'John',
#     'date': '09-04-2025',
# }
# img = qrcode.make(str(json_data))
# print(type(img))    #this return <class 'PIL.Image.Image'>
# img.save("my_qrcode.png")

# to do 2: to read the data through camera and print it
import cv2
data = {}
camera = cv2.VideoCapture(0)
# this opens the default camera of the system

detector = cv2.QRCodeDetector()
# this will detect the qr from the camera in real time
while True:
    _,image = camera.read()
    data, bbox, straight_qrcode = detector.detectAndDecode(image)
    print(data)
    if data:
        a = data
        break
    cv2.imshow("QRCODEscanner", image)
    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

import csv
fields = ['Emp_id', 'Name', 'date']


with open("qrData.csv", "a") as f:
    f.write(data)
    f.write("\n")