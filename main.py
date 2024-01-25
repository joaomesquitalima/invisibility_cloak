import cv2
import numpy

webcam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    cv2.waitKey(1)
    cap, first_img = webcam.read()

    if cap:
        break

while True:
    capturou, img = webcam.read()
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    kernel = numpy.ones((9, 9), numpy.uint8)

    upper_hsv = numpy.array([120, 255, 255])
    lower_hsv = numpy.array([90, 50, 50])

    mask = cv2.inRange(imghsv, lower_hsv, upper_hsv)
    mask = cv2.medianBlur(mask, 19)
    mask_inv = cv2.bitwise_not(mask)

  
    mask= cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    b = cv2.bitwise_and(mask_inv, b)
    g = cv2.bitwise_and(mask_inv, g)
    r = cv2.bitwise_and(mask_inv, r)
    part1 = cv2.merge((b, g, r))

    b = first_img[:, :, 0]
    g = first_img[:, :, 1]
    r = first_img[:, :, 2]
    b = cv2.bitwise_and(b, mask)
    g = cv2.bitwise_and(g, mask)
    r = cv2.bitwise_and(r, mask)
    part2 = cv2.merge((b, g, r))

    final = cv2.add(part1,part2)

    cv2.imshow("capa do harry", final)

    if (cv2.waitKey(3) == ord('q')):
        break


