from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QProgressBar, QGridLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QThread


class MainWindow(QMainWindow):
    def __init__(self, coreObject: QThread) -> None:
        super().__init__()

        font = QFont("Vazir", 14)
        self.setFont(font)

        self.setWindowTitle("Final Projet")

        self.setMinimumSize(500, 300)

        widget = CentralWidget(coreObject)
        self.setCentralWidget(widget)

        self.show()


class CentralWidget(QWidget):
    def __init__(self, coreObject) -> None:
        super().__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        self.txtdisplay = QLineEdit()
        self.txtdisplay.setPlaceholderText("Name")
        self.txtdisplay.textChanged.connect(self.check_enable)
        layout.addWidget(self.txtdisplay, 0, 0, 1, 4)

        self.btnAdd = QPushButton(text="Add", parent=self)
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
        layout.addWidget(self.btnRoll, 4, 4)

        try:
            with open('Datafile.dll', 'r') as file:
                pass
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


app = QApplication([])
with open("Datafile.dll", 'a'):
    pass
win = MainWindow("")
app.exec()
