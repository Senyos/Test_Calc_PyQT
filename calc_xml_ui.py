# Form implementation generated from reading ui file '.\calc.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(435, 340)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Calculator.sizePolicy().hasHeightForWidth())
        Calculator.setSizePolicy(sizePolicy)
        Calculator.setMinimumSize(QtCore.QSize(435, 340))
        Calculator.setMaximumSize(QtCore.QSize(435, 340))
        self.main_widget = QtWidgets.QWidget(parent=Calculator)
        self.main_widget.setGeometry(QtCore.QRect(10, 10, 421, 321))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_widget.sizePolicy().hasHeightForWidth())
        self.main_widget.setSizePolicy(sizePolicy)
        self.main_widget.setObjectName("main_widget")
        self.nums_widget = QtWidgets.QWidget(parent=self.main_widget)
        self.nums_widget.setGeometry(QtCore.QRect(0, 50, 201, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nums_widget.sizePolicy().hasHeightForWidth())
        self.nums_widget.setSizePolicy(sizePolicy)
        self.nums_widget.setObjectName("nums_widget")
        self.b_8 = QtWidgets.QPushButton(parent=self.nums_widget)
        self.b_8.setGeometry(QtCore.QRect(70, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_8.setFont(font)
        self.b_8.setObjectName("b_8")
        self.b_3 = QtWidgets.QPushButton(parent=self.nums_widget)
        self.b_3.setGeometry(QtCore.QRect(140, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_3.setFont(font)
        self.b_3.setObjectName("b_3")
        self.b_9 = QtWidgets.QPushButton(parent=self.nums_widget)
        self.b_9.setGeometry(QtCore.QRect(140, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_9.setFont(font)
        self.b_9.setObjectName("b_9")
        self.b_5 = QtWidgets.QPushButton(parent=self.nums_widget)
        self.b_5.setGeometry(QtCore.QRect(70, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_5.setFont(font)
        self.b_5.setObjectName("b_5")
        self.b_7 = QtWidgets.QPushButton(parent=self.nums_widget)
        self.b_7.setGeometry(QtCore.QRect(0, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_7.setFont(font)
        self.b_7.setObjectName("b_7")
        self.b_1 = QtWidgets.QPushButton(parent=self.nums_widget)
        self.b_1.setGeometry(QtCore.QRect(0, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_1.setFont(font)
        self.b_1.setObjectName("b_1")
        self.b_2 = QtWidgets.QPushButton(parent=self.nums_widget)
        self.b_2.setGeometry(QtCore.QRect(70, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_2.setFont(font)
        self.b_2.setObjectName("b_2")
        self.b_6 = QtWidgets.QPushButton(parent=self.nums_widget)
        self.b_6.setGeometry(QtCore.QRect(140, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_6.setFont(font)
        self.b_6.setObjectName("b_6")
        self.b_0 = QtWidgets.QPushButton(parent=self.nums_widget)
        self.b_0.setGeometry(QtCore.QRect(70, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_0.setFont(font)
        self.b_0.setObjectName("b_0")
        self.b_4 = QtWidgets.QPushButton(parent=self.nums_widget)
        self.b_4.setGeometry(QtCore.QRect(0, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_4.setFont(font)
        self.b_4.setObjectName("b_4")
        self.operators_widget = QtWidgets.QWidget(parent=self.main_widget)
        self.operators_widget.setGeometry(QtCore.QRect(220, 50, 201, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.operators_widget.sizePolicy().hasHeightForWidth())
        self.operators_widget.setSizePolicy(sizePolicy)
        self.operators_widget.setObjectName("operators_widget")
        self.b_bracket_right = QtWidgets.QPushButton(parent=self.operators_widget)
        self.b_bracket_right.setGeometry(QtCore.QRect(140, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_bracket_right.setFont(font)
        self.b_bracket_right.setObjectName("b_bracket_right")
        self.b_bracket_left = QtWidgets.QPushButton(parent=self.operators_widget)
        self.b_bracket_left.setGeometry(QtCore.QRect(70, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_bracket_left.setFont(font)
        self.b_bracket_left.setObjectName("b_bracket_left")
        self.b_dot = QtWidgets.QPushButton(parent=self.operators_widget)
        self.b_dot.setGeometry(QtCore.QRect(0, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_dot.setFont(font)
        self.b_dot.setObjectName("b_dot")
        self.b_minus = QtWidgets.QPushButton(parent=self.operators_widget)
        self.b_minus.setGeometry(QtCore.QRect(70, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_minus.setFont(font)
        self.b_minus.setObjectName("b_minus")
        self.b_times = QtWidgets.QPushButton(parent=self.operators_widget)
        self.b_times.setGeometry(QtCore.QRect(0, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_times.setFont(font)
        self.b_times.setObjectName("b_times")
        self.b_sqrt = QtWidgets.QPushButton(parent=self.operators_widget)
        self.b_sqrt.setGeometry(QtCore.QRect(70, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_sqrt.setFont(font)
        self.b_sqrt.setObjectName("b_sqrt")
        self.b_plus = QtWidgets.QPushButton(parent=self.operators_widget)
        self.b_plus.setGeometry(QtCore.QRect(0, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_plus.setFont(font)
        self.b_plus.setObjectName("b_plus")
        self.b_power = QtWidgets.QPushButton(parent=self.operators_widget)
        self.b_power.setGeometry(QtCore.QRect(0, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_power.setFont(font)
        self.b_power.setObjectName("b_power")
        self.b_divide = QtWidgets.QPushButton(parent=self.operators_widget)
        self.b_divide.setGeometry(QtCore.QRect(70, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_divide.setFont(font)
        self.b_divide.setObjectName("b_divide")
        self.b_equal = QtWidgets.QPushButton(parent=self.operators_widget)
        self.b_equal.setGeometry(QtCore.QRect(140, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_equal.setFont(font)
        self.b_equal.setStyleSheet("background-color: rgb(214, 60, 93);\n"
"color: rgb(255, 255, 255);")
        self.b_equal.setObjectName("b_equal")

        self.b_clear = QtWidgets.QPushButton(parent=self.operators_widget)
        self.b_clear.setGeometry(QtCore.QRect(140, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.b_clear.setFont(font)
        self.b_clear.setStyleSheet("background-color: rgb(214, 60, 93);\n"
"color: rgb(255, 255, 255);")
        self.b_clear.setObjectName("b_clear")

        self.calc_enter = QtWidgets.QTextEdit(parent=self.main_widget)
        self.calc_enter.setGeometry(QtCore.QRect(0, 0, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.calc_enter.setFont(font)
        self.calc_enter.setObjectName("calc_enter")

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Калькулятор"))
        self.b_8.setText(_translate("Calculator", "8"))
        self.b_3.setText(_translate("Calculator", "3"))
        self.b_9.setText(_translate("Calculator", "9"))
        self.b_5.setText(_translate("Calculator", "5"))
        self.b_7.setText(_translate("Calculator", "7"))
        self.b_1.setText(_translate("Calculator", "1"))
        self.b_2.setText(_translate("Calculator", "2"))
        self.b_6.setText(_translate("Calculator", "6"))
        self.b_0.setText(_translate("Calculator", "0"))
        self.b_4.setText(_translate("Calculator", "4"))
        self.b_bracket_right.setText(_translate("Calculator", ")"))
        self.b_bracket_left.setText(_translate("Calculator", "("))
        self.b_dot.setText(_translate("Calculator", ","))
        self.b_minus.setText(_translate("Calculator", "-"))
        self.b_times.setText(_translate("Calculator", "×"))
        self.b_sqrt.setText(_translate("Calculator", "√"))
        self.b_plus.setText(_translate("Calculator", "+"))
        self.b_power.setText(_translate("Calculator", "^"))
        self.b_divide.setText(_translate("Calculator", "/"))
        self.b_equal.setText(_translate("Calculator", "="))
        self.b_clear.setText(_translate("Calculator", "C"))