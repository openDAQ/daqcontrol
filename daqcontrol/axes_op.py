# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'daqcontrol/axes_op.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 433)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(MainWindow)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setMinimumSize(QtCore.QSize(100, 27))
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.ax_title = QtWidgets.QLineEdit(MainWindow)
        self.ax_title.setObjectName("ax_title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ax_title)
        self.verticalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.ax_left = QtWidgets.QLineEdit(MainWindow)
        self.ax_left.setObjectName("ax_left")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ax_left)
        self.ax_right = QtWidgets.QLineEdit(MainWindow)
        self.ax_right.setObjectName("ax_right")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ax_right)
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.ax_xlb = QtWidgets.QLineEdit(MainWindow)
        self.ax_xlb.setObjectName("ax_xlb")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ax_xlb)
        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.ax_xscale = QtWidgets.QComboBox(MainWindow)
        self.ax_xscale.setObjectName("ax_xscale")
        self.ax_xscale.addItem("")
        self.ax_xscale.addItem("")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ax_xscale)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_7 = QtWidgets.QLabel(MainWindow)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.ax_bottom = QtWidgets.QLineEdit(MainWindow)
        self.ax_bottom.setObjectName("ax_bottom")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ax_bottom)
        self.ax_top = QtWidgets.QLineEdit(MainWindow)
        self.ax_top.setObjectName("ax_top")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ax_top)
        self.label_8 = QtWidgets.QLabel(MainWindow)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(MainWindow)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.ax_ylb = QtWidgets.QLineEdit(MainWindow)
        self.ax_ylb.setObjectName("ax_ylb")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ax_ylb)
        self.label_10 = QtWidgets.QLabel(MainWindow)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(MainWindow)
        self.label_11.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.ax_yscale = QtWidgets.QComboBox(MainWindow)
        self.ax_yscale.setObjectName("ax_yscale")
        self.ax_yscale.addItem("")
        self.ax_yscale.addItem("")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ax_yscale)
        self.verticalLayout.addLayout(self.formLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.ax_Bok = QtWidgets.QPushButton(MainWindow)
        self.ax_Bok.setMinimumSize(QtCore.QSize(100, 27))
        self.ax_Bok.setObjectName("ax_Bok")
        self.horizontalLayout.addWidget(self.ax_Bok)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Axes options"))
        self.label.setText(_translate("MainWindow", "Title "))
        self.label_3.setText(_translate("MainWindow", "Left"))
        self.label_4.setText(_translate("MainWindow", "Right"))
        self.label_5.setText(_translate("MainWindow", "Label"))
        self.label_6.setText(_translate("MainWindow", "Scale"))
        self.label_2.setText(_translate("MainWindow", "X-Axis"))
        self.ax_xscale.setItemText(0, _translate("MainWindow", "linear"))
        self.ax_xscale.setItemText(1, _translate("MainWindow", "log"))
        self.label_7.setText(_translate("MainWindow", "Bottom"))
        self.label_8.setText(_translate("MainWindow", "Top"))
        self.label_9.setText(_translate("MainWindow", "Label"))
        self.label_10.setText(_translate("MainWindow", "Scale"))
        self.label_11.setText(_translate("MainWindow", "Y-Axis"))
        self.ax_yscale.setItemText(0, _translate("MainWindow", "linear"))
        self.ax_yscale.setItemText(1, _translate("MainWindow", "log"))
        self.ax_Bok.setText(_translate("MainWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

