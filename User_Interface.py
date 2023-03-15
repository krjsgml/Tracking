import sys
from tkinter import Label, Widget
import cv2
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtTest import *
import numpy as np
from object_data import data

running = False

class first(QWidget): 
    
    def __init__(self):
        super().__init__()
        self.initUI()


############################# 시작 화면 ################################


    def initUI(self):

    ## 라벨
        label_img_st = QLabel()
        pixmap = QPixmap('Graduation/img_st1.png')
        pixmap = pixmap.scaledToWidth(app.desktop().screenGeometry().width()) # 모니터 해상도 가로 길이
        label_img_st.setPixmap(QPixmap(pixmap))
        label_img_st.setAlignment(Qt.AlignCenter)

    ## 레이아웃

        vbox = QVBoxLayout()
        vbox.addWidget(label_img_st)
        
        self.setLayout(vbox)

        global touch
        touch = 1

    ## 스크린       
        self.setWindowTitle('Autonomous Driving Choices')
        self.showFullScreen()


############################## 시작화면 터치시 다음으로 넘어감 ###############################


    def mousePressEvent(self, e):  # e ; QMouseEvent
        global touch
        if (e.button() == Qt.LeftButton) & (touch == 1):
            touch = 0
            self.Main()


############################### 메인 쇼핑 창 ##############################


## No버튼 선택시
    def Main(self):
        def Barcode():
            num = 0
            while True:
                barcode_data = input("바코드를 찍어주세요 : ")
                print("바코드정보 = " + barcode_data)

                if barcode_data in data.keys():
                    product = data[barcode_data]
                    print(data[barcode_data])
                    
                    self.Table.setItem(num,0,QTableWidgetItem(product))
                    self.Table.repaint()

                    num = num+1
            
                else:
                    continue

                if data == 'q':
                    break

        def Product_Cancel():
            
            print("stoped..")

        def Activate_Scanner():
            th = threading.Thread(target=Barcode)
            th.start()
            print("started..")


        self.Widget_Shopping = QWidget()
    
        self.label_total = QLabel('총 금액 : ')
        font = self.label_total.font()
        font.setPointSize(40)
        font.setFamily('한컴산뜻돋움')
        font.setBold(True)
        self.label_total.setFont(font)

        label_P = QLabel('                                     장바구니           ')
        font = label_P.font()
        font.setPointSize(40)
        font.setFamily('한컴산뜻돋움')
        font.setBold(True)
        label_P.setFont(font)

        self.Table = QTableWidget(3,3)
        #self.Table.setColumnCount(3)
        self.Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.Table.setHorizontalHeaderLabels(["제품명", "수량","가격"])
        #self.Table.setColumnWidth(1, 80)
        #self.Table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        #self.Table.horizontalHeader().setStretchLastSection(True)
        #header = self.Table.horizontalHeader()
        #header.resizeSection(0, 200)
        #header.resizeSection(1, 200)
        #header.resizeSection(2, 200)

        font = self.Table.font()
        font.setPointSize(20)
        font.setFamily('한컴산뜻돋움')
        font.setBold(True)
        self.Table.setFont(font)

        btn_Cancel = QPushButton()
        btn_Cancel.setText(' 상품 취소 ')
        font = btn_Cancel.font()
        font.setPointSize(30)
        font.setFamily('한컴산뜻돋움')
        font.setBold(True)
        btn_Cancel.setFont(font)
        btn_Cancel.setStyleSheet("color: #6633CC;"
                      "border-style: solid;"
                      "border-width: 5px;"
                      "border-color: #33CCCC;"
                      "background-color: #C8FFD4")

        
        btn_ON = QPushButton()
        btn_ON.setText(' Tracking ON ')
        font = btn_ON.font()
        font.setPointSize(30)
        font.setFamily('한컴산뜻돋움')
        font.setBold(True)
        btn_ON.setFont(font)
        btn_ON.setStyleSheet("color: #6633CC;"
                      "border-style: solid;"
                      "border-width: 5px;"
                      "border-color: #33CCCC;"
                      "background-color: #C8FFD4")
        
        btn_OFF = QPushButton()
        btn_OFF.setText(' Tracking OFF ')
        font = btn_OFF.font()
        font.setPointSize(30)
        font.setFamily('한컴산뜻돋움')
        font.setBold(True)
        btn_OFF.setFont(font)
        btn_OFF.setStyleSheet("color: #6633CC;"
                      "border-style: solid;"
                      "border-width: 5px;"
                      "border-color: #33CCCC;"
                      "background-color: #C8FFD4")
        
        btnM = QPushButton()
        btnM.setText(' 길 안내 모드 ')
        font = btnM.font()
        font.setPointSize(30)
        font.setFamily('한컴산뜻돋움')
        font.setBold(True)
        btnM.setFont(font)
        btnM.setStyleSheet("color: #6633CC;"
                      "border-style: solid;"
                      "border-width: 5px;"
                      "border-color: #33CCCC;"
                      "background-color: #C8FFD4")
        
        btnR = QPushButton()
        btnR.setText(' 결제 ')
        font = btnR.font()
        font.setPointSize(30)
        font.setFamily('한컴산뜻돋움')
        font.setBold(True)
        btnR.setFont(font)
        btnR.setStyleSheet("color: #6633CC;"
                      "border-style: solid;"
                      "border-width: 5px;"
                      "border-color: #33CCCC;"
                      "background-color: #C8FFD4")

        vbox_1 = QVBoxLayout()
        vbox_1.addWidget(label_P)
        vbox_1.addWidget(self.Table)
        vbox_1.addWidget(self.label_total)

        vbox_3 = QVBoxLayout()
        vbox_3.addWidget(btn_Cancel)
        vbox_3.addWidget(btn_ON)
        vbox_3.addWidget(btn_OFF)
        vbox_3.addWidget(btnM)
        vbox_3.addWidget(btnR)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox_1)
        hbox.addLayout(vbox_3)

        self.Widget_Shopping.setLayout(hbox)

        self.Widget_Shopping.setWindowTitle('쇼핑중')
        self.Widget_Shopping.showFullScreen()
        
        btn_Cancel.clicked.connect(self.Map)
        btnM.clicked.connect(self.Map)
        btnR.clicked.connect(self.RFID)
        btn_ON.clicked.connect(self.Tracking)
        
        Activate_Scanner()     # 바코드 스캐너 활성화

        

#############################################################
  

## 
    def Tracking(self):

        
        self.Table.setItem(0,0,QTableWidgetItem("바나나맛우유"))
        self.Table.setItem(0,1,QTableWidgetItem("1"))
        self.Table.setItem(0,2,QTableWidgetItem("1400"))
      
        self.Table.repaint()
        

#############################################################


    def Map(self):
        self.dialog_Map = QDialog()

        pixmap = QPixmap('Map_mart.png')   
        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        
        btnB = QPushButton(self.dialog_Map)
        btnB.setText(' <- ')
        btnB.setFont(QFont('Times', 30))

        hBbox = QHBoxLayout()
        hBbox.addStretch(1)
        hBbox.addWidget(btnB)

        hMbox = QHBoxLayout()
        hMbox.addStretch(1)
        hMbox.addWidget(lbl_img)
        hMbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addLayout(hBbox)
        vbox.addLayout(hMbox)
        vbox.addStretch(1)

        self.dialog_Map.setLayout(vbox)

        self.dialog_Map.setWindowTitle('마트 지도')
        self.dialog_Map.showFullScreen()

        btnB.clicked.connect(self.Auto_Back3)


#############################################################


## 결제 버튼 선택시 ( RFID )
    def RFID(self):

        self.dialog_RFID = QDialog()

        

        lbl_img = QLabel()
        lbl_img.resize(50,50)
        pixmap = QPixmap('RFID.png') 
        lbl_img.setPixmap(QPixmap(pixmap))

        label_0 = QLabel()

        label_1 = QLabel('그림과 같이 카드를 올려주세요.')
        font = label_1.font()
        font.setPointSize(30)
        font.setFamily('Times New Roman')
        font.setBold(True)
        label_1.setFont(font)

        btnB = QPushButton(self.dialog_RFID)
        btnB.setText(' <- ')
        btnB.setFont(QFont('Times', 30)) 

        btnR = QPushButton(self.dialog_RFID)
        btnR.setText(' 결제하기 ')
        btnR.setFont(QFont('Times', 30)) 

        label_2 = QLabel('현재 잔액 : 10000')
        font = label_2.font()
        font.setPointSize(30)
        font.setFamily('Times New Roman')
        font.setBold(True)
        label_2.setFont(font)

        label_3 = QLabel('결제 금액 : 6500')
        font = label_3.font()
        font.setPointSize(30)
        font.setFamily('Times New Roman')
        font.setBold(True)
        label_3.setFont(font)

        label_4 = QLabel('결제 후 잔액 : 3500')
        font = label_4.font()
        font.setPointSize(30)
        font.setFamily('Times New Roman')
        font.setBold(True)
        label_4.setFont(font)


        grid_1 = QGridLayout()
        grid_2 = QGridLayout()
        
        grid_2.addWidget(label_2,0,0)
        grid_2.addWidget(label_3,1,0)
        grid_2.addWidget(label_4,3,0)
        grid_2.addWidget(btnR,4,0)

        #grid_1.addWidget(label_0,0,1)
        grid_1.addWidget(lbl_img,1,0)
        grid_1.addWidget(label_1,2,0)
        grid_1.addWidget(btnB,0,3)
        grid_1.addLayout(grid_2,1,2)



        #vbox_1 = QVBoxLayout()
        #vbox_1.addWidget(lbl_img)
        #vbox_1.addWidget(label_1)
#
        #vbox_2 = QVBoxLayout()
        #vbox_2.addWidget(btnB)
        #vbox_2.addWidget(label_2)
        #vbox_2.addWidget(btnR)
#
        #hbox = QHBoxLayout()
        #hbox.addLayout(vbox_1)
        #hbox.addLayout(vbox_2)

        self.dialog_RFID.setLayout(grid_1)

        self.dialog_RFID.setWindowTitle('RFID')
        self.dialog_RFID.showFullScreen()

        ## <- 버튼 누르면
        btnB.clicked.connect(self.Auto_Back4)
        
        btnR.clicked.connect(self.Payment)


#############################################################


    def Payment(self):
        self.dialog_Payment = QDialog()

        self.label_P = QLabel('결제가 완료되었습니다.\n    안녕히가세요..')
        font = self.label_P.font()
        font.setPointSize(30)
        font.setFamily('Times New Roman')
        font.setBold(True)
        self.label_P.setFont(font)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label_P)
        hbox.addStretch(1)

        self.dialog_Payment.setLayout(hbox)

        self.dialog_Payment.setWindowTitle('progress')
        self.dialog_Payment.showFullScreen()

        QTest.qWait(1000)

        QTest.qWait(1000)

        #self.Widget_Shopping.close()
        #global running
        #running = False
        #self.dialog_RFID.close()
        #self.dialog_Payment.close()
        #self.close()
        #self.ex = first()
        


#############################################################


    def Payment_Completed(self):
        self.Completed = QDialog()

        label = QLabel('결제 진행중 입니다.')
        font = label.font()
        font.setPointSize(30)
        font.setFamily('Times New Roman')
        font.setBold(True)
        label.setFont(font)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(label)
        hbox.addStretch(1)

        self.Completed.setLayout(hbox)

        self.Completed.setWindowTitle('progress')
        self.Completed.showFullScreen()

        QTest.qWait(1000)


#############################################################


## Tarcking_ON 버튼 선택시
    def Auto_Start(self):
        self.dialog_Camera = QDialog()

        label1 = QLabel('5초 후에 사용자 인식이 시작됩니다.\n            카트 앞에 서주세요.', self.dialog_Camera)
        font1 = label1.font()
        font1.setPointSize(30)
        font1.setFamily('Times New Roman')
        font1.setBold(True)
        label1.setFont(font1)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(label1)
        hbox.addStretch(1)
        self.dialog_Camera.setLayout(hbox)

        self.dialog_Camera.setWindowTitle('카메라 인식')
        self.dialog_Camera.showFullScreen()

        QTest.qWait(1000)
        
        self.dialog_Camera.close()  # 5초후 인식 설명창 닫기


#############################################################


## <- 버튼 선택시 (Dialog Map 나가기)
    def Auto_Back3(self):
        self.dialog_Map.close()

        
#############################################################


## <- 버튼 선택시 (Dialog RFID 나가기)
    def Auto_Back4(self):
        self.dialog_RFID.close()



#############################################################
#############################################################
#############################################################

## 나가기
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    palette = QtGui.QPalette()
    palette.setColor(QPalette.Window, QColor(255, 255, 255))
    #palette.setColor(QPalette.WindowText, Qt.white)
    #palette.setColor(QPalette.Base, QColor(25, 25, 25))
    #palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    #palette.setColor(QPalette.ToolTipBase, Qt.white)
    #palette.setColor(QPalette.ToolTipText, Qt.white)
    #palette.setColor(QPalette.Text, Qt.white)
    #palette.setColor(QPalette.Button, QColor(53, 53, 53))
    #palette.setColor(QPalette.ButtonText, Qt.white)
    #palette.setColor(QPalette.BrightText, Qt.red)
    #palette.setColor(QPalette.Link, QColor(42, 130, 218))
    #palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    #palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    ex = first()
    sys.exit(app.exec_())