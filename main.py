import cv2 as cv

# img = cv.imread('Fotos/Capturar.png')
# cv.imshow('Fodase', img)

# cv.waitKey(0)


#0, 1, 2, [...] para webcam, para vídeo apenas botar diretório
video = cv.VideoCapture('Videos/PatoGS.mp4')

while True:
    isTrue, frame = video.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()