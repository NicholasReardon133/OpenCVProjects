import cv2 
 
# Create a video capture object, in this case we are reading the video from a file
vid_capture = cv2.VideoCapture('COM251Group0.2.mp4')
 
if (vid_capture.isOpened() == False):
  print("Error opening the video file")
# Read fps and frame count
else:
  # Get frame rate information
  # You can replace 5 with CAP_PROP_FPS as well, they are enumerations
  fps = vid_capture.get(5)
  print('Frames per second : ', fps,'FPS')
 
  # Get frame count
  # You can replace 7 with CAP_PROP_FRAME_COUNT as well, they are enumerations
  frame_count = vid_capture.get(7)
  print('Frame count : ', frame_count)
 
  bit_rate = vid_capture.get(cv2.CAP_PROP_BITRATE)
  print('Bit rate : ', bit_rate)

while(vid_capture.isOpened()):
  # vid_capture.read() methods returns a tuple, first element is a bool 
  # and the second is frame
  ret, frame = vid_capture.read()
  if ret == True:
    cv2.imshow('Frame',frame)
    # 20 is in milliseconds, try to increase the value, say 50 and observe
    key = cv2.waitKey(25)
     
     #If the 'q' key is pressed, exit program
    if key == ord('q'):
      break
    #If the X on the window is pressed, end program
    ###########CURRENTLY THROWS ERROR, NEEDS HANDLING############
    if cv2.getWindowProperty('Frame',0) == -1:
      break
  else:
    break
 
# Release the video capture object
vid_capture.release()
cv2.destroyAllWindows()