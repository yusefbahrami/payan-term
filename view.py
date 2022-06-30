from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QProgressBar, QGridLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QThread


class MainWindow(QMainWindow):
    def __init__(self, coreObject, modelObject) -> None:
        super().__init__()

        font = QFont("Vazir", 14)
        self.setFont(font)

        self.setWindowTitle("Final Projet")

        self.setMinimumSize(500, 300)

        widget = CentralWidget(coreObject, modelObject)
        self.setCentralWidget(widget)


class CentralWidget(QWidget):
    def __init__(self, coreObject: QThread, modelObject) -> None:
        super().__init__()
        self.coreObj = coreObject
        self.modelObj = modelObject

        layout = QGridLayout()
        self.setLayout(layout)

        self.txtdisplay = QLineEdit()
        self.txtdisplay.setPlaceholderText("Name")
        self.txtdisplay.textChanged.connect(self.check_enable)
        layout.addWidget(self.txtdisplay, 0, 0, 1, 4)

        self.btnAdd = QPushButton(text="Add", parent=self)
        self.btnAdd.clicked.connect(self.btnAdd_click)
        layout.addWidget(self.btnAdd, 0, 4)

        self.lblDisplay = QLabel()
        self.lblDisplay.setStyleSheet(
            "background-color: #bababa; color: #3d3d3c;")
        self.lblDisplay.setFont(QFont("Vazir", 14))
        layout.addWidget(self.lblDisplay, 1, 0, 1, 5)

        self.lblShowInitPrev = QLabel("prev")
        self.lblShowInitPrev.setStyleSheet("color: #3d3d3c;")
        self.lblShowInitPrev.setFont(QFont("Vazir", 10))
        layout.addWidget(self.lblShowInitPrev, 2, 1)

        self.lblShowInit = QLabel(text="init")
        layout.addWidget(self.lblShowInit, 2, 2)

        self.lblShowInitNext = QLabel("next")
        self.lblShowInitNext.setStyleSheet("color: #3d3d3c;")
        self.lblShowInitNext.setFont(QFont("Vazir", 10))
        layout.addWidget(self.lblShowInitNext, 2, 3)

        self.lblShowFrontPrev = QLabel("prev")
        self.lblShowFrontPrev.setStyleSheet("color: #3d3d3c;")
        self.lblShowFrontPrev.setFont(QFont("Vazir", 10))
        layout.addWidget(self.lblShowFrontPrev, 3, 1)

        self.lblShowFront = QLabel(text="front")
        layout.addWidget(self.lblShowFront, 3, 2)

        self.lblShowFrontNext = QLabel("next")
        self.lblShowFrontNext.setStyleSheet("color: #3d3d3c;")
        self.lblShowFrontNext.setFont(QFont("Vazir", 10))
        layout.addWidget(self.lblShowFrontNext, 3, 3)

        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(0)
        layout.addWidget(self.progressbar, 4, 0, 1, 4)

        self.btnRoll = QPushButton(text="Roll", parent=self)
        self.btnRoll.clicked.connect(self.btnRoll_click)
        layout.addWidget(self.btnRoll, 4, 4)

        try:
            with open('Datafile.dll', 'r') as file:
                for line in file:
                    self.displayLabel_setText(line.strip())
        except FileNotFoundError:
            self.show_messagebox()

        self.check_enable()

    def show_messagebox(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Critical)
        self.msgBox.setText("Data File Was Not Found!")
        self.msgBox.setWindowTitle("File Not Found Error")
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.exec()

    def check_enable(self):
        if self.txtdisplay.text() == "":
            self.btnAdd.setEnabled(False)
        else:
            self.btnAdd.setEnabled(True)

        if self.lblDisplay.text() == "":
            self.btnRoll.setEnabled(False)
        else:
            self.btnRoll.setEnabled(True)

    def displayLabel_setText(self, text):
        if self.lblDisplay.text() == "":
            self.lblDisplay.setText(text)
            self.modelObj.append(text)
        else:
            self.lblDisplay.setText(f"{self.lblDisplay.text()}, {text}")
            self.modelObj.append(text)

    def btnAdd_click(self):
        self.displayLabel_setText(self.txtdisplay.text())
        self.txtdisplay.setFocus()

        with open('Datafile.dll', 'a') as file:
            file.write(f"{self.txtdisplay.text()}\n")

        self.txtdisplay.clear()
        self.check_enable()

    def btnRoll_click(self):
        self.coreObj.start()
        self.coreObj.newValue.connect(self.set_data)

    def set_data(self, data):
        self.lblShowInit.setText(data[0])
        self.lblShowFront.setText(data[1])
        self.progressbar.setMaximum(data[2])
        self.progressbar.setValue(data[3]+1)
        self.lblShowInitPrev.setText(data[5])
        self.lblShowInitNext.setText(data[4])
        self.lblShowFrontPrev.setText(data[7])
        self.lblShowFrontNext.setText(data[6])
