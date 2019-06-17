from PyQt5.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,QLabel, QLineEdit,
    QPushButton, QTextEdit,QVBoxLayout, QWidget, QDesktopWidget, QCheckBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from core.qm.qm import QM


#TODO
#validation for variables

class QMWidget(QWidget):
    
    warning_style = "QLabel { color : red;qproperty-alignment: AlignCenter; }"

    def __init__(self):
        super(QMWidget, self).__init__()

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
        self.setWindowIcon(QIcon("assets/images/win_icon.jpeg"))
        self.setMinimumWidth(500)

        
    def createHorizontalGroupBox(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QHBoxLayout()

     
        button = QPushButton("Minimize")
        button.setMaximumWidth(100)
        layout.addWidget(button)
        button.clicked.connect(self.minimize_clicked)

        show_check = QCheckBox("Show Steps")
        show_check.setMaximumWidth(100)
        layout.addWidget(show_check)
        self.horizontalGroupBox.setLayout(layout)


    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Input")
        layout = QFormLayout()
        self.mterm_edit = QLineEdit()
        self.mterm_edit.setPlaceholderText("space seperated list of minterms e.g 1 2 3 4")
        layout.addRow(QLabel("Minterms*:"), self.mterm_edit)

        #error label for minterms
        self.mt_err_label = QLabel()
        self.mt_err_label.setHidden(True)
        layout.addRow(self.mt_err_label)
        self.mt_err_label.setStyleSheet(self.warning_style)

        self.dcare_edit = QLineEdit()
        layout.addRow(QLabel("Don't cares:"),self.dcare_edit)
        self.dcare_edit.setPlaceholderText("space seperated list of don't cares e.g 0 5 7")
        

        #error label for don't cares
        self.dc_err_label = QLabel("Don't cares must be non negative integers")
        self.dc_err_label.setHidden(True)
        layout.addRow(self.dc_err_label)
        self.dc_err_label.setStyleSheet(self.warning_style)

        self.v_edit = QLineEdit()
        layout.addRow(QLabel("Variables:"),self.v_edit)
        self.v_edit.setPlaceholderText("space seperated list of characters e.g a b c")
        self.formGroupBox.setLayout(layout)

        #error label for variables
        self.v_err_label = QLabel('Variables must be non negative integers')
        self.v_err_label.setHidden(True)
        layout.addRow(self.v_err_label)
        self.v_err_label.setStyleSheet(self.warning_style)

    @staticmethod
    def representsInt(s):
        try: 
            int(s)
            return True
        except ValueError:
            return False

    def validate_input(self):
        #if there is no value in minterms indicate
        valid = True
        if not self.mterm_edit.text():
            self.mt_err_label.setText('Minterms field cannot be empty enter a value')
            self.mt_err_label.setHidden(False)
            valid = False

        #change to regex
        #if any of the values in minterms is not an intger indicate
        mts = self.mterm_edit.text().split(' ')
        for mt in mts:
            #if it is not a whitespace and it is not an integer 
            if (mt and not self.representsInt(mt)) or ((mt and self.representsInt(mt)) and int(mt) < 0):
                valid = False
                self.mt_err_label.setText('Minterms must be non negative integers')
                self.mt_err_label.setHidden(False)

        #if there any of the values in the dont cares is not an integer indicate
        dcs = self.dcare_edit.text().split(' ')
        for dc in dcs:
            if (dc and not self.representsInt(dc)) or (dc and self.representsInt(dc) and int(dc) < 0):
                valid = False
                self.dc_err_label.setHidden(False)

        #if the expression is valid hide all error labels

        if valid:
            self.mt_err_label.setHidden(True)
            self.dc_err_label.setHidden(True)
            self.v_err_label.setHidden(True)

        return valid
        
    def minimize_clicked(self):
        if self.validate_input():
            self.bigEditor.clear()

            mts = self.mterm_edit.text().split(' ')

            #remove any duplicates from the list
            #remove any non integers from the list
            mts = list(set(filter(lambda x: self.representsInt(x),mts)))

            dcs = self.dcare_edit.text().split(' ')

            #remove any non integers from the list
            dcs = list(set(filter(lambda x: self.representsInt(x),dcs)))

            vs = self.v_edit.text().split(' ')
            vs = list(filter(lambda x: x,vs))
            
            qm = QM(mts,dcs,vs)
            pis = qm.pis()
            qm.primary_epis()
            self.bigEditor.append('Prime Implicants')
            
            print(qm.procedure)
            for pi in pis:
                self.bigEditor.append(qm.procedure)
                self.bigEditor.append('\n')
                    
if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = QMWidget()
    window.show()
    sys.exit(app.exec_())
