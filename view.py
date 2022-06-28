from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QProgressBar, QGridLayout, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QThread


class MainWindow(QMainWindow):
    def __init__(self, _coreObject) -> None:
        super().__init__()

        font = QFont("Vazir", 12)
        self.setFont(font)

        self.setWindowTitle("Final Projet")

        self.setMinimumSize(500, 300)

        widget = CentralWidget(_coreObject)
        self.setCentralWidget(widget)

        self.show()


class CentralWidget(QWidget):
    def __init__(self, _coreObject) -> None:
        super().__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        self.txtdisplay = QLineEdit()
        self.txtdisplay.setPlaceholderText("Name")
        layout.addWidget(self.txtdisplay, 0, 0, 1, 5)


app = QApplication([])
win = MainWindow("")
app.exec()
