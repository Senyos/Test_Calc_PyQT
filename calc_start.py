from calc_xml_ui import *
from calc_xml_ui import Ui_Calculator
from calc_func import *

def click_1():
    global calc_enter_text
    calc_enter_text += "1"
    ui.calc_enter.setText(calc_enter_text)
def click_2():
    global calc_enter_text
    calc_enter_text += "2"
    ui.calc_enter.setText(calc_enter_text)
def click_3():
    global calc_enter_text
    calc_enter_text += "3"
    ui.calc_enter.setText(calc_enter_text)
def click_4():
    global calc_enter_text
    calc_enter_text += "4"
    ui.calc_enter.setText(calc_enter_text)
def click_5():
    global calc_enter_text
    calc_enter_text += "5"
    ui.calc_enter.setText(calc_enter_text)
def click_6():
    global calc_enter_text
    calc_enter_text += "6"
    ui.calc_enter.setText(calc_enter_text)
def click_7():
    global calc_enter_text
    calc_enter_text += "7"
    ui.calc_enter.setText(calc_enter_text)
def click_8():
    global calc_enter_text
    calc_enter_text += "8"
    ui.calc_enter.setText(calc_enter_text)
def click_9():
    global calc_enter_text
    calc_enter_text += "9"
    ui.calc_enter.setText(calc_enter_text)
def click_0():
    global calc_enter_text
    calc_enter_text += "0"
    ui.calc_enter.setText(calc_enter_text)
def click_plus():
    global calc_enter_text
    calc_enter_text += " + "
    ui.calc_enter.setText(calc_enter_text)
def click_minus():
    global calc_enter_text
    calc_enter_text += " - "
    ui.calc_enter.setText(calc_enter_text)
def click_times():
    global calc_enter_text
    calc_enter_text += " × "
    ui.calc_enter.setText(calc_enter_text)
def click_divide():
    global calc_enter_text
    calc_enter_text += " / "
    ui.calc_enter.setText(calc_enter_text)
def click_power():
    global calc_enter_text
    calc_enter_text += "^"
    ui.calc_enter.setText(calc_enter_text)
def click_sqrt():
    global calc_enter_text
    calc_enter_text += "√"
    ui.calc_enter.setText(calc_enter_text)
def click_dot():
    global calc_enter_text
    calc_enter_text += ","
    ui.calc_enter.setText(calc_enter_text)
def click_bracket_left():
    global calc_enter_text
    calc_enter_text += "("
    ui.calc_enter.setText(calc_enter_text)
def click_bracket_right():
    global calc_enter_text
    calc_enter_text += ")"
    ui.calc_enter.setText(calc_enter_text)

calc_enter_text = ""
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operators = ['+', '-', '×', '/', '^', '√']

def click_equal():
    global calc_enter_text
    global numbers
    global operators
    num = ""
    result = ""
    flag = False
    flag_operator = False

    print(calc_enter_text)
    count = 0
    count_end = len(calc_enter_text)

    for _ in calc_enter_text:
        if _ in numbers:
            flag_operator = False
            num += _
        elif _ in operators:
            if flag:
                num += ")**(1/2)"
                flag = False
            if _ == operators[0] or _ == operators[1] or _ == operators[2] or _ == operators[3] or _ == operators[4]:
                flag_operator = True
            if _ == operators[2]:
                result = result + num + "*"
            elif _ == operators[4]:
                _ = "**"
                result = result + num + _
            elif _ == operators[5]:
                flag = True
                if flag_operator:
                    result = result + num + "("
                else: result = result + num + "*("
                flag_operator = False
            else: result = result + num + _
            num = ""
        elif _ == "(" or _ == ")":
            result = result + num + _
        else: pass
        count += 1
        if count >= count_end: result = result + num
        if count >= count_end and flag: result += ")**(1/2)"
    print(result)

    try:
        calc_enter_text = str(eval(result))
        ui.calc_enter.setText(calc_enter_text)
        calc_enter_text = ""
    except:
        calc_enter_text = ""
        ui.calc_enter.setText("Неправильный ввод данных")
        print("Неправильный ввод данных")


def click_clear():
    global calc_enter_text
    calc_enter_text = ""
    ui.calc_enter.setText(calc_enter_text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QDialog()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)

    ui.b_1.clicked.connect(click_1)
    ui.b_2.clicked.connect(click_2)
    ui.b_3.clicked.connect(click_3)
    ui.b_4.clicked.connect(click_4)
    ui.b_5.clicked.connect(click_5)
    ui.b_6.clicked.connect(click_6)
    ui.b_7.clicked.connect(click_7)
    ui.b_8.clicked.connect(click_8)
    ui.b_9.clicked.connect(click_9)
    ui.b_0.clicked.connect(click_0)
    ui.b_plus.clicked.connect(click_plus)
    ui.b_minus.clicked.connect(click_minus)
    ui.b_times.clicked.connect(click_times)
    ui.b_divide.clicked.connect(click_divide)
    ui.b_power.clicked.connect(click_power)
    ui.b_sqrt.clicked.connect(click_sqrt)
    ui.b_dot.clicked.connect(click_dot)
    ui.b_bracket_left.clicked.connect(click_bracket_left)
    ui.b_bracket_right.clicked.connect(click_bracket_right)
    ui.b_equal.clicked.connect(click_equal)
    ui.b_clear.clicked.connect(click_clear)

    Calculator.show()
    sys.exit(app.exec())
