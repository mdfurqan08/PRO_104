import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "SUN",
            (20,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "mercury",
            (120,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,205,255))

cv2.putText(img,
            "venus",
            (200,150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,205,255))

cv2.putText(img,
            "earth",
            (300,150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,205,255))

cv2.putText(img,
            "mars",
            (400,150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,205,255))

cv2.putText(img,
            "jupiter",
            (500,300),
            cv2.FONT_HERSHEY_COMPLEX,
            1.0,
            (255,205,255))

cv2.putText(img,
            "saturn",
            (700,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,205,255))

cv2.putText(img,
            "uranus",
            (950,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "meacuery",
            (1100,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,205,255))



cv2.imshow("hlo",img)

cv2.waitKey(0)
