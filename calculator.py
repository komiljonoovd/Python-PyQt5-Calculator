import os

os.system('cls')

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")

        self.v_label_box = QHBoxLayout()

        self.h_box1 = QHBoxLayout()

        self.h_box2 = QHBoxLayout()

        self.h_box3 = QHBoxLayout()

        self.h_box4 = QHBoxLayout()

        self.h_box5 = QHBoxLayout()

        self.h_box6 = QHBoxLayout()

        self.v_box = QVBoxLayout()

        self.label1 = QLabel('0')

        self.label2 = QLabel('0')

        self.label1.setStyleSheet('color : white; font-weight: bold; font : 40px')

        self.label2.setStyleSheet('color : white; font-weight: bold; font : 20px')

        self.btn_ac = QPushButton(self)
        self.btn_ac.setText('AC')
        self.btn_ac.setFixedSize(70, 70)
        self.btn_ac.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color : 	#B7B7B7 ; font: 20px")

        self.btn_ps = QPushButton(self)
        self.btn_ps.setText('+/-')
        self.btn_ps.setFixedSize(70, 70)
        self.btn_ps.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :		#B7B7B7; font: 20px")

        self.btn_percent = QPushButton(self)
        self.btn_percent.setText('%')
        self.btn_percent.setFixedSize(70, 70)
        self.btn_percent.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :		#B7B7B7 ; font: 20px")

        self.btn_divide = QPushButton(self)
        self.btn_divide.setText('/')
        self.btn_divide.setFixedSize(70, 70)
        self.btn_divide.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :	#EABF29 ; font: 20px;color: white")

        self.btn_7 = QPushButton(self)
        self.btn_7.setText('7')
        self.btn_7.setFixedSize(70, 70)
        self.btn_7.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :	#555555	 ; font: 20px;color: white")

        self.btn_8 = QPushButton(self)
        self.btn_8.setText('8')
        self.btn_8.setFixedSize(70, 70)
        self.btn_8.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :		#515151; font: 20px;color: white")

        self.btn_9 = QPushButton(self)
        self.btn_9.setText('9')
        self.btn_9.setFixedSize(70, 70)
        self.btn_9.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :		#515151; font: 20px;color: white")

        self.btn_multiply = QPushButton(self)
        self.btn_multiply.setText('*')
        self.btn_multiply.setFixedSize(70, 70)
        self.btn_multiply.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :	#F4C633 ; font: 20px;color: white")

        self.btn_4 = QPushButton(self)
        self.btn_4.setText('4')
        self.btn_4.setFixedSize(70, 70)
        self.btn_4.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :		#515151; font: 20px;color: white")

        self.btn_5 = QPushButton(self)
        self.btn_5.setText('5')
        self.btn_5.setFixedSize(70, 70)
        self.btn_5.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :		#515151; font: 20px;color :white")

        self.btn_6 = QPushButton(self)
        self.btn_6.setText('6')
        self.btn_6.setFixedSize(70, 70)
        self.btn_6.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :		#515151; font: 20px;color: white")

        self.btn_minus = QPushButton(self)
        self.btn_minus.setText('-')
        self.btn_minus.setFixedSize(70, 70)
        self.btn_minus.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :	#F4C633; font: 20px;color :white")

        self.btn_1 = QPushButton(self)
        self.btn_1.setText('1')
        self.btn_1.setFixedSize(70, 70)
        self.btn_1.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :		#515151; font: 20px;color: white")

        self.btn_2 = QPushButton(self)
        self.btn_2.setText('2')
        self.btn_2.setFixedSize(70, 70)
        self.btn_2.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :		#515151; font: 20px;color: white")

        self.btn_3 = QPushButton(self)
        self.btn_3.setText('3')
        self.btn_3.setFixedSize(70, 70)
        self.btn_3.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :		#515151; font: 20px;color :white")

        self.btn_plus = QPushButton(self)
        self.btn_plus.setText('+')
        self.btn_plus.setFixedSize(70, 70)
        self.btn_plus.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :	#F4C633 ; font: 20px;color :white")

        self.btn_0 = QPushButton(self)
        self.btn_0.setText(' 0               ')
        self.btn_0.setFixedSize(150, 70)
        self.btn_0.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :		#515151; font: 20px;color: white")

        self.btn_comma = QPushButton(self)
        self.btn_comma.setText(',')
        self.btn_comma.setFixedSize(70, 70)
        self.btn_comma.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :		#515151; font: 20px;color: white")

        self.btn_result = QPushButton(self)
        self.btn_result.setText('=')
        self.btn_result.setFixedSize(70, 70)
        self.btn_result.setStyleSheet(
            "border-radius: 35; border: 2px solid black; font-weight: bold;background-color :	#F4C633; font: 20px;color   :white")

        self.v_label_box.addStretch()
        self.v_label_box.addWidget(self.label2)

        self.h_box1.addStretch()
        self.h_box1.addWidget(self.label1)

        self.h_box2.addWidget(self.btn_ac)
        self.h_box2.addWidget(self.btn_ps)
        self.h_box2.addWidget(self.btn_percent)
        self.h_box2.addWidget(self.btn_divide)

        self.h_box3.addWidget(self.btn_7)
        self.h_box3.addWidget(self.btn_8)
        self.h_box3.addWidget(self.btn_9)
        self.h_box3.addWidget(self.btn_multiply)

        self.h_box4.addWidget(self.btn_4)
        self.h_box4.addWidget(self.btn_5)
        self.h_box4.addWidget(self.btn_6)
        self.h_box4.addWidget(self.btn_minus)

        self.h_box5.addWidget(self.btn_1)
        self.h_box5.addWidget(self.btn_2)
        self.h_box5.addWidget(self.btn_3)
        self.h_box5.addWidget(self.btn_plus)

        self.h_box6.addWidget(self.btn_0)
        self.h_box6.addWidget(self.btn_comma)
        self.h_box6.addWidget(self.btn_result)

        self.v_box.addLayout(self.v_label_box)
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addLayout(self.h_box5)
        self.v_box.addLayout(self.h_box6)

        self.setStyleSheet('background-color: black')

        self.setLayout(self.v_box)

        self.btn_ac.clicked.connect(self.press_btn_ac)

        self.btn_1.clicked.connect(self.press_btn1)
        self.btn_2.clicked.connect(self.press_btn2)
        self.btn_3.clicked.connect(self.press_btn3)
        self.btn_4.clicked.connect(self.press_btn4)
        self.btn_5.clicked.connect(self.press_btn5)
        self.btn_6.clicked.connect(self.press_btn6)
        self.btn_7.clicked.connect(self.press_btn7)
        self.btn_8.clicked.connect(self.press_btn8)
        self.btn_9.clicked.connect(self.press_btn9)
        self.btn_0.clicked.connect(self.press_btn0)
        self.btn_plus.clicked.connect(self.press_btn_plus)
        self.btn_minus.clicked.connect(self.press_btn_minus)
        self.btn_multiply.clicked.connect(self.press_btn_multiply)
        self.btn_divide.clicked.connect(self.press_btn_divide)
        self.btn_result.clicked.connect(self.press_btn_result)
        self.btn_comma.clicked.connect(self.press_btn_comma)
        self.btn_percent.clicked.connect(self.press_btn_percent)

        self.show()

    def press_btn_percent(self):
        answer = self.label1.text()

    def press_btn_ac(self):
        self.label1.setText('0')
        self.label2.setText('0')

    def press_btn1(self):
        if self.label1.text() == '0':
            self.label1.setText('')
            self.label1.setText(self.label1.text() + '1')
        else:
            self.label1.setText(self.label1.text() + '1')

    def press_btn2(self):
        if self.label1.text() == '0':
            self.label1.setText('')
            self.label1.setText(self.label1.text() + '2')
        else:
            self.label1.setText(self.label1.text() + '2')

    def press_btn3(self):
        if self.label1.text() == '0':
            self.label1.setText('')
            self.label1.setText(self.label1.text() + '3')
        else:
            self.label1.setText(self.label1.text() + '3')

    def press_btn4(self):
        if self.label1.text() == '0':
            self.label1.setText('')
            self.label1.setText(self.label1.text() + '4')
        else:
            self.label1.setText(self.label1.text() + '4')

    def press_btn5(self):
        if self.label1.text() == '0':
            self.label1.setText('')
            self.label1.setText(self.label1.text() + '5')
        else:
            self.label1.setText(self.label1.text() + '5')

    def press_btn6(self):
        if self.label1.text() == '0':
            self.label1.setText('')
            self.label1.setText(self.label1.text() + '6')
        else:
            self.label1.setText(self.label1.text() + '6')

    def press_btn7(self):
        if self.label1.text() == '0':
            self.label1.setText('')
            self.label1.setText(self.label1.text() + '7')
        else:
            self.label1.setText(self.label1.text() + '7')

    def press_btn8(self):
        if self.label1.text() == '0':
            self.label1.setText('')
            self.label1.setText(self.label1.text() + '8')
        else:
            self.label1.setText(self.label1.text() + '8')

    def press_btn9(self):
        if self.label1.text() == '0':
            self.label1.setText('')
            self.label1.setText(self.label1.text() + '9')
        else:
            self.label1.setText(self.label1.text() + '9')

    def press_btn0(self):
        if self.label1.text() != '0':
            self.label1.setText(self.label1.text() + '0')

    def press_btn_plus(self):
        if self.label1.text()[-1] not in [',', '*', '/', '+', '-']:
            self.label1.setText(self.label1.text() + '+')

    def press_btn_minus(self):
        if self.label1.text()[-1] not in [',', '*', '/', '+', '-']:
            self.label1.setText(self.label1.text() + '-')

    def press_btn_multiply(self):
        if self.label1.text()[-1] not in [',', '*', '/', '+', '-']:
            self.label1.setText(self.label1.text() + '*')

    def press_btn_divide(self):
        if self.label1.text()[-1] not in [',', '*', '/', '+', '-']:
            self.label1.setText(self.label1.text() + '/')

    def press_btn_result(self):
        jami = self.label1.text()
        jami = eval(jami)
        self.label2.setText(self.label1.text())
        self.label1.setText(str(jami))

    def press_btn_comma(self):
        if self.label1.text()[-1] not in [',', '*', '/', '+', '-']:
            self.label1.setText(self.label1.text() + ',')


app = QApplication(sys.argv)
win = MainWindow()
sys.exit(app.exec_())
