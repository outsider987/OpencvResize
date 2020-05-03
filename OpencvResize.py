# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpencvResize.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import cv2




class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        
        self.buttonBox.setObjectName("buttonBox")
        self.WidthBox = QtWidgets.QSpinBox(Dialog)
        self.WidthBox.setGeometry(QtCore.QRect(30, 30, 101, 22))
        self.WidthBox.setRange(0,40000)
        
        self.WidthBox.setObjectName("WidthBox")

        self.HeightBox = QtWidgets.QSpinBox(Dialog)
        self.HeightBox.setGeometry(QtCore.QRect(30, 80, 101, 22))
        self.HeightBox.setObjectName("HeightBox")
        self.HeightBox.setRange(0,40000)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 47, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 47, 12))
        self.label_2.setObjectName("label_2")
        self.InputFileButton = QtWidgets.QPushButton(Dialog)
        self.InputFileButton.setGeometry(QtCore.QRect(310, 130, 75, 23))
        self.InputFileButton.setObjectName("InputFileButton")
        self.InputFileButton.clicked.connect(self.openfile)

        self.InputEdit = QtWidgets.QLineEdit(Dialog)
        self.InputEdit.setGeometry(QtCore.QRect(40, 130, 261, 20))
        self.InputEdit.setText("")
        self.InputEdit.setObjectName("InputEdit")
    
        self.OutPutPathButton = QtWidgets.QPushButton(Dialog)
        self.OutPutPathButton.setGeometry(QtCore.QRect(310, 180, 75, 23))
        self.OutPutPathButton.setObjectName("OutPutPathButton")
        self.OutPutPathButton.clicked.connect(self.savefile)

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 180, 261, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.OnOk)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Width"))
        self.label_2.setText(_translate("Dialog", "Height\'"))
        self.InputFileButton.setText(_translate("Dialog", "Open File"))
        self.OutPutPathButton.setText(_translate("Dialog", "Output Path"))

    def openfile(self):
        srcpath = QFileDialog.getOpenFileName()
        
        if srcpath == None:
            return
        else:
            self.InputEdit.setText(srcpath[0])
            SrcPath = self.InputEdit.text()

            img=cv2.imdecode(np.fromfile(SrcPath,dtype=np.uint8),-1)
            height, width = img.shape[:2]
            self.WidthBox.setValue(width)
            self.HeightBox.setValue(height)
            
    def savefile(self):
        # QFileDialog.(None,'save file',os.getcwd(),"Images (*.png *.xpm *.jpg)")
        srcpath = QFileDialog.getExistingDirectory(None,"Select Floder...","");  
        srcpath +="/Ouput.png"
        # srcpath = QFileDialog.getExistingDirectory(None,'Choose a directory ''for saving the ''peaks','\home') 
        self.lineEdit.setText(srcpath)


    def AspectRatio(self,iWidth,iHeight):
        img = cv2.imdecode(self.InputEdit.displayText(),cv2.IMREAD_COLOR)
        height, width = img.shape[:2]  

        LargeEdge = iWidth if iWidth > iHeight else iHeight
        ratio=1.0

        if height>width:
            ratio = height/LargeEdge
            height=LargeEdge
            width = width/ratio

        else:
            ratio = width/LargeEdge
            width =LargeEdge
            height = height/ratio

        self.WidthBox.setValue(width)
        self.HeightBox.setValue(height)
        


    def OnOk(self):
         
        img = cv2.imdecode(self.InputEdit.displayText(),cv2.IMREAD_COLOR)
        height, width = img.shape[:2]  

        ratio=1.0

        # True if self.WidthBox. == 'Apple' else False

        # LargeEdge = 1200
        # if height>width:
        #     ratio = height/LargeEdge
        #     height=LargeEdge
        #     width = width/ratio

        # else:
        #     ratio = width/LargeEdge
        #     width =LargeEdge
        #     height = height/ratio
    
    
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
