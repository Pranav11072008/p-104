import cv2
image = cv2.imread("solar-system.jpg")
cv2.imshow("result",image)
cv2.waitKey(0)
cv2.putText(image,
            "sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(image,
            "mercury",
            (20,310),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(image,
            "venus",
            (20,320),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(image,
            "Earth",
            (20,340),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(image,
            "Mars",
            (20,350),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(image,
            "jupiter",
            (20,360),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(image,
            "Saturn",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(image,
            "Uranus",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(image,
            "neptune",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)