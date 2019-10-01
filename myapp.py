import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt5.QtCore import Qt





class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        ## Title Main UI
        self.setWindowTitle("My Awesome App!")
        self.initUI()
        self.show()

    def initUI(self):
        ## Main UI code goes here
        self.label = qtw.QLabel(self)
        self.label.setText("This is a PyQt5 App")
        self.label.move(50,50)

        self.button1 = qtw.QPushButton(self)
        self.button1.setText("Click Me")
        self.button1.clicked.connect(self.clicked)

        ## End main UI code
        
    def clicked(self):
        self.label.setText("Button pressed")

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())