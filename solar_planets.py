import cv2

img = cv2.imread("solar-system.jpg")

cv2.imshow("Output", img)

cv2.waitKey(0)

cv2.putText(
    img,
    "Sun",
    (100,40),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (255,255,255)
)


cv2.putText(
    img,
    "Mercury",
    (100,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.75,
    (255,255,255)
)

cv2.putText(
    img,
    "VENUS",
    (180,150),
    cv2.FONT_HERSHEY_COMPLEX,
    0.75,
    (255,255,255)
)
cv2.putText(
    img,
    "Earth",
    (280,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.75,
    (255,255,255)
)
cv2.putText(
    img,
    "Mars",
    (380,150),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(
    img,
    "Jupiter",
    (500,380),
    cv2.FONT_HERSHEY_COMPLEX,
    0.85,
    (255,255,255)
)
cv2.putText(
    img,
    "Saturn",
    (730,100),
    cv2.FONT_HERSHEY_COMPLEX,
    0.85,
    (255,255,255)
)
cv2.putText(
    img,
    "Uranus",
    (950,350),
    cv2.FONT_HERSHEY_COMPLEX,
    0.85,
    (255,255,255)
)
cv2.putText(
    img,
    "Neptune",
    (1090,130),
    cv2.FONT_HERSHEY_COMPLEX,
    0.85,
    (255,255,255)
)
cv2.imshow("Output", img)
cv2.imwrite("Solar_systemwithname.jpg",img)
