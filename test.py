import cv2


def test(x):
    print(x)


switch = 'color/gray'

cv2.namedWindow("Image")

cv2.createTrackbar('B', "Image", 0, 255, test)
cv2.createTrackbar('G', "Image", 0, 255, test)
cv2.createTrackbar('R', "Image", 0, 255, test)
cv2.createTrackbar(switch, 'Image', 0, 2, test)


while 1:
    img = cv2.imread('12.jpg')
    img = cv2.resize(img, (512, 512))
    b = cv2.getTrackbarPos('B', "Image")
    g = cv2.getTrackbarPos('G', "Image")
    r = cv2.getTrackbarPos('R', "Image")
    s = cv2.getTrackbarPos(switch, 'Image')

    cv2.putText(img, str(b), (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255))
    cv2.putText(img, str(g), (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255))
    cv2.putText(img, str(r), (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255))



    if s == 0:
        pass

    elif s == 1:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    img = cv2.imshow('Image', img)


    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
