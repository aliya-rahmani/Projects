#importing libraries
#pip install PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore , QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar")
        self.setGeometry(100,100,600,400)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        calendar=QCalendarWidget(self)
        calendar.setGeometry(10,10,400,250)
        push=QPushButton("Next Year",self)
        push2=QPushButton("Previous Year",self)
        push2.setGeometry(60,280,100,40)
        push2.clicked.connect(lambda: do_action2())
        def do_action2():
            calendar.showPreviousYear()

        push.setGeometry(180,280,100,40)
        push.clicked.connect(lambda: do_action())
        def do_action():
            calendar.showNextYear()
app=QApplication(sys.argv)
window=Window()
sys.exit(app.exec())
