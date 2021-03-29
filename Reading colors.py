import cv2
cap = cv2.VideoCapture(0)
while(True):
  #Capture frame-by-frame
  ret, image = cap.read()
  size=image.shape #find the size of the image
  mid_width=int(size[0]/2) #find the middle of the width
  mid_height=int(size[1]/2) #Find the the middle of the height
  #Print the BGR values when 'v' is pressed
  if cv2.waitKey(1) & 0xFF == ord('v'):
    BGR=image[mid_width, mid_height]
    color=[]
    color=BGR
    #print('The BGR values are:',BGR)
    print('The values are:', "Red-->",color[2],"Green-->",color[1],"Blue-->",color[0])
	#Print the BGR value for the center pixel
  #Exit the window when 'e' is pressed
  if cv2.waitKey(1) & 0xFF == ord('e'):
    break
  #Draw a circle around the centre pixel
  r=254
  g=101
  b=50
  cv2.circle(image, (mid_height,mid_width),10 , (b,g,r),thickness=2, lineType=8)
  cv2.imshow('Camera',image)#Display the image
#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()