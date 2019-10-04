import sys
import os
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyPDF2 import PdfFileReader, PdfFileWriter


class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        ## Title Main UI
        self.setWindowTitle("My Awesome App!")
        self.initUI()
        self.show()

    def initUI(self):
        ## Main UI code goes here
        self.label_title = qtw.QLabel(self)
        self.label_title.setText("This is a PyQt5 PDF-merger App")
        self.label_title.setAlignment(qtc.Qt.AlignCenter)

        self.label_empty = qtw.QLabel(self)

        self.button_add = qtw.QPushButton(self)
        self.button_add.setText("Add PDF File")
        self.button_add.clicked.connect(self.open_file)
        
        self.button_remove = qtw.QPushButton(self)
        self.button_remove.setText("Remove PDF File")
        self.button_remove.clicked.connect(self.remove_file)
        
        self.label_listbox = qtw.QLabel(self)
        self.label_listbox.setText("List of PDF Files")
        self.listbox = qtw.QListWidget(self)
        self.listbox.setFixedWidth(200)
        self.listbox.setFixedHeight(100)
        #self.listbox.setDragDropMode(qtw.QAbstractItemView.InternalMove)
        self.listbox.setSelectionMode(self.listbox.SingleSelection)
        self.listbox.itemClicked.connect(self.display_item)

        self.label_settings = qtw.QLabel(self)
        self.label_settings.setText("Setting for PDF File")

        self.label_filename = qtw.QLabel(self)
        self.label_filename.setFixedWidth(60)
        self.label_filename.setText("File Name:")

        self.label_pages = qtw.QLabel(self)
        self.label_pages.setFixedWidth(60)
        self.label_pages.setText("Pages:")

        self.label_start = qtw.QLabel(self)
        self.label_start.setFixedWidth(60)
        self.label_start.setText("Start page:")

        self.label_end = qtw.QLabel(self)
        self.label_end.setFixedWidth(60)
        self.label_end.setText("End page:")

        self.label_filename_text = qtw.QLabel(self)
        self.label_filename_text.setMinimumWidth(100)

        self.label_pages_text = qtw.QLabel(self)

        self.label_start_text = qtw.QLineEdit(self)
        self.label_start_text.setValidator(qtg.QIntValidator(self.label_start_text))
        self.label_start_text.editingFinished.connect(self.edit_start)

        self.label_end_text = qtw.QLineEdit(self)
        self.label_end_text.setValidator(qtg.QIntValidator(self.label_end_text))
        self.label_end_text.editingFinished.connect(self.edit_end)

        self.button_save = qtw.QPushButton(self)
        self.button_save.setText("Save as new PDF File")
        self.button_save.clicked.connect(self.save_file)

        self.createLayout()
        ## End main UI code

    def createLayout(self):
        topLayout = qtw.QHBoxLayout()
        topLayout.addWidget(self.label_title)

        layout1 = qtw.QVBoxLayout()
        layout1.addWidget(self.label_empty)
        layout1.addWidget(self.button_add)
        layout1.addWidget(self.button_remove)
        layout1.addStretch(20)
        layout2 = qtw.QVBoxLayout()
        layout2.addWidget(self.label_listbox)
        layout2.addWidget(self.listbox)
                
        layout3A = qtw.QHBoxLayout()
        layout3A.addWidget(self.label_settings)
        layout3B = qtw.QHBoxLayout()
        layout3B.addWidget(self.label_filename)
        layout3B.addWidget(self.label_filename_text)
        layout3C = qtw.QHBoxLayout()
        layout3C.addWidget(self.label_pages)
        layout3C.addWidget(self.label_pages_text)
        layout3D = qtw.QHBoxLayout()
        layout3D.addWidget(self.label_start)
        layout3D.addWidget(self.label_start_text)
        layout3E = qtw.QHBoxLayout()
        layout3E.addWidget(self.label_end)
        layout3E.addWidget(self.label_end_text)
     
        layout3 = qtw.QVBoxLayout()
        layout3.addLayout(layout3A)
        layout3.addLayout(layout3B)
        layout3.addLayout(layout3C)
        layout3.addLayout(layout3D)
        layout3.addLayout(layout3E)
        layout3.addStretch(20)

        middleLayout = qtw.QHBoxLayout()
        middleLayout.addLayout(layout1)
        middleLayout.addLayout(layout2)
        middleLayout.addLayout(layout3)

        bottomLayout = qtw.QHBoxLayout()
        bottomLayout.addWidget(self.button_save)

        mainLayout = qtw.QVBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(middleLayout)
        mainLayout.addLayout(bottomLayout)

        widget = qtw.QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

    def open_file(self):
        self.filename = qtw.QFileDialog.getOpenFileName(self, 'Open File', './', "PDF Files (*.pdf)")
        if self.filename[0]:
            self.pdf = PDF_Doc(self.filename)
            pdf_list.append(self.pdf)
            self.listbox.addItem(self.pdf.display)

    def display_item(self, item):
        self.index = self.listbox.row(item)
        self.label_filename_text.setText(str(pdf_list[self.index].display))
        self.label_pages_text.setText(str(pdf_list[self.index].pages))
        self.label_start_text.setText(str(pdf_list[self.index].start))
        self.label_end_text.setText(str(pdf_list[self.index].end))

    def edit_start(self):
        if self.label_start_text.text() > self.label_end_text.text():
            title = "Oops!"
            message = "Number exceeds last page number!"
            self.show_popup(title, message)
            self.label_start_text.setText(str(pdf_list[self.index].start))
        else:
            pdf_list[self.index].start = self.label_start_text.text()

    def edit_end(self):
        if int(self.label_end_text.text()) > int(self.label_pages_text.text()):
            title = "Oops!"
            message = "Number exceeds the total page numbers!"
            self.show_popup(title, message)
            self.label_end_text.setText(str(pdf_list[self.index].end))
        else:
            pdf_list[self.index].end = self.label_end_text.text()

    def show_popup(self, title, message):
        msg = qtw.QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)

        _ = msg.exec_()

    def save_file(self):
        writer = PdfFileWriter()

        output_filename = qtw.QFileDialog.getSaveFileName(self, 'Save File As', './', "PDF Files (*.pdf)")
        if output_filename[0]:
            print(output_filename[0])
            with open(output_filename[0], 'wb') as f:
                for doc in pdf_list:
                    doc.add_to_writer(writer)
                    
                writer.write(f)

    def remove_file(self):
        listItems=self.listbox.selectedItems()
        if not listItems: return        
        for item in listItems:            
            index = self.listbox.row(item)
            self.listbox.takeItem(self.listbox.row(item))
            title = "Removed PDF File"
            message = f"Removed PDF File: \'{item.text()}\'"
            self.show_popup(title, message)
            pdf_list.pop(index)


class PDF_Doc():

    def __init__(self, filename):
        self.filename = filename
        self.display = filename[0].split('/')[-1]
        self.pdf = load_pdf(filename[0])
        self.pages = self.pdf.getNumPages()
        self.start = 1
        self.end = self.pages

    def add_to_writer(self, writer):
        for i in range(int(self.start)-1, int(self.end)):
            writer.addPage(self.pdf.getPage(i))

def load_pdf(filename):
    f = open(filename, 'rb')
    return PdfFileReader(f)


if __name__ == '__main__':
    pdf_list = []
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())