from view import MainWindow
from model import CoreModel, linkedListObject
from PyQt5.QtWidgets import QApplication

app = QApplication([])
core = CoreModel()
win = MainWindow(core, linkedListObject)
win.show()
app.exec()
