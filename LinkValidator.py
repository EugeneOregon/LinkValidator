# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LinkValidator.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LinkValidator(object):
    def setupUi(self, LinkValidator):
        LinkValidator.setObjectName("LinkValidator")
        LinkValidator.resize(780, 517)
        LinkValidator.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.625, y1:0.744, x2:1, y2:0, stop:0 rgba(55, 55, 55, 255), stop:1 rgba(37, 37, 37, 255));\n"
            "color: rgb(240, 240, 240);\n"
            "border-radius: 5%;\n"
            "font: 10pt \"Arial\";\n"
            "\n"
            "")
        self.centralwidget = QtWidgets.QWidget(LinkValidator)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.stopValidateButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopValidateButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopValidateButton.sizePolicy().hasHeightForWidth())
        self.stopValidateButton.setSizePolicy(sizePolicy)
        self.stopValidateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopValidateButton.setStyleSheet("QPushButton {\n"
                                              "    background-color: qlineargradient(spread:pad, x1:0.272727, y1:0.767, x2:1, y2:0, stop:0 rgba(81, 81, 81, 255), stop:1 rgba(100, 100, 100, 255));\n"
                                              "    border-radius: 5%;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "    font: 87 8pt \"Arial Black\";\n"
                                              "    \n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: qlineargradient(spread:pad, x1:0.472, y1:0.585, x2:1, y2:0, stop:0.00568182 rgba(250, 167, 1, 255), stop:1 rgba(234, 128, 7, 255));\n"
                                              "    border-radius: 5%;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "    font: 87 10pt \"Arial Black\";\n"
                                              "    transition: 0.3s ease;\n"
                                              "}")
        self.stopValidateButton.setObjectName("stopValidateButton")
        self.gridLayout.addWidget(self.stopValidateButton, 4, 1, 1, 2)
        self.Header = QtWidgets.QWidget(self.centralwidget)
        self.Header.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.472, y1:0.585, x2:1, y2:0, stop:0.00568182 rgba(250, 167, 1, 255), stop:1 rgba(234, 128, 7, 255));")
        self.Header.setObjectName("Header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Header)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.imgLogo = QtWidgets.QLabel(self.Header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgLogo.sizePolicy().hasHeightForWidth())
        self.imgLogo.setSizePolicy(sizePolicy)
        self.imgLogo.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.imgLogo.setText("")
        self.imgLogo.setPixmap(QtGui.QPixmap("image/linkvalidlogo.png"))
        self.imgLogo.setObjectName("imgLogo")
        self.horizontalLayout.addWidget(self.imgLogo)
        self.textLogo = QtWidgets.QLabel(self.Header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textLogo.sizePolicy().hasHeightForWidth())
        self.textLogo.setSizePolicy(sizePolicy)
        self.textLogo.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
            "color: rgb(255, 255, 255);\n"
            "font: 87 14pt \"Arial Black\";")
        self.textLogo.setObjectName("textLogo")
        self.horizontalLayout.addWidget(self.textLogo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.manualButton = QtWidgets.QPushButton(self.Header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manualButton.sizePolicy().hasHeightForWidth())
        self.manualButton.setSizePolicy(sizePolicy)
        self.manualButton.setBaseSize(QtCore.QSize(0, 0))
        self.manualButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.manualButton.setStyleSheet("QPushButton {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
                                        "    border-radius: 5%;\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    font: 87 8pt \"Arial Black\";\n"
                                        "    \n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0.272727, y1:0.767, x2:1, y2:0, stop:0 rgba(81, 81, 81, 255), stop:1 rgba(100, 100, 100, 255));\n"
                                        "    border-radius: 50%;\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    font: 87 10pt \"Arial Black\";\n"
                                        "    transition: 0.3s ease;\n"
                                        "}")
        self.manualButton.setFlat(False)
        self.manualButton.setObjectName("manualButton")
        self.horizontalLayout.addWidget(self.manualButton)
        self.faqButton = QtWidgets.QPushButton(self.Header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faqButton.sizePolicy().hasHeightForWidth())
        self.faqButton.setSizePolicy(sizePolicy)
        self.faqButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.faqButton.setStyleSheet("QPushButton {\n"
                                     "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
                                     "    border-radius: 5%;\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    font: 87 8pt \"Arial Black\";\n"
                                     "    \n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: qlineargradient(spread:pad, x1:0.272727, y1:0.767, x2:1, y2:0, stop:0 rgba(81, 81, 81, 255), stop:1 rgba(100, 100, 100, 255));\n"
                                     "    border-radius: 50%;\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    font: 87 10pt \"Arial Black\";\n"
                                     "    transition: 0.3s ease;\n"
                                     "}")
        self.faqButton.setObjectName("faqButton")
        self.horizontalLayout.addWidget(self.faqButton)
        self.copyButton = QtWidgets.QPushButton(self.Header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copyButton.sizePolicy().hasHeightForWidth())
        self.copyButton.setSizePolicy(sizePolicy)
        self.copyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.copyButton.setStyleSheet("QPushButton {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
                                      "    border-radius: 5%;\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    font: 87 20pt \"Arial Black\";\n"
                                      "    \n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0.272727, y1:0.767, x2:1, y2:0, stop:0 rgba(81, 81, 81, 255), stop:1 rgba(100, 100, 100, 255));\n"
                                      "    border-radius: 50%;\n"
                                      "    color: rgb(255, 170, 0);\n"
                                      "    font: 87 24pt \"Arial Black\";\n"
                                      "    transition: 0.3s ease;\n"
                                      "}")
        self.copyButton.setObjectName("copyButton")
        self.horizontalLayout.addWidget(self.copyButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 9)
        self.horizontalLayout.setStretch(4, 2)
        self.horizontalLayout.setStretch(5, 2)
        self.horizontalLayout.setStretch(6, 2)
        self.horizontalLayout.setStretch(7, 1)
        self.textLogo.raise_()
        self.manualButton.raise_()
        self.faqButton.raise_()
        self.imgLogo.raise_()
        self.copyButton.raise_()
        self.gridLayout.addWidget(self.Header, 0, 0, 1, 3)
        self.Success = QtWidgets.QWidget(self.centralwidget)
        self.Success.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.272727, y1:0.767, x2:1, y2:0, stop:0 rgba(81, 81, 81, 255), stop:1 rgba(100, 100, 100, 255));\n"
            "border-radius: 5%;")
        self.Success.setObjectName("Success")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Success)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.successLinks = QtWidgets.QLabel(self.Success)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.successLinks.sizePolicy().hasHeightForWidth())
        self.successLinks.setSizePolicy(sizePolicy)
        self.successLinks.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
            "color: rgb(255, 255, 255);\n"
            "font: 87 10pt \"Arial Black\";")
        self.successLinks.setObjectName("successLinks")
        self.verticalLayout_6.addWidget(self.successLinks)
        self.successEdit = QtWidgets.QLineEdit(self.Success)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.successEdit.sizePolicy().hasHeightForWidth())
        self.successEdit.setSizePolicy(sizePolicy)
        self.successEdit.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
            "font: 87 16pt \"Arial Black\";\n"
            "border-radius: 5%;")
        self.successEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.successEdit.setObjectName("successEdit")
        self.verticalLayout_6.addWidget(self.successEdit)
        self.gridLayout.addWidget(self.Success, 2, 2, 1, 1)
        self.Reidrect = QtWidgets.QWidget(self.centralwidget)
        self.Reidrect.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.272727, y1:0.767, x2:1, y2:0, stop:0 rgba(81, 81, 81, 255), stop:1 rgba(100, 100, 100, 255));\n"
            "border-radius: 5%;")
        self.Reidrect.setObjectName("Reidrect")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Reidrect)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.redirectLinks = QtWidgets.QLabel(self.Reidrect)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redirectLinks.sizePolicy().hasHeightForWidth())
        self.redirectLinks.setSizePolicy(sizePolicy)
        self.redirectLinks.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
            "color: rgb(255, 255, 255);\n"
            "font: 87 10pt \"Arial Black\";")
        self.redirectLinks.setObjectName("redirectLinks")
        self.verticalLayout_4.addWidget(self.redirectLinks)
        self.redirectEdit = QtWidgets.QLineEdit(self.Reidrect)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redirectEdit.sizePolicy().hasHeightForWidth())
        self.redirectEdit.setSizePolicy(sizePolicy)
        self.redirectEdit.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
            "font: 87 16pt \"Arial Black\";\n"
            "border-radius: 5%;")
        self.redirectEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.redirectEdit.setObjectName("redirectEdit")
        self.verticalLayout_4.addWidget(self.redirectEdit)
        self.gridLayout.addWidget(self.Reidrect, 2, 1, 1, 1)
        self.Error = QtWidgets.QWidget(self.centralwidget)
        self.Error.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.272727, y1:0.767, x2:1, y2:0, stop:0 rgba(81, 81, 81, 255), stop:1 rgba(100, 100, 100, 255));\n"
            "border-radius: 5%;")
        self.Error.setObjectName("Error")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Error)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.errorLinks = QtWidgets.QLabel(self.Error)
        self.errorLinks.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
            "color: rgb(255, 255, 255);\n"
            "font: 87 10pt \"Arial Black\";")
        self.errorLinks.setObjectName("errorLinks")
        self.verticalLayout_2.addWidget(self.errorLinks)
        self.errorEdit = QtWidgets.QLineEdit(self.Error)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errorEdit.sizePolicy().hasHeightForWidth())
        self.errorEdit.setSizePolicy(sizePolicy)
        self.errorEdit.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
            "font: 87 16pt \"Arial Black\";\n"
            "border-radius: 5%;")
        self.errorEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.errorEdit.setObjectName("errorEdit")
        self.verticalLayout_2.addWidget(self.errorEdit)
        self.gridLayout.addWidget(self.Error, 1, 2, 1, 1)
        self.Total = QtWidgets.QWidget(self.centralwidget)
        self.Total.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.272727, y1:0.767, x2:1, y2:0, stop:0 rgba(81, 81, 81, 255), stop:1 rgba(100, 100, 100, 255));\n"
            "border-radius: 5%;")
        self.Total.setObjectName("Total")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Total)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.totalLinks = QtWidgets.QLabel(self.Total)
        self.totalLinks.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
            "color: rgb(255, 170, 0);\n"
            "font: 87 10pt \"Arial Black\";")
        self.totalLinks.setObjectName("totalLinks")
        self.verticalLayout_5.addWidget(self.totalLinks)
        self.totalEdit = QtWidgets.QLineEdit(self.Total)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalEdit.sizePolicy().hasHeightForWidth())
        self.totalEdit.setSizePolicy(sizePolicy)
        self.totalEdit.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
            "font: 87 16pt \"Arial Black\";\n"
            "border-radius: 5%;")
        self.totalEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.totalEdit.setObjectName("totalEdit")
        self.verticalLayout_5.addWidget(self.totalEdit)
        self.gridLayout.addWidget(self.Total, 1, 1, 1, 1)
        self.Sidebar = QtWidgets.QWidget(self.centralwidget)
        self.Sidebar.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.272727, y1:0.767, x2:1, y2:0, stop:0 rgba(81, 81, 81, 255), stop:1 rgba(100, 100, 100, 255));\n"
            "border-radius: 5%;")
        self.Sidebar.setObjectName("Sidebar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Sidebar)
        self.verticalLayout.setContentsMargins(7, 15, 7, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkLinkButton = QtWidgets.QPushButton(self.Sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkLinkButton.sizePolicy().hasHeightForWidth())
        self.checkLinkButton.setSizePolicy(sizePolicy)
        self.checkLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkLinkButton.setStyleSheet("QPushButton {\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0.472, y1:0.585, x2:1, y2:0, stop:0.00568182 rgba(250, 167, 1, 255), stop:1 rgba(234, 128, 7, 255));\n"
                                           "    border-radius: 5%;\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    font: 87 9pt \"Arial Black\";\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0.329545, y1:0.739, x2:1, y2:0, stop:0 rgba(255, 216, 57, 255), stop:1 rgba(255, 173, 0, 255));\n"
                                           "    border-radius: 5%;\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    font: 87 10pt \"Arial Black\";\n"
                                           "    transition: 0.3s ease;\n"
                                           "}")
        self.checkLinkButton.setObjectName("checkLinkButton")
        self.verticalLayout.addWidget(self.checkLinkButton)
        self.gDocsButton = QtWidgets.QPushButton(self.Sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gDocsButton.sizePolicy().hasHeightForWidth())
        self.gDocsButton.setSizePolicy(sizePolicy)
        self.gDocsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gDocsButton.setStyleSheet("QPushButton {\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0.472, y1:0.585, x2:1, y2:0, stop:0.00568182 rgba(250, 167, 1, 255), stop:1 rgba(234, 128, 7, 255));\n"
                                       "    border-radius: 5%;\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    font: 87 9pt \"Arial Black\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0.329545, y1:0.739, x2:1, y2:0, stop:0 rgba(255, 216, 57, 255), stop:1 rgba(255, 173, 0, 255));\n"
                                       "    border-radius: 5%;\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    font: 87 10pt \"Arial Black\";\n"
                                       "    transition: 0.3s ease;\n"
                                       "}")
        self.gDocsButton.setObjectName("gDocsButton")
        self.verticalLayout.addWidget(self.gDocsButton)
        self.excelButton = QtWidgets.QPushButton(self.Sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.excelButton.sizePolicy().hasHeightForWidth())
        self.excelButton.setSizePolicy(sizePolicy)
        self.excelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.excelButton.setStyleSheet("QPushButton {\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0.472, y1:0.585, x2:1, y2:0, stop:0.00568182 rgba(250, 167, 1, 255), stop:1 rgba(234, 128, 7, 255));\n"
                                       "    border-radius: 5%;\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    font: 87 9pt \"Arial Black\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0.329545, y1:0.739, x2:1, y2:0, stop:0 rgba(255, 216, 57, 255), stop:1 rgba(255, 173, 0, 255));\n"
                                       "    border-radius: 5%;\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    font: 87 10pt \"Arial Black\";\n"
                                       "    transition: 0.3s ease;\n"
                                       "}")
        self.excelButton.setObjectName("excelButton")
        self.verticalLayout.addWidget(self.excelButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.Sidebar)
        self.pushButton.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
            "border-radius: 5%;\n"
            "font: 10pt \"Ink Free\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.designButton = QtWidgets.QPushButton(self.Sidebar)
        self.designButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.designButton.setStyleSheet("QPushButton {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
                                        "    color: rgb(240, 240, 240);\n"
                                        "    font: 12pt \"Ink Free\";\n"
                                        "    border-radius: 5%;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    color: rgb(255, 170, 0);\n"
                                        "}")
        self.designButton.setObjectName("designButton")
        self.verticalLayout.addWidget(self.designButton)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 14)
        self.verticalLayout.setStretch(5, 1)
        self.gridLayout.addWidget(self.Sidebar, 1, 0, 4, 1)
        self.logMonitor = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.logMonitor.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.272727, y1:0.767, x2:1, y2:0, stop:0 rgba(81, 81, 81, 255), stop:1 rgba(100, 100, 100, 255));\n"
            "border-radius: 5%;\n"
            "color: rgb(255, 255, 255);")
        self.logMonitor.setObjectName("logMonitor")
        self.gridLayout.addWidget(self.logMonitor, 3, 1, 1, 2)
        self.gridLayout.setRowMinimumHeight(4, 40)
        LinkValidator.setCentralWidget(self.centralwidget)

        self.retranslateUi(LinkValidator)
        QtCore.QMetaObject.connectSlotsByName(LinkValidator)

    def retranslateUi(self, LinkValidator):
        _translate = QtCore.QCoreApplication.translate
        LinkValidator.setWindowTitle(_translate("LinkValidator", "Link Validator"))
        LinkValidator.setWindowIcon(QtGui.QIcon('image/linkvalidicon.png'))
        self.stopValidateButton.setText(_translate("LinkValidator", "Stop validate"))
        self.textLogo.setText(_translate("LinkValidator", "Link Validator"))
        self.manualButton.setText(_translate("LinkValidator", "  Manual  "))
        self.faqButton.setText(_translate("LinkValidator", "FAQ"))
        self.copyButton.setText(_translate("LinkValidator", "???"))
        self.successLinks.setText(_translate("LinkValidator", "2xx: Success"))
        self.successEdit.setText(_translate("LinkValidator", "0"))
        self.redirectLinks.setText(_translate("LinkValidator", "3xx: Redirection"))
        self.redirectEdit.setText(_translate("LinkValidator", "0"))
        self.errorLinks.setText(_translate("LinkValidator", "4xx: Client Error"))
        self.errorEdit.setText(_translate("LinkValidator", "0"))
        self.totalLinks.setText(_translate("LinkValidator", "Total links"))
        self.totalEdit.setText(_translate("LinkValidator", "0"))
        self.checkLinkButton.setText(_translate("LinkValidator", "Check Link"))
        self.gDocsButton.setText(_translate("LinkValidator", "Google Docs report"))
        self.excelButton.setText(_translate("LinkValidator", "Excel report"))
        self.pushButton.setText(_translate("LinkValidator", "version  1.0"))
        self.designButton.setText(_translate("LinkValidator", "Designed by Eugene"))
