# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpencvResize_Aspect_ratio.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.WidthBox.setObjectName("WidthBox")
        self.HeightBox = QtWidgets.QSpinBox(Dialog)
        self.HeightBox.setGeometry(QtCore.QRect(30, 80, 101, 22))
        self.HeightBox.setObjectName("HeightBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 47, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 47, 12))
        self.label_2.setObjectName("label_2")
        self.InputFileButton = QtWidgets.QPushButton(Dialog)
        self.InputFileButton.setGeometry(QtCore.QRect(310, 130, 75, 23))
        self.InputFileButton.setObjectName("InputFileButton")
        self.InputEdit = QtWidgets.QLineEdit(Dialog)
        self.InputEdit.setGeometry(QtCore.QRect(40, 130, 261, 20))
        self.InputEdit.setText("")
        self.InputEdit.setObjectName("InputEdit")
        self.OutPutPathButton = QtWidgets.QPushButton(Dialog)
        self.OutPutPathButton.setGeometry(QtCore.QRect(310, 180, 75, 23))
        self.OutPutPathButton.setObjectName("OutPutPathButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 180, 261, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(240, 30, 83, 16))
        self.radioButton.setObjectName("radioButton")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Width"))
        self.label_2.setText(_translate("Dialog", "Height\'"))
        self.InputFileButton.setText(_translate("Dialog", "Open File"))
        self.OutPutPathButton.setText(_translate("Dialog", "Output Path"))
        self.radioButton.setText(_translate("Dialog", "RadioButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
