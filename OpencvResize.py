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
import tkinter
import tkinter.messagebox
from PyQt5.QtCore import QTimer



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
        self.WidthBox.editingFinished.connect(self.AspectRatio)
        # self.WidthBox.setKeyboardTracking(False)
        # self.WidthBox.valueChanged.connect(QTimer.startTimer(500, self.AspectRatio))
        self.WidthBox.setObjectName("WidthBox")

        self.HeightBox = QtWidgets.QSpinBox(Dialog)
        self.HeightBox.setGeometry(QtCore.QRect(30, 80, 101, 22))
        self.HeightBox.setObjectName("HeightBox")
        self.HeightBox.setRange(0,40000)
        self.HeightBox.editingFinished.connect(self.AspectRatio)
        # self.HeightBox.setKeyboardTracking(False)
        # self.HeightBox.valueChanged.connect(QTimer.startTimer(500, self.AspectRatio))
        
      
        self.AspectRatioButton = QtWidgets.QRadioButton(Dialog)
        self.AspectRatioButton.setGeometry(QtCore.QRect(240, 30,150, 16))
        self.AspectRatioButton.setObjectName("radioButton")
        self.AspectRatioButton.setText("AspectRatio Check")
        # self.AspectRatio.setGeometry(QtCore.QRect(70, 80, 101, 22))
        # self.AspectRatio.setObjectName("AspectRatioBox")

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
        
        if srcpath[0] == '':
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
        if  srcpath == '':
            return
        else:
            srcpath +="/Ouput.png"

        # srcpath = QFileDialog.getExistingDirectory(None,'Choose a directory ''for saving the ''peaks','\home') 
        self.lineEdit.setText(srcpath)


    def AspectRatio(self):
        
        if self.AspectRatioButton.isChecked():
            SrcPath = self.InputEdit.text()
            img = cv2.imdecode(np.fromfile(SrcPath,dtype=np.uint8),cv2.IMREAD_COLOR)
            height, width = img.shape[:2]  

            LargeEdge = self.WidthBox.value() if self.WidthBox.value() > self.HeightBox.value() else self.HeightBox.value()
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
        else:
            return
        


    def OnOk(self):
        SrcPath = self.InputEdit.text()
        if SrcPath == '':
            tkinter.messagebox.showinfo('Finish','Your image is resize down/n')
            
            # tkinter.messagebox.OK('Finish','Your image is resize down/n')
            return

        img = cv2.imdecode(np.fromfile(SrcPath,dtype=np.uint8),cv2.IMREAD_COLOR)
        
        img = cv2.resize(img,(self.WidthBox.value(),self.HeightBox.value()))
        
        cv2.imwrite(self.lineEdit.text(),img)
        tkinter.messagebox.showinfo('Finish','Your image is resize down/n')
        return


    
    
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
