#!/usr/bin/env python
# coding: utf-8

# In[13]:


import cv2

video_capture = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret,frame = video_capture.read()
    #Imagenp=show_inference(detection_model, frame)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows() 


# In[19]:


import pyttsx3
engine=pyttsx3.init()
engine.say('hello good morning')
engine.runAndWait()


# In[ ]:


import pytesseract
from PIL import Image
import pyttsx3
import cv2
img=cv2.imread('img.jpg')
cv2.imshow('image',img)
text=pytesseract.image_to_string(img)
print(text)
engine=pyttsx3.init()
engine.say(text)
engine.runAndWait()

cv2.waitKey(0)
cv2.destroyAllWindows()

