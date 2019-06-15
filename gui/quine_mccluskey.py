from PyQt5.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QPushButton, QTextEdit,
        QVBoxLayout, QWidget, QDesktopWidget)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from core.qm.qm import QM
class QuineMcCluskey(QWidget):
    

    def __init__(self):
        super(QuineMcCluskey, self).__init__()

        self.createHorizontalGroupBox()
        self.createFormGroupBox()

        self.bigEditor = QTextEdit()
        self.bigEditor.setReadOnly(True)

        mainLayout = QVBoxLayout()
     
        
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.horizontalGroupBox)
        mainLayout.addWidget(self.bigEditor)
        self.setLayout(mainLayout)

        self.setWindowTitle("QM Circuit Minimizer")
        self.setWindowIcon(QIcon("gui/logo.jpeg"))
        self.setMinimumWidth(500)

        
    def createHorizontalGroupBox(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QHBoxLayout()

     
        button = QPushButton("Minimize")
        button.setMaximumWidth(100)
        layout.addWidget(button)
        button.clicked.connect(self.minimize_clicked)
        self.horizontalGroupBox.setLayout(layout)


    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Input")
        layout = QFormLayout()
        self.mterm_edit = QLineEdit()
        layout.addRow(QLabel("Minterms:"), self.mterm_edit)
        self.dcare_edit = QLineEdit()
        layout.addRow(QLabel("Don't cares:"),self.dcare_edit)
        self.v_edit = QLineEdit()
        layout.addRow(QLabel("Variables:"),self.v_edit)
        self.formGroupBox.setLayout(layout)

    def minimize_clicked(self):
        self.bigEditor.clear()
        mts = self.mterm_edit.text().split(' ')
        mts = list(filter(lambda x: x,mts))

        dcs = self.dcare_edit.text().split(' ')
        dcs = list(filter(lambda x: x,dcs))

        vs = self.v_edit.text().split(' ')
        vs = list(filter(lambda x: x,vs))
        print(mts)
        qm = QM(mts,dcs,vs)
        pis = qm.pis()
        self.bigEditor.append('Prime Implicants')
        
        for pi in pis:
            self.bigEditor.append(str(pi))
            self.bigEditor.append('\n')

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = QuineMcCluskey()
    window.show()
    sys.exit(app.exec_())
