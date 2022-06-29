from PyQt5.QtCore import QThread, pyqtSignal
from random import randint
from time import sleep


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.countNumber = 0

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head
            self.head.prev = self.tail

            self.countNumber += 1
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next

            temp.next = newNode
            newNode.prev = temp
            self.tail = newNode
            self.tail.next = self.head
            self.head.prev = self.tail

            self.countNumber += 1

    def finder(self):
        init = self.head
        front = self.tail

        if self.countNumber % 2 == 0:
            temp = self.head.next
        elif self.countNumber % 2 != 0:
            temp = self.head
        while True:
            if temp.value == front.value:
                randomValue = randint(0, self.countNumber+1)
                for i in range(randomValue):
                    yield [str(init.value), str(front.value), randomValue, i, str(init.next.value), str(init.prev.value), str(front.next.value), str(front.prev.value)]
                    front = front.next
                    init = init.next
                    sleep(0.1*i)
                else:
                    return
            else:
                temp = temp.next
                front = front.prev


class CoreModel(QThread):
    newValue = pyqtSignal('PyQt_PyObject')

    def run(self) -> None:
        dataTuple = linkedListObject.finder()
        for i in dataTuple:
            # i will be a tuple
            self.newValue.emit(i)


linkedListObject = CircularDoublyLinkedList()
