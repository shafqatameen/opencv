import cv2
import numpy as np

# Initialize variables
drawing = False  # True if mouse is pressed
start_x, start_y = -1, -1  # Starting coordinates
image = np.zeros((500, 500, 3), dtype=np.uint8)  # Black canvas

# Mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global start_x, start_y, drawing, image
    
    if event == cv2.EVENT_LBUTTONDOWN:  # Mouse press event
        drawing = True
        start_x, start_y = x, y  # Store starting coordinates
    
    elif event == cv2.EVENT_MOUSEMOVE:  # Mouse movement event
        if drawing:  # Only draw if the left button is pressed
            temp_img = image.copy()  # Copy image to avoid overwriting
            cv2.rectangle(temp_img, (start_x, start_y), (x, y), (0, 255, 0), -1)
            cv2.imshow("Interactive Drawing", temp_img)
    
    elif event == cv2.EVENT_LBUTTONUP:  # Mouse release event
        drawing = False
        cv2.rectangle(image, (start_x, start_y), (x, y), (0, 255, 0), -1)
        cv2.imshow("Interactive Drawing", image)

# Create OpenCV window and set callback
cv2.imshow("Interactive Drawing", image)
cv2.setMouseCallback("Interactive Drawing", draw_rectangle)

# Keep window open until user presses 'q'
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()


'''import cv2
import numpy as np

img=np.zeros( (500,500,3) )

flag=False
ix=-1
iy=-1
def draw(event,x,y,flags,params):
    global ix,iy,flag
    if event==1:
        flag=True
        ix=x
        iy=y
    elif event==0:
        if flag==True:
            cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),-1)
        

    elif event==4:
            flag=False
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            

cv2.namedWindow(winname="window")
cv2.setMouseCallback('window',draw)

while True:
    cv2.imshow('window',img)
    if (cv2.waitKey(1) & 0xFF)==ord('x'):
        break

cv2.destroyAllWindows()'''