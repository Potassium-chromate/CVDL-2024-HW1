# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from q1 import CameraCalibration
from q2 import Argumented_Reality
import Load


CB = CameraCalibration()
AR = Argumented_Reality()

class Ui_Dialog(object):
    def __init__(self):
        self.spin_value = 0
        self.text = ""
        
    def Loadfolder_func(self):
        Load.Loadfolder()
        
    def Find_corner_func(self):
        CB.Find_corner()
    
    def Find_intrinsic_func(self):
        CB.Find_Intrinsic()
        
    def Find_extrinsic_func(self):
        CB.Find_Extrinsic(self.spin_value)
    
    def Find_distortion_func(self):
        CB.Find_Distortion(self.spin_value)
    
    def Show_result_func(self):
        CB.Show_Result(self.spin_value)
        
    def Show_word_func(self):
        AR.vertical_mode = False
        print(self.text)
        AR.Show_on_board(self.text)
        
    def Show_word_vertical_func(self):
        AR.vertical_mode = True
        AR.Show_on_board(self.text)
    
    def on_spin_value_changed(self, value):
        self.spin_value = value
        
    def textEdit_changed(self):
        self.text = self.textEdit.toPlainText()
        print("textEdit_changed:",self.text)
        
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(988, 717)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 160, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.LoadImage = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.LoadImage.setContentsMargins(5, 5, 5, 5)
        self.LoadImage.setObjectName("LoadImage")
        self.Loadfolder = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Loadfolder.setObjectName("Loadfolder")
        ####### Load Image #######
        
        self.Loadfolder.clicked.connect(self.Loadfolder_func)
        
        ##########################
        self.LoadImage.addWidget(self.Loadfolder)
        self.LoadImage_L = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.LoadImage_L.setObjectName("LoadImage_L")
        self.LoadImage.addWidget(self.LoadImage_L)
        self.LoadImage_R = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.LoadImage_R.setObjectName("LoadImage_R")
        self.LoadImage.addWidget(self.LoadImage_R)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 61, 21))
        self.label.setObjectName("label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(210, 30, 109, 203))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Find_corner = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Find_corner.setObjectName("Find_corner")
        self.verticalLayout.addWidget(self.Find_corner)
        ####### Find_corner #######
        
        self.Find_corner.clicked.connect(self.Find_corner_func)
        
        ##########################
        self.Find_intrinsic = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Find_intrinsic.setObjectName("Find_intrinsic")
        self.verticalLayout.addWidget(self.Find_intrinsic)
        ####### Find_intrinsic #######
        
        self.Find_intrinsic.clicked.connect(self.Find_intrinsic_func)
        
        ##########################
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.valueChanged.connect(self.on_spin_value_changed)        
        self.verticalLayout_2.addWidget(self.spinBox)
        self.Find_extrinsic = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Find_extrinsic.setObjectName("Find_extrinsic")
        self.verticalLayout_2.addWidget(self.Find_extrinsic)
        ####### Find_extrinsic #######
        
        self.Find_extrinsic.clicked.connect(self.Find_extrinsic_func)
        
        ##########################
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.Find_distortion = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Find_distortion.setObjectName("Find_distortion")
        self.verticalLayout.addWidget(self.Find_distortion)
        ####### Find_distortion #######
        
        self.Find_distortion.clicked.connect(self.Find_distortion_func)
        
        ##########################
        self.Show_result = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Show_result.setObjectName("Show_result")
        self.verticalLayout.addWidget(self.Show_result)
        ####### Show_result #######
        
        self.Show_result.clicked.connect(self.Show_result_func)
        
        ##########################
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(210, 10, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(350, 10, 111, 16))
        self.label_4.setObjectName("label_4")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(530, 30, 160, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Stereo_disparity_map = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.Stereo_disparity_map.setObjectName("Stereo_disparity_map")
        self.verticalLayout_5.addWidget(self.Stereo_disparity_map)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(530, 10, 121, 16))
        self.label_5.setObjectName("label_5")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(350, 310, 141, 231))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Load_Image_1 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.Load_Image_1.setObjectName("Load_Image_1")
        self.verticalLayout_6.addWidget(self.Load_Image_1)
        self.Laod_Image_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.Laod_Image_2.setObjectName("Laod_Image_2")
        self.verticalLayout_6.addWidget(self.Laod_Image_2)
        self.Keypoints = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.Keypoints.setObjectName("Keypoints")
        self.verticalLayout_6.addWidget(self.Keypoints)
        self.Matched_keypoints = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.Matched_keypoints.setObjectName("Matched_keypoints")
        self.verticalLayout_6.addWidget(self.Matched_keypoints)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(350, 290, 111, 16))
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(350, 30, 141, 228))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_3.setSpacing(50)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.textChanged.connect(self.textEdit_changed)    
        self.verticalLayout_3.addWidget(self.textEdit)
        self.Show_words_on_board = QtWidgets.QPushButton(self.layoutWidget)
        self.Show_words_on_board.setObjectName("Show_words_on_board")
        ####### Show_result #######
        
        self.Show_words_on_board.clicked.connect(self.Show_word_func)
        
        ##########################
        self.verticalLayout_3.addWidget(self.Show_words_on_board)
        self.Show_words_vertical = QtWidgets.QPushButton(self.layoutWidget)
        self.Show_words_vertical.setObjectName("Show_words_vertical")
        ####### Show_result #######
        
        self.Show_words_vertical.clicked.connect(self.Show_word_vertical_func)
        
        ##########################
        self.verticalLayout_3.addWidget(self.Show_words_vertical)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Loadfolder.setText(_translate("Dialog", "Load folder"))
        self.LoadImage_L.setText(_translate("Dialog", "Load Image_L"))
        self.LoadImage_R.setText(_translate("Dialog", "Load Image_R"))
        self.label.setText(_translate("Dialog", "Load Image"))
        self.Find_corner.setText(_translate("Dialog", "1.1 Find corner"))
        self.Find_intrinsic.setText(_translate("Dialog", "1.2 Find intrinsic"))
        self.label_3.setText(_translate("Dialog", "1.3 Find extrinsic"))
        self.Find_extrinsic.setText(_translate("Dialog", "1.3 Find extrinsic"))
        self.Find_distortion.setText(_translate("Dialog", "1.4 Find distortion"))
        self.Show_result.setText(_translate("Dialog", "1.5 Show result"))
        self.label_2.setText(_translate("Dialog", "1. Calibration"))
        self.label_4.setText(_translate("Dialog", "2. Argumented Reality"))
        self.Stereo_disparity_map.setText(_translate("Dialog", "3.1 Stereo disparity map"))
        self.label_5.setText(_translate("Dialog", "3. Stereo disparity map"))
        self.Load_Image_1.setText(_translate("Dialog", "Load Image1"))
        self.Laod_Image_2.setText(_translate("Dialog", "Load Image2"))
        self.Keypoints.setText(_translate("Dialog", "4.1 Keypoints"))
        self.Matched_keypoints.setText(_translate("Dialog", "4.2 Matched Keypoints"))
        self.label_6.setText(_translate("Dialog", "4. SIFT"))
        self.textEdit.setWhatsThis(_translate("Dialog", "<html><head/><body><p>3</p></body></html>"))
        self.Show_words_on_board.setText(_translate("Dialog", "2.1 Show words on board"))
        self.Show_words_vertical.setText(_translate("Dialog", "2.2 Show words vertical"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())