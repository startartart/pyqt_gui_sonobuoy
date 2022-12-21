# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QScrollBar,
    QSizePolicy, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1088, 759)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout_27 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setEnabled(True)
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"background-image: url(:/images/images/images/sono.jpg);\n"
"background-position: centered;\n"
"background-repeat: no-repeat;")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.topMenu)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_home = QVBoxLayout()
        self.verticalLayout_home.setSpacing(0)
        self.verticalLayout_home.setObjectName(u"verticalLayout_home")
        self.groupBox = QGroupBox(self.topMenu)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.groupBox)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);\n"
"")

        self.verticalLayout_7.addWidget(self.btn_home)


        self.verticalLayout_home.addWidget(self.groupBox)


        self.verticalLayout_23.addLayout(self.verticalLayout_home)

        self.verticalLayout_map = QVBoxLayout()
        self.verticalLayout_map.setSpacing(0)
        self.verticalLayout_map.setObjectName(u"verticalLayout_map")
        self.groupBox_2 = QGroupBox(self.topMenu)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btn_map = QPushButton(self.groupBox_2)
        self.btn_map.setObjectName(u"btn_map")
        sizePolicy.setHeightForWidth(self.btn_map.sizePolicy().hasHeightForWidth())
        self.btn_map.setSizePolicy(sizePolicy)
        self.btn_map.setMinimumSize(QSize(0, 45))
        self.btn_map.setFont(font)
        self.btn_map.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_map.setLayoutDirection(Qt.LeftToRight)
        self.btn_map.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-map.png);")

        self.verticalLayout_13.addWidget(self.btn_map)

        self.btn_widgets = QPushButton(self.groupBox_2)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-wifi-signal-off.png);\n"
"")

        self.verticalLayout_13.addWidget(self.btn_widgets)

        self.btn_kill = QPushButton(self.groupBox_2)
        self.btn_kill.setObjectName(u"btn_kill")
        sizePolicy.setHeightForWidth(self.btn_kill.sizePolicy().hasHeightForWidth())
        self.btn_kill.setSizePolicy(sizePolicy)
        self.btn_kill.setMinimumSize(QSize(0, 45))
        self.btn_kill.setFont(font)
        self.btn_kill.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_kill.setLayoutDirection(Qt.LeftToRight)
        self.btn_kill.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_13.addWidget(self.btn_kill)


        self.verticalLayout_map.addWidget(self.groupBox_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_23.addLayout(self.verticalLayout_map)

        self.verticalLayout_setting = QVBoxLayout()
        self.verticalLayout_setting.setObjectName(u"verticalLayout_setting")
        self.groupBox_3 = QGroupBox(self.topMenu)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_setting = QPushButton(self.groupBox_3)
        self.btn_setting.setObjectName(u"btn_setting")
        sizePolicy.setHeightForWidth(self.btn_setting.sizePolicy().hasHeightForWidth())
        self.btn_setting.setSizePolicy(sizePolicy)
        self.btn_setting.setMinimumSize(QSize(0, 45))
        self.btn_setting.setFont(font)
        self.btn_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_setting.setLayoutDirection(Qt.LeftToRight)
        self.btn_setting.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-settings.png);\n"
"\n"
"")

        self.verticalLayout_14.addWidget(self.btn_setting)


        self.verticalLayout_setting.addWidget(self.groupBox_3)


        self.verticalLayout_23.addLayout(self.verticalLayout_setting)

        self.verticalLayout_plot = QVBoxLayout()
        self.verticalLayout_plot.setObjectName(u"verticalLayout_plot")
        self.groupBox_4 = QGroupBox(self.topMenu)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 10)
        self.btn_index = QPushButton(self.groupBox_4)
        self.btn_index.setObjectName(u"btn_index")
        sizePolicy.setHeightForWidth(self.btn_index.sizePolicy().hasHeightForWidth())
        self.btn_index.setSizePolicy(sizePolicy)
        self.btn_index.setMinimumSize(QSize(0, 45))
        self.btn_index.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_index.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-link.png);")

        self.verticalLayout_22.addWidget(self.btn_index)

        self.plot1 = QLabel(self.groupBox_4)
        self.plot1.setObjectName(u"plot1")
        self.plot1.setStyleSheet(u"font-size:10px;")

        self.verticalLayout_22.addWidget(self.plot1, 0, Qt.AlignHCenter)

        self.btn_index_2 = QPushButton(self.groupBox_4)
        self.btn_index_2.setObjectName(u"btn_index_2")
        sizePolicy.setHeightForWidth(self.btn_index_2.sizePolicy().hasHeightForWidth())
        self.btn_index_2.setSizePolicy(sizePolicy)
        self.btn_index_2.setMinimumSize(QSize(0, 45))
        self.btn_index_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_index_2.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-link.png);")

        self.verticalLayout_22.addWidget(self.btn_index_2)

        self.plot2 = QLabel(self.groupBox_4)
        self.plot2.setObjectName(u"plot2")
        self.plot2.setStyleSheet(u"font-size:10px;")

        self.verticalLayout_22.addWidget(self.plot2, 0, Qt.AlignHCenter)

        self.btn_index_3 = QPushButton(self.groupBox_4)
        self.btn_index_3.setObjectName(u"btn_index_3")
        sizePolicy.setHeightForWidth(self.btn_index_3.sizePolicy().hasHeightForWidth())
        self.btn_index_3.setSizePolicy(sizePolicy)
        self.btn_index_3.setMinimumSize(QSize(0, 45))
        self.btn_index_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_index_3.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-link.png);")

        self.verticalLayout_22.addWidget(self.btn_index_3)

        self.plot3 = QLabel(self.groupBox_4)
        self.plot3.setObjectName(u"plot3")
        self.plot3.setStyleSheet(u"font-size:10px;")

        self.verticalLayout_22.addWidget(self.plot3, 0, Qt.AlignHCenter)

        self.btn_index_4 = QPushButton(self.groupBox_4)
        self.btn_index_4.setObjectName(u"btn_index_4")
        sizePolicy.setHeightForWidth(self.btn_index_4.sizePolicy().hasHeightForWidth())
        self.btn_index_4.setSizePolicy(sizePolicy)
        self.btn_index_4.setMinimumSize(QSize(0, 45))
        self.btn_index_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_index_4.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-link.png);")

        self.verticalLayout_22.addWidget(self.btn_index_4)

        self.plot4 = QLabel(self.groupBox_4)
        self.plot4.setObjectName(u"plot4")
        self.plot4.setStyleSheet(u"font-size:10px;")

        self.verticalLayout_22.addWidget(self.plot4, 0, Qt.AlignHCenter)


        self.verticalLayout_plot.addWidget(self.groupBox_4)


        self.verticalLayout_23.addLayout(self.verticalLayout_plot)

        self.verticalLayout_check = QVBoxLayout()
        self.verticalLayout_check.setObjectName(u"verticalLayout_check")
        self.groupBox_5 = QGroupBox(self.topMenu)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_24 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.btn_information = QPushButton(self.groupBox_5)
        self.btn_information.setObjectName(u"btn_information")
        sizePolicy.setHeightForWidth(self.btn_information.sizePolicy().hasHeightForWidth())
        self.btn_information.setSizePolicy(sizePolicy)
        self.btn_information.setMinimumSize(QSize(0, 45))
        self.btn_information.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_information.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-magnifying-glass.png);")

        self.verticalLayout_24.addWidget(self.btn_information)


        self.verticalLayout_check.addWidget(self.groupBox_5)


        self.verticalLayout_23.addLayout(self.verticalLayout_check)


        self.verticalMenuLayout.addWidget(self.topMenu)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setMinimumSize(QSize(1178, 0))
        self.home.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.home)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.home_label = QLabel(self.home)
        self.home_label.setObjectName(u"home_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.home_label.sizePolicy().hasHeightForWidth())
        self.home_label.setSizePolicy(sizePolicy3)
        self.home_label.setStyleSheet(u"font-size:30px;")

        self.verticalLayout_8.addWidget(self.home_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.passive_btn = QRadioButton(self.home)
        self.passive_btn.setObjectName(u"passive_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.passive_btn.sizePolicy().hasHeightForWidth())
        self.passive_btn.setSizePolicy(sizePolicy4)
        self.passive_btn.setStyleSheet(u"font-size:25px;")

        self.horizontalLayout_7.addWidget(self.passive_btn, 0, Qt.AlignHCenter)

        self.active_btn = QRadioButton(self.home)
        self.active_btn.setObjectName(u"active_btn")
        sizePolicy4.setHeightForWidth(self.active_btn.sizePolicy().hasHeightForWidth())
        self.active_btn.setSizePolicy(sizePolicy4)
        self.active_btn.setStyleSheet(u"font-size:25px;")

        self.horizontalLayout_7.addWidget(self.active_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, -1, -1, 20)
        self.home_image_label = QLabel(self.home)
        self.home_image_label.setObjectName(u"home_image_label")
        sizePolicy3.setHeightForWidth(self.home_image_label.sizePolicy().hasHeightForWidth())
        self.home_image_label.setSizePolicy(sizePolicy3)
        self.home_image_label.setStyleSheet(u"background-image: url(:/images/images/images/picture.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")

        self.gridLayout_6.addWidget(self.home_image_label, 0, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_6)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(2, 6)

        self.gridLayout_3.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home)
        self.show = QWidget()
        self.show.setObjectName(u"show")
        self.gridLayout_5 = QGridLayout(self.show)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.show)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 20))
        self.label_2.setMaximumSize(QSize(100, 20))

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_wav = QLabel(self.show)
        self.label_wav.setObjectName(u"label_wav")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_wav.sizePolicy().hasHeightForWidth())
        self.label_wav.setSizePolicy(sizePolicy5)
        self.label_wav.setMinimumSize(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.label_wav)


        self.gridLayout_4.addLayout(self.verticalLayout_4, 1, 1, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_4 = QLabel(self.show)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 20))
        self.label_4.setMaximumSize(QSize(100, 20))

        self.verticalLayout_16.addWidget(self.label_4)

        self.label_spec = QLabel(self.show)
        self.label_spec.setObjectName(u"label_spec")
        sizePolicy5.setHeightForWidth(self.label_spec.sizePolicy().hasHeightForWidth())
        self.label_spec.setSizePolicy(sizePolicy5)
        self.label_spec.setMinimumSize(QSize(0, 0))

        self.verticalLayout_16.addWidget(self.label_spec)


        self.gridLayout_4.addLayout(self.verticalLayout_16, 1, 2, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_3 = QLabel(self.show)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 20))
        self.label_3.setMaximumSize(QSize(100, 20))

        self.verticalLayout_18.addWidget(self.label_3)

        self.label_soundpath = QLabel(self.show)
        self.label_soundpath.setObjectName(u"label_soundpath")
        sizePolicy5.setHeightForWidth(self.label_soundpath.sizePolicy().hasHeightForWidth())
        self.label_soundpath.setSizePolicy(sizePolicy5)
        self.label_soundpath.setMinimumSize(QSize(0, 0))

        self.verticalLayout_18.addWidget(self.label_soundpath)


        self.gridLayout_4.addLayout(self.verticalLayout_18, 3, 2, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.outputStatus = QLabel(self.show)
        self.outputStatus.setObjectName(u"outputStatus")

        self.verticalLayout_19.addWidget(self.outputStatus)

        self.outputTx = QLabel(self.show)
        self.outputTx.setObjectName(u"outputTx")

        self.verticalLayout_19.addWidget(self.outputTx)

        self.outputRx = QLabel(self.show)
        self.outputRx.setObjectName(u"outputRx")

        self.verticalLayout_19.addWidget(self.outputRx)

        self.outputTarget = QLabel(self.show)
        self.outputTarget.setObjectName(u"outputTarget")

        self.verticalLayout_19.addWidget(self.outputTarget)

        self.outputPulse = QLabel(self.show)
        self.outputPulse.setObjectName(u"outputPulse")

        self.verticalLayout_19.addWidget(self.outputPulse)


        self.gridLayout_4.addLayout(self.verticalLayout_19, 3, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.show)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widgets)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.setting_layout = QFrame(self.widgets)
        self.setting_layout.setObjectName(u"setting_layout")
        self.setting_layout.setMinimumSize(QSize(0, 150))
        self.setting_layout.setFrameShape(QFrame.StyledPanel)
        self.setting_layout.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.setting_layout)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.active_or_passive_setting = QStackedWidget(self.setting_layout)
        self.active_or_passive_setting.setObjectName(u"active_or_passive_setting")
        self.active_page = QWidget()
        self.active_page.setObjectName(u"active_page")
        self.verticalLayout_25 = QVBoxLayout(self.active_page)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_7 = QGroupBox(self.active_page)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_28 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.active_type_label = QLabel(self.groupBox_7)
        self.active_type_label.setObjectName(u"active_type_label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.active_type_label.sizePolicy().hasHeightForWidth())
        self.active_type_label.setSizePolicy(sizePolicy6)
        self.active_type_label.setMinimumSize(QSize(0, 0))
        self.active_type_label.setMaximumSize(QSize(500, 16777215))
        self.active_type_label.setStyleSheet(u"font-size:30px;")

        self.horizontalLayout_10.addWidget(self.active_type_label)

        self.active_type_edit = QComboBox(self.groupBox_7)
        self.active_type_edit.addItem("")
        self.active_type_edit.addItem("")
        self.active_type_edit.setObjectName(u"active_type_edit")
        self.active_type_edit.setMaximumSize(QSize(100, 16777215))
        self.active_type_edit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_10.addWidget(self.active_type_edit)


        self.verticalLayout_28.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.active_freq_label = QLabel(self.groupBox_7)
        self.active_freq_label.setObjectName(u"active_freq_label")
        sizePolicy6.setHeightForWidth(self.active_freq_label.sizePolicy().hasHeightForWidth())
        self.active_freq_label.setSizePolicy(sizePolicy6)
        self.active_freq_label.setMaximumSize(QSize(500, 16777215))
        self.active_freq_label.setStyleSheet(u"font-size:30px;")

        self.horizontalLayout_12.addWidget(self.active_freq_label)

        self.active_freq_edit = QComboBox(self.groupBox_7)
        self.active_freq_edit.addItem("")
        self.active_freq_edit.addItem("")
        self.active_freq_edit.addItem("")
        self.active_freq_edit.addItem("")
        self.active_freq_edit.addItem("")
        self.active_freq_edit.addItem("")
        self.active_freq_edit.setObjectName(u"active_freq_edit")
        self.active_freq_edit.setMaximumSize(QSize(100, 16777215))
        self.active_freq_edit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_12.addWidget(self.active_freq_edit)


        self.verticalLayout_28.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.active_pulse_label = QLabel(self.groupBox_7)
        self.active_pulse_label.setObjectName(u"active_pulse_label")
        sizePolicy6.setHeightForWidth(self.active_pulse_label.sizePolicy().hasHeightForWidth())
        self.active_pulse_label.setSizePolicy(sizePolicy6)
        self.active_pulse_label.setMaximumSize(QSize(500, 16777215))
        self.active_pulse_label.setStyleSheet(u"font-size:30px;")

        self.horizontalLayout_11.addWidget(self.active_pulse_label)

        self.active_pulse_edit = QComboBox(self.groupBox_7)
        self.active_pulse_edit.addItem("")
        self.active_pulse_edit.addItem("")
        self.active_pulse_edit.addItem("")
        self.active_pulse_edit.setObjectName(u"active_pulse_edit")
        self.active_pulse_edit.setMaximumSize(QSize(100, 16777215))
        self.active_pulse_edit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.active_pulse_edit)


        self.verticalLayout_28.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.active_band_label = QLabel(self.groupBox_7)
        self.active_band_label.setObjectName(u"active_band_label")
        sizePolicy6.setHeightForWidth(self.active_band_label.sizePolicy().hasHeightForWidth())
        self.active_band_label.setSizePolicy(sizePolicy6)
        self.active_band_label.setMaximumSize(QSize(500, 16777215))
        self.active_band_label.setStyleSheet(u"font-size:30px;")

        self.horizontalLayout_13.addWidget(self.active_band_label)

        self.active_band_edit = QComboBox(self.groupBox_7)
        self.active_band_edit.addItem("")
        self.active_band_edit.addItem("")
        self.active_band_edit.addItem("")
        self.active_band_edit.setObjectName(u"active_band_edit")
        self.active_band_edit.setMaximumSize(QSize(100, 16777215))
        self.active_band_edit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_13.addWidget(self.active_band_edit)


        self.verticalLayout_28.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_6.addWidget(self.groupBox_7)


        self.verticalLayout_25.addLayout(self.horizontalLayout_6)

        self.active_or_passive_setting.addWidget(self.active_page)
        self.passive_page = QWidget()
        self.passive_page.setObjectName(u"passive_page")
        self.verticalLayout_17 = QVBoxLayout(self.passive_page)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.groupBox_6 = QGroupBox(self.passive_page)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout = QVBoxLayout(self.groupBox_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.passive_type_label = QLabel(self.groupBox_6)
        self.passive_type_label.setObjectName(u"passive_type_label")
        sizePolicy6.setHeightForWidth(self.passive_type_label.sizePolicy().hasHeightForWidth())
        self.passive_type_label.setSizePolicy(sizePolicy6)
        self.passive_type_label.setMaximumSize(QSize(500, 50))
        self.passive_type_label.setStyleSheet(u"font-size:30px;")

        self.horizontalLayout_8.addWidget(self.passive_type_label)

        self.passive_type_edit = QComboBox(self.groupBox_6)
        self.passive_type_edit.addItem("")
        self.passive_type_edit.addItem("")
        self.passive_type_edit.setObjectName(u"passive_type_edit")
        self.passive_type_edit.setMaximumSize(QSize(100, 16777215))
        self.passive_type_edit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_8.addWidget(self.passive_type_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.passive_freq_label = QLabel(self.groupBox_6)
        self.passive_freq_label.setObjectName(u"passive_freq_label")
        sizePolicy6.setHeightForWidth(self.passive_freq_label.sizePolicy().hasHeightForWidth())
        self.passive_freq_label.setSizePolicy(sizePolicy6)
        self.passive_freq_label.setMaximumSize(QSize(500, 50))
        self.passive_freq_label.setStyleSheet(u"font-size:30px;")

        self.horizontalLayout_9.addWidget(self.passive_freq_label)

        self.passive_freq_edit = QComboBox(self.groupBox_6)
        self.passive_freq_edit.addItem("")
        self.passive_freq_edit.addItem("")
        self.passive_freq_edit.addItem("")
        self.passive_freq_edit.addItem("")
        self.passive_freq_edit.addItem("")
        self.passive_freq_edit.addItem("")
        self.passive_freq_edit.addItem("")
        self.passive_freq_edit.addItem("")
        self.passive_freq_edit.addItem("")
        self.passive_freq_edit.addItem("")
        self.passive_freq_edit.addItem("")
        self.passive_freq_edit.addItem("")
        self.passive_freq_edit.addItem("")
        self.passive_freq_edit.addItem("")
        self.passive_freq_edit.addItem("")
        self.passive_freq_edit.setObjectName(u"passive_freq_edit")
        self.passive_freq_edit.setMaximumSize(QSize(100, 16777215))
        self.passive_freq_edit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_9.addWidget(self.passive_freq_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.verticalLayout_21.addWidget(self.groupBox_6)


        self.verticalLayout_17.addLayout(self.verticalLayout_21)

        self.active_or_passive_setting.addWidget(self.passive_page)

        self.verticalLayout_26.addWidget(self.active_or_passive_setting)

        self.generate_layout = QHBoxLayout()
        self.generate_layout.setObjectName(u"generate_layout")
        self.progressBar = QProgressBar(self.setting_layout)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)

        self.generate_layout.addWidget(self.progressBar)

        self.sendBtn = QPushButton(self.setting_layout)
        self.sendBtn.setObjectName(u"sendBtn")
        self.sendBtn.setMinimumSize(QSize(120, 120))
        self.sendBtn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-check-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sendBtn.setIcon(icon3)

        self.generate_layout.addWidget(self.sendBtn)


        self.verticalLayout_26.addLayout(self.generate_layout)

        self.verticalLayout_26.setStretch(0, 1)
        self.verticalLayout_26.setStretch(1, 4)

        self.gridLayout.addWidget(self.setting_layout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.new_page.setStyleSheet(u"")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.new_page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(20)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(40, -1, -1, -1)
        self.label_5 = QLabel(self.new_page)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.label_5)

        self.Tx_depth_value = QLabel(self.new_page)
        self.Tx_depth_value.setObjectName(u"Tx_depth_value")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.Tx_depth_value.sizePolicy().hasHeightForWidth())
        self.Tx_depth_value.setSizePolicy(sizePolicy7)

        self.horizontalLayout_14.addWidget(self.Tx_depth_value)

        self.horizontalScrollBar_Tx = QScrollBar(self.new_page)
        self.horizontalScrollBar_Tx.setObjectName(u"horizontalScrollBar_Tx")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar_Tx.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar_Tx.setSizePolicy(sizePolicy)
        self.horizontalScrollBar_Tx.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar_Tx.setMaximum(300)
        self.horizontalScrollBar_Tx.setPageStep(5)
        self.horizontalScrollBar_Tx.setOrientation(Qt.Horizontal)

        self.horizontalLayout_14.addWidget(self.horizontalScrollBar_Tx)

        self.Rx_depth_value = QLabel(self.new_page)
        self.Rx_depth_value.setObjectName(u"Rx_depth_value")
        sizePolicy7.setHeightForWidth(self.Rx_depth_value.sizePolicy().hasHeightForWidth())
        self.Rx_depth_value.setSizePolicy(sizePolicy7)

        self.horizontalLayout_14.addWidget(self.Rx_depth_value)

        self.horizontalScrollBar_Rx = QScrollBar(self.new_page)
        self.horizontalScrollBar_Rx.setObjectName(u"horizontalScrollBar_Rx")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar_Rx.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar_Rx.setSizePolicy(sizePolicy)
        self.horizontalScrollBar_Rx.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar_Rx.setMaximum(300)
        self.horizontalScrollBar_Rx.setPageStep(5)
        self.horizontalScrollBar_Rx.setOrientation(Qt.Horizontal)

        self.horizontalLayout_14.addWidget(self.horizontalScrollBar_Rx)

        self.Target_depth_value = QLabel(self.new_page)
        self.Target_depth_value.setObjectName(u"Target_depth_value")
        sizePolicy7.setHeightForWidth(self.Target_depth_value.sizePolicy().hasHeightForWidth())
        self.Target_depth_value.setSizePolicy(sizePolicy7)

        self.horizontalLayout_14.addWidget(self.Target_depth_value)

        self.horizontalScrollBar_Target = QScrollBar(self.new_page)
        self.horizontalScrollBar_Target.setObjectName(u"horizontalScrollBar_Target")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar_Target.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar_Target.setSizePolicy(sizePolicy)
        self.horizontalScrollBar_Target.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar_Target.setMaximum(300)
        self.horizontalScrollBar_Target.setPageStep(5)
        self.horizontalScrollBar_Target.setOrientation(Qt.Horizontal)

        self.horizontalLayout_14.addWidget(self.horizontalScrollBar_Target)


        self.verticalLayout_20.addLayout(self.horizontalLayout_14)

        self.verticalLayout_20.setStretch(0, 55)
        self.verticalLayout_20.setStretch(1, 1)
        self.stackedWidget.addWidget(self.new_page)
        self.plot1_page = QWidget()
        self.plot1_page.setObjectName(u"plot1_page")
        self.label_6 = QLabel(self.plot1_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 50, 221, 16))
        self.layoutWidget = QWidget(self.plot1_page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(120, 110, 80, 42))
        self.verticalLayout_29 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_29.addWidget(self.label_8)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_29.addWidget(self.label_10)

        self.layoutWidget1 = QWidget(self.plot1_page)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(530, 100, 93, 42))
        self.verticalLayout_30 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_30.addWidget(self.label_7)

        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_30.addWidget(self.label_9)

        self.stackedWidget.addWidget(self.plot1_page)
        self.plot2_page = QWidget()
        self.plot2_page.setObjectName(u"plot2_page")
        self.label_11 = QLabel(self.plot2_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(180, 100, 221, 16))
        self.layoutWidget2 = QWidget(self.plot2_page)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(210, 160, 80, 42))
        self.verticalLayout_31 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget2)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_31.addWidget(self.label_12)

        self.label_13 = QLabel(self.layoutWidget2)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_31.addWidget(self.label_13)

        self.layoutWidget_2 = QWidget(self.plot2_page)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(620, 150, 93, 42))
        self.verticalLayout_32 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.layoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_32.addWidget(self.label_14)

        self.label_15 = QLabel(self.layoutWidget_2)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_32.addWidget(self.label_15)

        self.layoutWidget_3 = QWidget(self.plot2_page)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(230, 320, 93, 42))
        self.verticalLayout_33 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.layoutWidget_3)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_33.addWidget(self.label_16)

        self.label_17 = QLabel(self.layoutWidget_3)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_33.addWidget(self.label_17)

        self.stackedWidget.addWidget(self.plot2_page)
        self.plot3_page = QWidget()
        self.plot3_page.setObjectName(u"plot3_page")
        self.label_18 = QLabel(self.plot3_page)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(180, 130, 261, 16))
        self.layoutWidget_4 = QWidget(self.plot3_page)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(210, 190, 80, 42))
        self.verticalLayout_34 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.layoutWidget_4)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_34.addWidget(self.label_19)

        self.label_20 = QLabel(self.layoutWidget_4)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_34.addWidget(self.label_20)

        self.layoutWidget_5 = QWidget(self.plot3_page)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(230, 350, 93, 42))
        self.verticalLayout_35 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.layoutWidget_5)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_35.addWidget(self.label_21)

        self.label_22 = QLabel(self.layoutWidget_5)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_35.addWidget(self.label_22)

        self.layoutWidget_6 = QWidget(self.plot3_page)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(620, 180, 93, 42))
        self.verticalLayout_36 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.layoutWidget_6)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_36.addWidget(self.label_23)

        self.label_24 = QLabel(self.layoutWidget_6)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_36.addWidget(self.label_24)

        self.stackedWidget.addWidget(self.plot3_page)
        self.plot4_page = QWidget()
        self.plot4_page.setObjectName(u"plot4_page")
        self.label_25 = QLabel(self.plot4_page)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(250, 120, 221, 16))
        self.layoutWidget_7 = QWidget(self.plot4_page)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(280, 180, 80, 42))
        self.verticalLayout_37 = QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.layoutWidget_7)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_37.addWidget(self.label_26)

        self.label_27 = QLabel(self.layoutWidget_7)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_37.addWidget(self.label_27)

        self.layoutWidget_8 = QWidget(self.plot4_page)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(300, 340, 94, 42))
        self.verticalLayout_38 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.layoutWidget_8)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_38.addWidget(self.label_28)

        self.label_29 = QLabel(self.layoutWidget_8)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_38.addWidget(self.label_29)

        self.layoutWidget_9 = QWidget(self.plot4_page)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(690, 170, 93, 42))
        self.verticalLayout_39 = QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.layoutWidget_9)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_39.addWidget(self.label_30)

        self.label_31 = QLabel(self.layoutWidget_9)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_39.addWidget(self.label_31)

        self.stackedWidget.addWidget(self.plot4_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setCursor(QCursor(Qt.ArrowCursor))
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_27.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.active_or_passive_setting.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"home", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"map", None))
        self.btn_map.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.btn_kill.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"setting", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"show", None))
        self.btn_index.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.plot1.setText(QCoreApplication.translate("MainWindow", u"plot1", None))
        self.btn_index_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.plot2.setText(QCoreApplication.translate("MainWindow", u"plot2", None))
        self.btn_index_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.plot3.setText(QCoreApplication.translate("MainWindow", u"plot3", None))
        self.btn_index_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.plot4.setText(QCoreApplication.translate("MainWindow", u"plot4", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"check", None))
        self.btn_information.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><"
                        "span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; "
                        "margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"PyDracula APP - Theme with colors based on Dracula for Python.", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.home_label.setText(QCoreApplication.translate("MainWindow", u"Underwater Signal Genrator Ver 1.0", None))
        self.passive_btn.setText(QCoreApplication.translate("MainWindow", u"Passive", None))
        self.active_btn.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.home_image_label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"wav.png", None))
        self.label_wav.setText(QCoreApplication.translate("MainWindow", u"wav", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"spec.png", None))
        self.label_spec.setText(QCoreApplication.translate("MainWindow", u"spec", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"soundpath.png", None))
        self.label_soundpath.setText(QCoreApplication.translate("MainWindow", u"soundpath", None))
        self.outputStatus.setText(QCoreApplication.translate("MainWindow", u"Status :", None))
        self.outputTx.setText(QCoreApplication.translate("MainWindow", u"Tx Pos(x, y, z) :", None))
        self.outputRx.setText(QCoreApplication.translate("MainWindow", u"Rx Pos(x, y, z) :", None))
        self.outputTarget.setText(QCoreApplication.translate("MainWindow", u"Target Pos(x, y, z) :", None))
        self.outputPulse.setText(QCoreApplication.translate("MainWindow", u"Pulse :", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Active", None))
        self.active_type_label.setText(QCoreApplication.translate("MainWindow", u"type", None))
        self.active_type_edit.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.active_type_edit.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))

        self.active_freq_label.setText(QCoreApplication.translate("MainWindow", u"center frequency", None))
        self.active_freq_edit.setItemText(0, QCoreApplication.translate("MainWindow", u"3500", None))
        self.active_freq_edit.setItemText(1, QCoreApplication.translate("MainWindow", u"3600", None))
        self.active_freq_edit.setItemText(2, QCoreApplication.translate("MainWindow", u"3700", None))
        self.active_freq_edit.setItemText(3, QCoreApplication.translate("MainWindow", u"3800", None))
        self.active_freq_edit.setItemText(4, QCoreApplication.translate("MainWindow", u"3900", None))
        self.active_freq_edit.setItemText(5, QCoreApplication.translate("MainWindow", u"4000", None))

        self.active_pulse_label.setText(QCoreApplication.translate("MainWindow", u"pulse duration", None))
        self.active_pulse_edit.setItemText(0, QCoreApplication.translate("MainWindow", u"0.1", None))
        self.active_pulse_edit.setItemText(1, QCoreApplication.translate("MainWindow", u"0.5", None))
        self.active_pulse_edit.setItemText(2, QCoreApplication.translate("MainWindow", u"1.0", None))

        self.active_band_label.setText(QCoreApplication.translate("MainWindow", u"bandwitdh", None))
        self.active_band_edit.setItemText(0, QCoreApplication.translate("MainWindow", u"400", None))
        self.active_band_edit.setItemText(1, QCoreApplication.translate("MainWindow", u"500", None))
        self.active_band_edit.setItemText(2, QCoreApplication.translate("MainWindow", u"600", None))

        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Passive", None))
        self.passive_type_label.setText(QCoreApplication.translate("MainWindow", u"type", None))
        self.passive_type_edit.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.passive_type_edit.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))

        self.passive_freq_label.setText(QCoreApplication.translate("MainWindow", u"center frequency", None))
        self.passive_freq_edit.setItemText(0, QCoreApplication.translate("MainWindow", u"1000", None))
        self.passive_freq_edit.setItemText(1, QCoreApplication.translate("MainWindow", u"1100", None))
        self.passive_freq_edit.setItemText(2, QCoreApplication.translate("MainWindow", u"1200", None))
        self.passive_freq_edit.setItemText(3, QCoreApplication.translate("MainWindow", u"1300", None))
        self.passive_freq_edit.setItemText(4, QCoreApplication.translate("MainWindow", u"1400", None))
        self.passive_freq_edit.setItemText(5, QCoreApplication.translate("MainWindow", u"1500", None))
        self.passive_freq_edit.setItemText(6, QCoreApplication.translate("MainWindow", u"1600", None))
        self.passive_freq_edit.setItemText(7, QCoreApplication.translate("MainWindow", u"1700", None))
        self.passive_freq_edit.setItemText(8, QCoreApplication.translate("MainWindow", u"1800", None))
        self.passive_freq_edit.setItemText(9, QCoreApplication.translate("MainWindow", u"1900", None))
        self.passive_freq_edit.setItemText(10, QCoreApplication.translate("MainWindow", u"2000", None))
        self.passive_freq_edit.setItemText(11, QCoreApplication.translate("MainWindow", u"2100", None))
        self.passive_freq_edit.setItemText(12, QCoreApplication.translate("MainWindow", u"2200", None))
        self.passive_freq_edit.setItemText(13, QCoreApplication.translate("MainWindow", u"2300", None))
        self.passive_freq_edit.setItemText(14, QCoreApplication.translate("MainWindow", u"2400", None))

        self.sendBtn.setText(QCoreApplication.translate("MainWindow", u"Send \ubcf4\ub0b4\uae30", None))
        self.label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"SET depth", None))
        self.Tx_depth_value.setText(QCoreApplication.translate("MainWindow", u"Tx 0", None))
        self.Rx_depth_value.setText(QCoreApplication.translate("MainWindow", u"Rx 0", None))
        self.Target_depth_value.setText(QCoreApplication.translate("MainWindow", u"Target 0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Plot 1 :\uc2dc\uac04\ucd95 + \uc8fc\ud30c\uc218\ucd95", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04\ucd95", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04\ucd95\uadf8\ub798\ud504", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ud30c\uc218\ucd95", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ud30c\uc218\ucd95\uadf8\ub798\ud504", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Plot 2 :\uc2dc\uac04\ucd95 + \uc8fc\ud30c\uc218\ucd95 + \uc74c\ud30c\uacbd\ub85c", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04\ucd95", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04\ucd95\uadf8\ub798\ud504", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ud30c\uc218\ucd95", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ud30c\uc218\ucd95\uadf8\ub798\ud504", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\uc74c\ud30c\uacbd\ub85c", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\uc74c\ud30c\uacbd\ub85c\uc0ac\uc9c4", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Plot 3 :\uc2dc\uac04\ucd95 + \uc8fc\ud30c\uc218\ucd95 + \ube54\ud3ec\ubc0d\uacb0\uacfc", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04\ucd95", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04\ucd95\uadf8\ub798\ud504", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\ube54\ud3ec\ubc0d \uacb0\uacfc", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\ube54\ud3ec\ubc0d\uacb0\uacfc\uc0ac\uc9c4", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ud30c\uc218\ucd95", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ud30c\uc218\ucd95\uadf8\ub798\ud504", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Plot 4 :\uc2dc\uac04\ucd95 + \uc8fc\ud30c\uc218\ucd95 + bearing", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04\ucd95", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04\ucd95\uadf8\ub798\ud504", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"bearing-to-time", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"bearing\uadf8\ub798\ud504", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ud30c\uc218\ucd95", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ud30c\uc218\ucd95\uadf8\ub798\ud504", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Maker : Park Byung Gwon  \u24d2Wanderson M. Pimenta", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

# Error: main.ui: Warning: The name 'layoutWidget' (QWidget) is already in use, defaulting to 'layoutWidget1'.

# main.ui: Warning: The name 'layoutWidget' (QWidget) is already in use, defaulting to 'layoutWidget2'.


# while executing 'C:\Users\user\AppData\Local\Programs\Python\Python310\Lib\site-packages\PySide6\uic -g python main.ui'
