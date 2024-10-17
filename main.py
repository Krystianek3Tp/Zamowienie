import sys
from contextlib import nullcontext

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.sButton.toggled.connect(self.calculate)
        self.ui.mButton.toggled.connect(self.calculate)
        self.ui.lButton.toggled.connect(self.calculate)
        self.ui.xlButton.toggled.connect(self.calculate)
        self.ui.kartaButton.toggled.connect(self.calculate)
        self.ui.blikButton.toggled.connect(self.calculate)
        self.ui.odbiorButton.toggled.connect(self.calculate)
        self.show()

    def calculate(self):
        rozmiar = "nie wybrano"
        metodaPlatnosci = "nie wybrano"
        if self.ui.sButton.isChecked():
            rozmiar = "S"
        elif self.ui.mButton.isChecked():
            rozmiar = "M"
        elif self.ui.lButton.isChecked():
            rozmiar = "L"
        else:
            rozmiar = "XL"

        if self.ui.kartaButton.isChecked():
            metodaPlatnosci = "Karta"
        if self.ui.blikButton.isChecked():
            metodaPlatnosci = "BLIK"
        if self.ui.odbiorButton.isChecked():
            metodaPlatnosci = "Płatność przy odbiorze"

        self.ui.outputLabel.setText(f"Rozmiar: {rozmiar}, Metoda płatności: {metodaPlatnosci}")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec())

