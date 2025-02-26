import cv2 as cv
#resiszng the frame of video 
def resizedFrame(frame,scale=75):
    width=int(frame.shape[1]*scale/100)
    height=int(frame.shape[0]*scale/100)
    dim=(width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)
capture= cv.VideoCapture("videos/dog.mp4")
while True:
    isTrue,frame=capture.read()
    if not isTrue:
        print('Can not read the video')
        break
    cv.imshow('Video',frame)
    frame_resized=resizedFrame(frame,scale=50)
    cv.imshow('Resized video',frame_resized)

    if cv.waitKey(20)&0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()