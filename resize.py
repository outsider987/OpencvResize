import cv2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import numpy as np


app = QApplication(sys.argv)
srcpath = QFileDialog.getOpenFileName()

img = cv2.imdecode(np.fromfile(srcpath[0],dtype=np.uint8),cv2.IMREAD_COLOR)


height, width = img.shape[:2]  
ratio=1.0

LargeEdge = 1200
if height>width:
    ratio = height/LargeEdge
    height=LargeEdge
    width = width/ratio

else:
    ratio = width/LargeEdge
    width =LargeEdge
    height = height/ratio



output = cv2.resize(img,(width,int(height)))
cv2.imwrite("C:\\Users\\t7902\\OneDrive\\Desktop\\Project\\Opencv\\output.png",output)