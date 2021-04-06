import cv2 as cv

# #Alterar resolução de video ao vivo apenas, webcam etc
# def changeRes(largura, altura):
#     capture.set(3, largura)
#     capture.set(4, altura)

#     largura= int(frame.shape[1] * scale)
#     altura= int(frame.shape[0] * scale)
#     dimensions=(largura, altura)
    
#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)





#Alterar escala de imagem, vídeo e ao vivo como webcam
def rescaleFrame(frame, scale=0.4):
    largura= int(frame.shape[1] * scale)
    altura= int(frame.shape[0] * scale)
    dimensions=(largura, altura)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)







# img = cv.imread('Fotos/Capturar.png')
# resized_image = rescaleFrame(img)

# cv.imshow('Fodase', img)
# cv.imshow('Fodase_resize', resized_image)

# cv.waitKey(0)





#0, 1, 2, [...] para webcam, para vídeo apenas botar diretório
video = cv.VideoCapture(0)

while True:
    isTrue, frame = video.read()

    frame_rescale = rescaleFrame(frame)
    # frame_resized = changeRes(frame)

    cv.imshow('video', frame)
    cv.imshow('video_rescale', frame_rescale)
    # cv.imshow('video_resize', frame_resized)       #Não consegui, o cara n ensinou ¯\_(ツ)_/¯

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()




cv.waitKey(0)