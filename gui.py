# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from collections import OrderedDict
import serial

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 625)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.WalkEngineParam = QtWidgets.QWidget()
        self.WalkEngineParam.setEnabled(True)
        self.WalkEngineParam.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.WalkEngineParam.setObjectName("WalkEngineParam")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.WalkEngineParam)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 30, 701, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(75, -1, 75, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.motionResLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.motionResLabel.setStyleSheet("font: 16pt \"TakaoPGothic\";")
        self.motionResLabel.setObjectName("motionResLabel")
        self.horizontalLayout_5.addWidget(self.motionResLabel)
        self.motionResSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.motionResSpin.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.motionResSpin.setMaximum(999.99)
        self.motionResSpin.setObjectName("motionResSpin")
        self.horizontalLayout_5.addWidget(self.motionResSpin)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(75, -1, 75, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.GaitFreqLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.GaitFreqLabel.setStyleSheet("font: 16pt \"TakaoPGothic\";")
        self.GaitFreqLabel.setObjectName("GaitFreqLabel")
        self.horizontalLayout_6.addWidget(self.GaitFreqLabel)
        self.gaitFreqSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.gaitFreqSpin.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.gaitFreqSpin.setMaximum(999.99)
        self.gaitFreqSpin.setDecimals(3)
        self.gaitFreqSpin.setObjectName("gaitFreqSpin")
        self.horizontalLayout_6.addWidget(self.gaitFreqSpin)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(75, -1, 75, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.singleSuppLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.singleSuppLabel.setStyleSheet("font: 16pt \"TakaoPGothic\";")
        self.singleSuppLabel.setObjectName("singleSuppLabel")
        self.horizontalLayout_7.addWidget(self.singleSuppLabel)
        self.singleSuppSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.singleSuppSpin.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.singleSuppSpin.setMaximum(999.99)
        self.singleSuppSpin.setObjectName("singleSuppSpin")
        self.horizontalLayout_7.addWidget(self.singleSuppSpin)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(75, -1, 75, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.doubleSuppLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.doubleSuppLabel.setStyleSheet("font: 16pt \"TakaoPGothic\";")
        self.doubleSuppLabel.setObjectName("doubleSuppLabel")
        self.horizontalLayout_9.addWidget(self.doubleSuppLabel)
        self.doubleSuppSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSuppSpin.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.doubleSuppSpin.setMaximum(999.99)
        self.doubleSuppSpin.setObjectName("doubleSuppSpin")
        self.horizontalLayout_9.addWidget(self.doubleSuppSpin)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.tabWidget.addTab(self.WalkEngineParam, "")
        self.BodyCom = QtWidgets.QWidget()
        self.BodyCom.setObjectName("BodyCom")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.BodyCom)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 20, 741, 461))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(75, -1, 75, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.comXOff = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.comXOff.setStyleSheet("font: 16pt \"TakaoPGothic\";")
        self.comXOff.setObjectName("comXOff")
        self.horizontalLayout_10.addWidget(self.comXOff)
        self.comXSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.comXSpin.setMaximum(999.99)
        self.comXSpin.setObjectName("comXSpin")
        self.horizontalLayout_10.addWidget(self.comXSpin)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(75, -1, 75, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.comYOff = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.comYOff.setStyleSheet("font: 16pt \"TakaoPGothic\";")
        self.comYOff.setObjectName("comYOff")
        self.horizontalLayout_11.addWidget(self.comYOff)
        self.comYSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.comYSpin.setMaximum(999.99)
        self.comYSpin.setObjectName("comYSpin")
        self.horizontalLayout_11.addWidget(self.comYSpin)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(75, -1, 75, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.comZOff = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.comZOff.setStyleSheet("font: 16pt \"TakaoPGothic\";")
        self.comZOff.setObjectName("comZOff")
        self.horizontalLayout_12.addWidget(self.comZOff)
        self.comZSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.comZSpin.setMaximum(999.99)
        self.comZSpin.setObjectName("comZSpin")
        self.horizontalLayout_12.addWidget(self.comZSpin)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(75, -1, 75, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.comRollOffset = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.comRollOffset.setStyleSheet("font: 16pt \"TakaoPGothic\";")
        self.comRollOffset.setObjectName("comRollOffset")
        self.horizontalLayout_13.addWidget(self.comRollOffset)
        self.comRollSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.comRollSpin.setMaximum(999.99)
        self.comRollSpin.setObjectName("comRollSpin")
        self.horizontalLayout_13.addWidget(self.comRollSpin)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(75, -1, 75, -1)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.comPitchOffset = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.comPitchOffset.setStyleSheet("font: 16pt \"TakaoPGothic\";")
        self.comPitchOffset.setObjectName("comPitchOffset")
        self.horizontalLayout_14.addWidget(self.comPitchOffset)
        self.comPitchSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.comPitchSpin.setMaximum(999.99)
        self.comPitchSpin.setMinimum(-1.0)
        self.comPitchSpin.setDecimals(3)
        self.comPitchSpin.setObjectName("comPitchSpin")
        self.horizontalLayout_14.addWidget(self.comPitchSpin)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(75, -1, 75, -1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.comYawOffset = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.comYawOffset.setStyleSheet("font: 16pt \"TakaoPGothic\";")
        self.comYawOffset.setObjectName("comYawOffset")
        self.horizontalLayout_15.addWidget(self.comYawOffset)
        self.comYawSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.comYawSpin.setMaximum(999.99)
        self.comYawSpin.setObjectName("comYawSpin")
        self.horizontalLayout_15.addWidget(self.comYawSpin)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.tabWidget.addTab(self.BodyCom, "")
        self.VelocityProf = QtWidgets.QWidget()
        self.VelocityProf.setObjectName("VelocityProf")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.VelocityProf)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 751, 451))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(75, -1, 75, -1)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.vXLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.vXLabel.setStyleSheet("font: 16pt \"TakaoPGothic\";\n"
"")
        self.vXLabel.setObjectName("vXLabel")
        self.horizontalLayout_16.addWidget(self.vXLabel)
        self.vXSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.vXSpin.setObjectName("vXSpin")
        self.horizontalLayout_16.addWidget(self.vXSpin)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(75, -1, 75, -1)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.vYLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.vYLabel.setStyleSheet("font: 16pt \"TakaoPGothic\";\n"
"")
        self.vYLabel.setObjectName("vYLabel")
        self.horizontalLayout_17.addWidget(self.vYLabel)
        self.vYSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.vYSpin.setObjectName("vYSpin")
        self.horizontalLayout_17.addWidget(self.vYSpin)
        self.verticalLayout_3.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(75, -1, 75, -1)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.vTLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.vTLabel.setStyleSheet("font: 16pt \"TakaoPGothic\";\n"
"")
        self.vTLabel.setObjectName("vTLabel")
        self.horizontalLayout_18.addWidget(self.vTLabel)
        self.vTSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.vTSpin.setObjectName("vTSpin")
        self.horizontalLayout_18.addWidget(self.vTSpin)
        self.verticalLayout_3.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setContentsMargins(75, -1, 75, -1)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.vXOffLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.vXOffLabel.setStyleSheet("font: 16pt \"TakaoPGothic\";\n"
"")
        self.vXOffLabel.setObjectName("vXOffLabel")
        self.horizontalLayout_19.addWidget(self.vXOffLabel)
        self.vXOffSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.vXOffSpin.setObjectName("vXOffSpin")
        self.horizontalLayout_19.addWidget(self.vXOffSpin)
        self.verticalLayout_3.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setContentsMargins(75, -1, 75, -1)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.vYOffLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.vYOffLabel.setStyleSheet("font: 16pt \"TakaoPGothic\";\n"
"")
        self.vYOffLabel.setObjectName("vYOffLabel")
        self.horizontalLayout_20.addWidget(self.vYOffLabel)
        self.vYOffSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.vYOffSpin.setObjectName("vYOffSpin")
        self.horizontalLayout_20.addWidget(self.vYOffSpin)
        self.verticalLayout_3.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setContentsMargins(75, -1, 75, -1)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.vTOffLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.vTOffLabel.setStyleSheet("font: 16pt \"TakaoPGothic\";\n"
"")
        self.vTOffLabel.setObjectName("vTOffLabel")
        self.horizontalLayout_21.addWidget(self.vTOffLabel)
        self.vTOffSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.vTOffSpin.setObjectName("vTOffSpin")
        self.horizontalLayout_21.addWidget(self.vTOffSpin)
        self.verticalLayout_3.addLayout(self.horizontalLayout_21)
        self.tabWidget.addTab(self.VelocityProf, "")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(190, 550, 131, 41))
        self.startBtn.setStyleSheet("font: 20pt \"TakaoPGothic\";\n"
"color : rgb(0, 170, 0);")
        self.startBtn.setObjectName("startBtn")
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(430, 550, 131, 41))
        self.stopBtn.setStyleSheet("font: 20pt \"TakaoPGothic\";\n"
"color : rgb(202, 0, 0)")
        self.stopBtn.setObjectName("stopBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        #MyCode Start

        self.flag = False
        self.mainValues =[]

        try:
            self.ser = serial.Serial('COM4', 115200)
            self.flag = True
        except:
            print("Port not found")
            self.flag = False

        self.actionSave.triggered.connect(self.saveFile)
        self.actionOpen.triggered.connect(self.openFile)

        self.stopBtn.clicked.connect(self.stopRobot)
        self.startBtn.clicked.connect(self.startRobot)
        #MyCode Finish

        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def saveFile(self):
        dlg = QFileDialog()
        fileName = QFileDialog.getSaveFileName(None, "Save Your Record","","")
        #if fileName:
        #    print(fileName)
        values = OrderedDict()

        values["V_X"] = str(self.vXSpin.value())
        values["V_Y"] = str(self.vYSpin.value())
        values["V_T"] = str(self.vTSpin.value())
        values["Vx_Offset"] = str(self.vXOffSpin.value())
        values["Vy_Offset"] = str(self.vYOffSpin.value())
        values["Vt_Offset"] = str(self.vTOffSpin.value())

        values["P_Motion_Resolution"] = str(self.motionResSpin.value())
        values["P_Gait_Frequency"] = str(self.gaitFreqSpin.value())
        values["P_Double_Support_Sleep"] = str(self.doubleSuppSpin.value())
        values["P_Single_Support_Sleep"] = str(self.singleSuppSpin.value())

        values["P_COM_X_offset"] = str(self.comXSpin.value())
        values["P_COM_Y_offset"] = str(self.comYSpin.value())
        values["P_COM_Z_offset"] = str(self.comZSpin.value())
        values["P_COM_Roll_offset"] = str(self.comRollSpin.value())
        values["P_COM_Pitch_offset"] = str(self.comPitchSpin.value())
        values["P_COM_Yaw_offset"] = str(self.comYawSpin.value())

        myFile = open(fileName[0] + '.txt', 'w')
        #myFile.write("{" + '\n')
        for value in values:
            if(value == "V_X" or value == "V_Y" or value == "V_T"):
                myFile.write("//WEP[" + value + "] = " + values[value] + ';' + '\n')
            else:
                myFile.write("WEP[" + value + "] = " + values[value] + ';' + '\n')
        #myFile.write('}')
        myFile.close()
        #dlg.setacceptMode(QFileDialog.AcceptSave)

    def openFile(self):

        seq = []
        seq.append(self.vXSpin)
        seq.append(self.vYSpin)
        seq.append(self.vTSpin)
        seq.append(self.vXOffSpin)
        seq.append(self.vYOffSpin)
        seq.append(self.vTOffSpin)
        seq.append(self.motionResSpin)
        seq.append(self.gaitFreqSpin)
        seq.append(self.doubleSuppSpin)
        seq.append(self.singleSuppSpin)
        seq.append(self.comXSpin)
        seq.append(self.comYSpin)
        seq.append(self.comZSpin)
        seq.append(self.comRollSpin)
        seq.append(self.comPitchSpin)
        seq.append(self.comYawSpin)

        #dlg = QFileDialog()
        fileName = QFileDialog.getOpenFileName(None, "Open your Record","","Text Files (*.txt)")
        #if fileName:
        #    print(fileName)
        #print("hello")
        myFile = open(fileName[0], 'r')
        #lenght = len(myFile.readlines())
        cnt = 0
        for line in myFile:
            #line.replace('\n', '')
            line = line.split(' = ')
            line[1] = (line[1].split(';'))[0]
            #print(line)
            seq[cnt].setValue(float(line[1]))
            cnt += 1
        myFile.close()

    def stopRobot(self):
        if(self.flag):
            #myArr = bytearray([254, 0, 0, 0, 112, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            myArr = bytearray(self.generateStop())
            self.ser.write(myArr)
        else:
            print("Not Connected to Robot")

    def startRobot(self):
        if(self.flag):
            #myArr = bytearray([254, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            myArr = bytearray(self.generateStart())
            #while True:
            self.ser.write(myArr)
        else:
            #print(self.generateStart())
            #myArr = bytearray(self.generateStart())
            #myArr = self.generateStart()
            print ("Not connected to Robot")

    def generateFormule(self, value):
            return int((value * 100) + 100)

    def generateStart(self):
        values = []
        values.append(254)
        values.append(self.generateFormule(self.vXSpin.value()))
        values.append(self.generateFormule(self.vYSpin.value()))
        values.append(self.generateFormule(self.vTSpin.value()))
        values.append(100)
        values.append(self.generateFormule(self.vXOffSpin.value()))
        values.append(self.generateFormule(self.vYOffSpin.value()))
        values.append(self.generateFormule(self.vTOffSpin.value()))
        values.append(self.generateFormule(self.motionResSpin.value()))
        values.append(self.generateFormule(self.gaitFreqSpin.value()))
        #values.append(self.generateFormule(self.doubleSuppSpin.value()))
        values.append(int(self.doubleSuppSpin.value()))
        #values.append(self.generateFormule(self.singleSuppSpin.value()))
        values.append(int(self.singleSuppSpin.value()))
        #values.append(self.generateFormule(self.comXSpin.value()))
        values.append(int(self.comXSpin.value()))
        #values.append(self.generateFormule(self.comYSpin.value()))
        values.append(int(self.comYSpin.value()))
        #values.append(self.generateFormule(self.comZSpin.value()))
        values.append(int(self.comZSpin.value()))
        values.append(self.generateFormule(int(self.comRollSpin.value())))
        values.append(self.generateFormule(self.comPitchSpin.value()))
        #values.append(0)
        values.append(self.generateFormule(self.comYawSpin.value()))
        #values.append(0)
        print(values)
        return values

    def generateStop(self):
        values = []
        values.append(254)
        values.append(0)
        values.append(0)
        values.append(0)
        values.append(112)
        values.append(0)
        values.append(0)
        values.append(0)
        values.append(self.generateFormule(self.motionResSpin.value()))
        values.append(self.generateFormule(self.gaitFreqSpin.value()))
        #values.append(self.generateFormule(self.doubleSuppSpin.value()))
        values.append(int(self.doubleSuppSpin.value()))
        #values.append(self.generateFormule(self.singleSuppSpin.value()))
        values.append(int(self.singleSuppSpin.value()))
        #values.append(self.generateFormule(self.comXSpin.value()))
        values.append(int(self.comXSpin.value()))
        #values.append(self.generateFormule(self.comYSpin.value()))
        values.append(int(self.comYSpin.value()))
        #values.append(self.generateFormule(self.comZSpin.value()))
        values.append(int(self.comZSpin.value()))
        values.append(self.generateFormule(int(self.comRollSpin.value())))
        values.append(self.generateFormule(self.comPitchSpin.value()))
        #values.append(0)
        values.append(self.generateFormule(self.comYawSpin.value()))
        return values

    def updateValues(self):
        values = []
        values.append(254)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.motionResLabel.setText(_translate("MainWindow", "Motion Resolution"))
        self.GaitFreqLabel.setText(_translate("MainWindow", "Gait Frequency"))
        self.singleSuppLabel.setText(_translate("MainWindow", "Single Support Sleep"))
        self.doubleSuppLabel.setText(_translate("MainWindow", "Double Support Sleep"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.WalkEngineParam), _translate("MainWindow", "Walk Engine Parameters"))
        self.comXOff.setText(_translate("MainWindow", "COM X Offset"))
        self.comYOff.setText(_translate("MainWindow", "COM Y Offset"))
        self.comZOff.setText(_translate("MainWindow", "COM Z Offset"))
        self.comRollOffset.setText(_translate("MainWindow", "COM Roll Offset"))
        self.comPitchOffset.setText(_translate("MainWindow", "COM Pitch Offset"))
        self.comYawOffset.setText(_translate("MainWindow", "COM Yaw Offset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BodyCom), _translate("MainWindow", "Body Com"))
        self.vXLabel.setText(_translate("MainWindow", "V x"))
        self.vYLabel.setText(_translate("MainWindow", "V y"))
        self.vTLabel.setText(_translate("MainWindow", "V t"))
        self.vXOffLabel.setText(_translate("MainWindow", "V x offset"))
        self.vYOffLabel.setText(_translate("MainWindow", "V y offset"))
        self.vTOffLabel.setText(_translate("MainWindow", "V t offset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VelocityProf), _translate("MainWindow", "Velocity Profile"))
        self.startBtn.setText(_translate("MainWindow", "START"))
        self.stopBtn.setText(_translate("MainWindow", "STOP"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

