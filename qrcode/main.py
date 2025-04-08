# ToDo1
# generate a qrcode for an employee having its credentials
# import qrcode
# img = qrcode.make('Emp_id: 123456, Name: John, date: 09-04-2025')
# type(img)
# img.save("my_qrcode.png")

# to do 2: to read the data through camera and print it
import cv2


cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
last_data = ""


while True:
    _, frame = cap.read()
    data, bbox, _ = detector.detectAndDecode(frame)
    if data and data != last_data:
        print(data)
        last_data = data


    cv2.imshow("QR code detector", frame)
    key = cv2.waitKey(1)

    cv2.imshow("QRCODEscanner", frame )
    if cv2.waitKey(1) == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
fs =  open('qrData.csv', 'a')
fs.write(data+'\n')
fs.close()