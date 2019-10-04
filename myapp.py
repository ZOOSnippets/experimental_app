import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


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

        self.button1 = qtw.QPushButton(self)
        self.button1.setText("Click Me")
        self.button1.clicked.connect(self.clickme)
        
        self.button2 = qtw.QPushButton(self)
        self.button2.setText("Open File")
        self.button2.clicked.connect(self.open_file)

        self.listbox = qtw.QListWidget(self)
        self.listbox.setGeometry(0,0,100,200)
        self.createLayout()
        ## End main UI code

    def createLayout(self):
        layout1 = qtw.QGridLayout()
        layout1.addWidget(self.label,0,0)
        layout1.addWidget(self.listbox,1,1)
        layout1.addWidget(self.button1,1,0)
        layout1.addWidget(self.button2,2,0)
        
        widget = qtw.QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

    def open_file(self):
        filename = qtw.QFileDialog.getOpenFileName(self, 'Open File', './', "PDF Files (*.pdf)")
        
        if filename[0]:
            print(filename[0])

    def clickme(self):
        self.label.setText("Button pressed")

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())