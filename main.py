# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
import requests
import generate_ActiveSig_PB as generate
import config

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        self.frimestate = 0
        self.previous_run = []
        self.txSave = {'posX': 0, 'posY': 0}
        self.rxSave = {'posX': 0, 'posY': 0}
        self.targetSave = {'posX': 0, 'posY': 0}
        self.checking_option = 0

        widgets.horizontalScrollBar_Target.setValue(0)
        widgets.horizontalScrollBar_Tx.setValue(0)
        widgets.horizontalScrollBar_Rx.setValue(0)
        widgets.horizontalScrollBar_Target.valueChanged.connect(self.checkScroll)
        widgets.horizontalScrollBar_Tx.valueChanged.connect(self.checkScroll)
        widgets.horizontalScrollBar_Rx.valueChanged.connect(self.checkScroll)

        widgets.label.setPixmap(QPixmap("./images/images/picture.png"))
        widgets.passive_btn.setChecked(True)

        widgets.active_or_passive_setting.setCurrentWidget(widgets.passive_page)
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "PyQt GUI"
        description = "Sonobuoy MAP GUI"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        # widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick) # main page - stack0

        widgets.btn_setting.clicked.connect(self.buttonClick) # param setting layout - stack1
        widgets.sendBtn.clicked.connect(self.buttonClick) # 파라미터 전송 - function3

        widgets.btn_map.clicked.connect(self.buttonClick) # map layout - stack2
        widgets.btn_widgets.clicked.connect(self.buttonClick) # 라벨 생성 - function1
        widgets.btn_kill.clicked.connect(self.buttonClick) # 라벨 지우기 - function2

        widgets.btn_information.clicked.connect(self.buttonClick) # wav, graph layout - stack3

        widgets.btn_index.clicked.connect(self.buttonClick) # index layout - stack4
        widgets.btn_index_2.clicked.connect(self.buttonClick) # index layout - stack5
        widgets.btn_index_3.clicked.connect(self.buttonClick) # index layout - stack6
        widgets.btn_index_4.clicked.connect(self.buttonClick) # index layout - stack7

        widgets.active_btn.clicked.connect(self.checkRadio)
        widgets.passive_btn.clicked.connect(self.checkRadio)
        
        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////

    # Active or Passive setting
    def checkRadio(self):
        if widgets.active_btn.isChecked():
            self.checking_option = 1
            widgets.active_or_passive_setting.setCurrentWidget(widgets.active_page)
        else:
            self.checking_option = 0
            widgets.active_or_passive_setting.setCurrentWidget(widgets.passive_page)
    
    # tx, rx, target scroll bar - z pos
    def checkScroll(self):
        widgets.Target_depth_value.setText("Target " + str(widgets.horizontalScrollBar_Target.value()))
        widgets.Tx_depth_value.setText("Tx " + str(widgets.horizontalScrollBar_Tx.value()))
        widgets.Rx_depth_value.setText("Rx " + str(widgets.horizontalScrollBar_Rx.value()))
        
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # 메인 홈 페이지
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

            self.labelSetHidden()


        # 설정 페이지
        if btnName == "btn_setting":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

            self.labelSetHidden()

        # 맵 좌표 이동시키기 - stack 1 function 1
        # if btnName == "settingBtn":
        #     BASE_URL = 'https://maps.googleapis.com/maps/api/staticmap?'
        #     API_KEY  = config.api_key
        #     POS = widgets.areaEdit.text() + ',' + widgets.areaEdit_2.text()
        #     URL = (BASE_URL 
        #     + f'center={POS}'
        #     + f'&zoom=6'
        #     + f'&size={1200}x{800}&scale=2'
        #     + f'&maptype=satellite'
        #     + f'&key={API_KEY}')
            
        #     r = requests.get(URL)
        #     file = open("./images/images/picture2.png","wb")
        #     file.write(r.content)
        #     file.close()
        #     widgets.label.setPixmap(QPixmap("./images/images/picture2.png"))
        #     widgets.currentArea.setText('현재 좌표 : (' + widgets.areaEdit.text() + ',' + widgets.areaEdit_2.text() + ')')

        # tx, rx, target 파라미터 전송과 맵 표시 - stack 1 function 2
        # if btnName == "txBtn":
        #     if self.txSave['label']:
        #         self.txSave['label'].close()
        #         self.txSave.clear()

        #     self.label = QLabel(self)
        #     self.label.setGeometry(int(widgets.txXEdit.text()), int(widgets.txYEdit.text()), 16, 16)
        #     pixmap = QPixmap("./images/icons/cil-cursor.png")
        #     self.label.setPixmap(pixmap)
        #     self.txSave = {'label':self.label, 'posX':int(widgets.txXEdit.text()), 'posY':int(widgets.txYEdit.text())}
        #     self.label.show()
        #     self.label.close()

        # if btnName == "rxBtn":
        #     if self.rxSave['label']:
        #         self.rxSave['label'].close()
        #         self.rxSave.clear()

        #     self.label = QLabel(self)
        #     self.label.setGeometry(int(widgets.rxXEdit.text()), int(widgets.rxYEdit.text()), 16, 16)
        #     pixmap = QPixmap("./images/icons/cil-wifi-signal-4.png")
        #     self.label.setPixmap(pixmap)
        #     self.rxSave = {'label':self.label, 'posX':int(widgets.rxXEdit.text()), 'posY':int(widgets.rxYEdit.text())}
        #     self.label.show()
        #     self.label.close()

        # if btnName == "targetBtn":
        #     if self.targetSave['label']:
        #         self.targetSave['label'].close()
        #         self.targetSave.clear()

        #     self.label = QLabel(self)
        #     self.label.setGeometry(int(widgets.targetXEdit.text()), int(widgets.targetYEdit.text()), 16, 16)
        #     pixmap = QPixmap("./images/icons/cil-wifi-signal-0.png")
        #     self.label.setPixmap(pixmap)
        #     self.targetSave = {'label':self.label, 'posX':int(widgets.targetXEdit.text()), 'posY':int(widgets.targetYEdit.text())}
        #     self.label.show()
        #     self.label.close()

        # 파라미터 보내기
        if btnName == "sendBtn":
            if self.checking_option == 0:
                self.paramList = {
                'tx' :[self.txSave['posX'], self.txSave['posY'], widgets.horizontalScrollBar_Tx.value()],
                'rx' :[self.rxSave['posX'], self.rxSave['posY'], widgets.horizontalScrollBar_Rx.value()],
                'target' :[self.targetSave['posX'], self.targetSave['posY'], widgets.horizontalScrollBar_Target.value()],
                'type' : widgets.passive_type_edit.text(), 'centerFreq' : widgets.passive_freq_edit.text()
                }
                widgets.outputPulse.setText('Pulse(Passive) type :' + widgets.passive_type_edit.text() + ', centerfrequncy :' + widgets.passive_freq_edit.text())
            else:
                self.paramList = {
                'tx' :[self.txSave['posX'], self.txSave['posY'], widgets.horizontalScrollBar_Tx.value()],
                'rx' :[self.rxSave['posX'], self.rxSave['posY'], widgets.horizontalScrollBar_Rx.value()],
                'target' :[self.targetSave['posX'], self.targetSave['posY'], widgets.horizontalScrollBar_Target.value()],
                'type' : widgets.active_type_edit.text(), 'centerFreq' : widgets.active_freq_edit.text(),
                'pulse' : widgets.active_pulse_edit.text(), 'bandwidth' : widgets.active_band_edit.text()
                }
                widgets.outputPulse.setText('Pulse(Active) type :' + widgets.active_type_edit.text() + ', centerfrequncy :' + widgets.active_freq_edit.text() + ', pulse :' + widgets.active_pulse_edit.text() + ', bandwidth :' + widgets.active_band_edit.text())
            print(self.paramList)

            # generate.main(self.paramList)

            widgets.outputTx.setText('Tx Pos(x, y, z) : ' + str(self.txSave['posX']) + ', ' + str(self.txSave['posY']) + ', ' + str(widgets.horizontalScrollBar_Tx.value()))
            widgets.outputRx.setText('Rx Pos(x, y, z) : ' + str(self.rxSave['posX']) + ', ' + str(self.rxSave['posY']) + ', ' + str(widgets.horizontalScrollBar_Rx.value()))
            widgets.outputTarget.setText('Target Pos(x, y, z) : ' + str(self.targetSave['posX']) + ', ' + str(self.targetSave['posY']) + ', ' + str(widgets.horizontalScrollBar_Target.value()))

            # widgets.label_spec.setPixmap(QPixmap("./Spec.png").scaled(self.width(), self.height()))
            # widgets.label_soundpath.setPixmap(QPixmap("./soundpath.png").scaled(self.width(), self.height()))
            # widgets.label_wav.setPixmap(QPixmap("./wav.png").scaled(self.width(), self.height()))
            # widgets.label_spec.setScaledContents(True)
            # widgets.label_soundpath.setScaledContents(True)
            # widgets.label_wav.setScaledContents(True)

        # 맵 페이지
        if btnName == "btn_map":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
            widgets.btn_widgets.setEnabled(True)
            if 'label' in self.txSave:
                self.txSave['label'].setHidden(False)
            if 'label' in self.rxSave:
                self.rxSave['label'].setHidden(False)
            if 'label' in self.targetSave:
                self.targetSave['label'].setHidden(False)

        # 맵 페이지에 아이콘라벨 입히기
        if btnName == "btn_widgets":
            if self.frimestate == 1:
                self.frimestate = 0
                widgets.btn_widgets.setStyleSheet("background-image: url(:/icons/images/icons/cil-wifi-signal-off.png);")
                
            else:
                self.frimestate = 1
                widgets.btn_widgets.setStyleSheet("background-image: url(:/icons/images/icons/cil-wifi-signal-0.png);")
                if 'label' in self.txSave:
                    self.txSave['label'].setHidden(False)
                if 'label' in self.rxSave:
                    self.rxSave['label'].setHidden(False)
                if 'label' in self.targetSave:
                    self.targetSave['label'].setHidden(False)

        # 아이콘라벨 모두 죽이기
        if btnName == "btn_kill":
            if 'label' in self.txSave:
                self.txSave['label'].close()
                self.txSave.clear()
                self.txSave = {'posX': 0, 'posY': 0}
            if 'label' in self.rxSave:
                self.rxSave['label'].close()
                self.rxSave.clear()
                self.rxSave = {'posX': 0, 'posY': 0}
            if 'label' in self.targetSave:
                self.targetSave['label'].close()
                self.targetSave.clear()
                self.targetSave = {'posX': 0, 'posY': 0}

        # 정보 확인 페이지
        if btnName == "btn_information":
            if self.checking_option == 0:
                widgets.outputPulse.setText('Pulse(Passive) type :' + widgets.passive_type_edit.text() + ', centerfrequncy :' + widgets.passive_freq_edit.text())
            else:
                widgets.outputPulse.setText('Pulse(Active) type :' + widgets.active_type_edit.text() + ', centerfrequncy :' + widgets.active_freq_edit.text() + ', pulse :' + widgets.active_pulse_edit.text() + ', bandwidth :' + widgets.active_band_edit.text())

            widgets.outputTx.setText('Tx Pos(x, y, z) : ' + str(self.txSave['posX']) + ', ' + str(self.txSave['posY']) + ', ' + str(widgets.horizontalScrollBar_Tx.value()))
            widgets.outputRx.setText('Rx Pos(x, y, z) : ' + str(self.rxSave['posX']) + ', ' + str(self.rxSave['posY']) + ', ' + str(widgets.horizontalScrollBar_Rx.value()))
            widgets.outputTarget.setText('Target Pos(x, y, z) : ' + str(self.targetSave['posX']) + ', ' + str(self.targetSave['posY']) + ', ' + str(widgets.horizontalScrollBar_Target.value()))
            widgets.stackedWidget.setCurrentWidget(widgets.show)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            widgets.btn_information.setEnabled(True)
            
            self.labelSetHidden()

        # 그래프 페이지
        if btnName == "btn_index":
            widgets.stackedWidget.setCurrentWidget(widgets.plot1_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            widgets.btn_index.setEnabled(True)
            
            self.labelSetHidden()

        if btnName == "btn_index_2":
            widgets.stackedWidget.setCurrentWidget(widgets.plot2_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            widgets.btn_index_2.setEnabled(True)
            
            self.labelSetHidden()
        
        if btnName == "btn_index_3":
            widgets.stackedWidget.setCurrentWidget(widgets.plot3_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            widgets.btn_index_3.setEnabled(True)
            
            self.labelSetHidden()

        if btnName == "btn_index_4":
            widgets.stackedWidget.setCurrentWidget(widgets.plot4_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            widgets.btn_index_4.setEnabled(True)
            
            self.labelSetHidden()

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')
    
    # 화면 전환시 라벨 숨기기
    def labelSetHidden(self):
        self.frimestate = 0
        widgets.btn_widgets.setStyleSheet("background-image: url(:/icons/images/icons/cil-wifi-signal-off.png);")
        widgets.btn_widgets.setDisabled(True)

        if 'label' in self.txSave:
            self.txSave['label'].setHidden(True)
        if 'label' in self.rxSave:
            self.rxSave['label'].setHidden(True)
        if 'label' in self.targetSave:
            self.targetSave['label'].setHidden(True)

    def mouseMoveEvent(self, event):
        # MOVE WINDOW
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()     

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # 마우스 좌클릭시 TX 아이콘 띄우기
        if event.buttons() == Qt.LeftButton and self.frimestate == 1:
            if 'label' in self.txSave:
                self.txSave['label'].close()
                self.txSave.clear()

            self.label = QLabel(self)
            self.label.setGeometry(event.pos().x(), event.pos().y(), 16, 16)
            pixmap = QPixmap("./images/icons/cil-cursor.png")
            self.label.setPixmap(pixmap)
            self.label.show()
            self.txSave = {'label':self.label, 'posX':event.pos().x(), 'posY':event.pos().y()}
            print(self.txSave)
        
        # 마우스 우클릭시 RX 아이콘 띄우기
        if event.buttons() == Qt.RightButton and self.frimestate == 1:
            if 'label' in self.rxSave:
                self.rxSave['label'].close()
                self.rxSave.clear()

            self.label = QLabel(self)
            self.label.setGeometry(event.pos().x(), event.pos().y(), 16, 16)
            pixmap = QPixmap("./images/icons/cil-wifi-signal-4.png")
            self.label.setPixmap(pixmap)
            self.label.show()
            self.rxSave = {'label':self.label, 'posX':event.pos().x(), 'posY':event.pos().y()}
        
        # 마우스 중간클릭시 타겟 아이콘 띄우기
        if event.buttons() == Qt.MiddleButton and self.frimestate == 1:
            if 'label' in self.targetSave:
                self.targetSave['label'].close()
                self.targetSave.clear()
            self.label = QLabel(self)
            self.label.setGeometry(event.pos().x(), event.pos().y(), 16, 16)
            pixmap = QPixmap("./images/icons/cil-wifi-signal-0.png")
            self.label.setPixmap(pixmap)
            self.label.show()
            self.targetSave = {'label':self.label, 'posX':event.pos().x(), 'posY':event.pos().y()}

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("sono.ico"))
    window = MainWindow()
    sys.exit(app.exec_())