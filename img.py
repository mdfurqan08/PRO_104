import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "SUN",
            (20,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.imshow("hlo",img)

cv2.waitKey(0)
