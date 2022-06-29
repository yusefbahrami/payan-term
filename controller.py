from view import MainWindow
from model import CoreModel, CircularDoublyLinkedList
from PyQt5.QtWidgets import QApplication

app = QApplication([])
core = CoreModel()
dataModel = CircularDoublyLinkedList()
win = MainWindow(core, dataModel)
win.show()
app.exec()
