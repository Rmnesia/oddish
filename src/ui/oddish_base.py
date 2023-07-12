# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../src/ui/oddish.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 750)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.settings = QtWidgets.QGroupBox(self.centralwidget)
        self.settings.setObjectName("settings")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.settings)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.settings)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.steamCookie = QtWidgets.QPlainTextEdit(self.settings)
        self.steamCookie.setEnabled(False)
        self.steamCookie.setMaximumSize(QtCore.QSize(16777215, 30))
        self.steamCookie.setObjectName("steamCookie")
        self.horizontalLayout.addWidget(self.steamCookie)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.settings)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.buffCookie = QtWidgets.QPlainTextEdit(self.settings)
        self.buffCookie.setEnabled(False)
        self.buffCookie.setMaximumSize(QtCore.QSize(16777215, 30))
        self.buffCookie.setObjectName("buffCookie")
        self.horizontalLayout_2.addWidget(self.buffCookie)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.getSteam = QtWidgets.QPushButton(self.settings)
        self.getSteam.setObjectName("getSteam")
        self.horizontalLayout_3.addWidget(self.getSteam)
        self.getBuff = QtWidgets.QPushButton(self.settings)
        self.getBuff.setObjectName("getBuff")
        self.horizontalLayout_3.addWidget(self.getBuff)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.settings)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.settings)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.priceMin = QtWidgets.QDoubleSpinBox(self.settings)
        self.priceMin.setMaximum(150000)
        self.priceMin.setObjectName("priceMin")
        self.horizontalLayout_4.addWidget(self.priceMin)
        self.label_4 = QtWidgets.QLabel(self.settings)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.priceMax = QtWidgets.QDoubleSpinBox(self.settings)
        self.priceMax.setMaximum(150000)
        self.priceMax.setObjectName("priceMax")
        self.horizontalLayout_4.addWidget(self.priceMax)
        self.line_3 = QtWidgets.QFrame(self.settings)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_4.addWidget(self.line_3)
        self.typeRestrict = QtWidgets.QPushButton(self.settings)
        self.typeRestrict.setObjectName("typeRestrict")
        self.horizontalLayout_4.addWidget(self.typeRestrict)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.settings)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.useProxy = QtWidgets.QCheckBox(self.settings)
        self.useProxy.setText("")
        self.useProxy.setChecked(True)
        self.useProxy.setObjectName("useProxy")
        self.horizontalLayout_8.addWidget(self.useProxy)
        self.label_7 = QtWidgets.QLabel(self.settings)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.proxyEditor = QtWidgets.QPlainTextEdit(self.settings)
        self.proxyEditor.setMaximumSize(QtCore.QSize(16777215, 30))
        self.proxyEditor.setObjectName("proxyEditor")
        self.horizontalLayout_8.addWidget(self.proxyEditor)
        self.proxyVaild = QtWidgets.QToolButton(self.settings)
        self.proxyVaild.setObjectName("proxyVaild")
        self.horizontalLayout_8.addWidget(self.proxyVaild)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.crawlStart = QtWidgets.QPushButton(self.settings)
        self.crawlStart.setObjectName("crawlStart")
        self.verticalLayout_4.addWidget(self.crawlStart)
        self.verticalLayout_2.addWidget(self.settings)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.logger = QtWidgets.QTextEdit(self.groupBox_2)
        self.logger.setObjectName("logger")
        self.verticalLayout_3.addWidget(self.logger)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Oddish"))
        self.settings.setTitle(_translate("MainWindow", "设置"))
        self.label.setText(_translate("MainWindow", "Steam:"))
        self.label_2.setText(_translate("MainWindow", "Buff: "))
        self.getSteam.setText(_translate("MainWindow", "获取Steam Cookies"))
        self.getBuff.setText(_translate("MainWindow", "获取Buff Cookies"))
        self.label_3.setText(_translate("MainWindow", "价格限定："))
        self.priceMin.setSuffix(_translate("MainWindow", "¥"))
        self.label_4.setText(_translate("MainWindow", "-"))
        self.priceMax.setSuffix(_translate("MainWindow", "¥"))
        self.typeRestrict.setText(_translate("MainWindow", "类型限定"))
        self.label_7.setText(_translate("MainWindow", "代理:"))
        self.proxyVaild.setText(_translate("MainWindow", "..."))
        self.crawlStart.setText(_translate("MainWindow", "开始"))
        self.groupBox_2.setTitle(_translate("MainWindow", "输出"))
