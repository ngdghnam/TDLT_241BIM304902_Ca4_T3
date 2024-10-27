from PySide6.QtWidgets import QWidget
from py_ui.mainWidget import Ui_widget
from functions.giai_ptb1 import Ptb1_Window
from functions.giai_ptb2 import Ptb2_Window
from functions.giai_ptb3 import Ptb3_Window
from functions.find_gcd import Gcd_Window
from functions.find_lcm import Lcm_Window
from functions.find_chinhhop import Find_chinhHop
from functions.find_tohop import Find_toHop
from functions.find_tongDaySo import Find_Summation
import math 

class Widget(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Modern Calculator")
 
        # Calling Button
        # Button Number 
        self.button_0.clicked.connect(self.on_button_click)
        self.button_1.clicked.connect(self.on_button_click)
        self.button_2.clicked.connect(self.on_button_click)
        self.button_3.clicked.connect(self.on_button_click)
        self.button_4.clicked.connect(self.on_button_click)
        self.button_5.clicked.connect(self.on_button_click)
        self.button_6.clicked.connect(self.on_button_click)
        self.button_7.clicked.connect(self.on_button_click)
        self.button_8.clicked.connect(self.on_button_click)
        self.button_9.clicked.connect(self.on_button_click)

        # Multiply, divide, plus, minus, equal, del 
        self.button_plus.clicked.connect(self.on_button_click)
        self.button_minus.clicked.connect(self.on_button_click)
        self.button_multiply.clicked.connect(self.on_button_click)
        self.button_divide.clicked.connect(self.on_button_click)
        self.button_equal.clicked.connect(self.on_button_click)
        self.button_del.clicked.connect(self.on_button_click)
        self.button_dot.clicked.connect(self.on_button_click)

        # pow, factorial 
        self.button_pow.clicked.connect(self.on_button_click)
        self.button_factor.clicked.connect(self.on_factorial_click)
        self.button_log.clicked.connect(self.on_log_click)
        
        # sin, cos, tan, cotan 
        self.button_sin.clicked.connect(self.on_sin_click)
        self.button_cos.clicked.connect(self.on_cos_click)
        self.button_tan.clicked.connect(self.on_tan_click)
        self.button_pi.clicked.connect(self.on_cotan_click)

        # to BIN
        self.button_e.clicked.connect(self.on_e_click)

        # Hoán vị 
        self.button_hoanvi.clicked.connect(self.on_hvi_click)

        # abs, sqrt
        self.button_abs.clicked.connect(self.on_abs_click)
        self.button_abs_2.clicked.connect(self.on_sqrt_click)

        # Thừa số nguyên tố 
        self.button_thuasonguyento.clicked.connect(self.on_tsnt_click)

        # GCD, LCM
        self.button_gcd.clicked.connect(self.open_gcd_window)
        self.button_lcm.clicked.connect(self.open_lcm_window)

        # Open new window to solve ptb1, ptb2, ptb3 
        self.button_ptb1.clicked.connect(self.open_ptb1_window)
        self.button_ptb2.clicked.connect(self.open_ptb2_window)
        self.button_ptb3.clicked.connect(self.open_ptb3_window)

        # Tổ hợp, chỉnh hợp, tổng dãy số 
        self.button_chinh_hop.clicked.connect(self.open_chinhHop_window)
        self.button_to_hop.clicked.connect(self.open_toHop_window)
        self.button_sum.clicked.connect(self.open_summation_window)

    # Simple Calculate function
    def on_button_click(self):
        button = self.sender()
        current_text = self.main_label.text()

        if current_text == "0":
            current_text = ""
        
        if button.text() == "=":
            try:
                result = str(eval(current_text))
                self.main_label.setText(result)
                self.main_label_2.setText(current_text + button.text())
            except ZeroDivisionError:
                self.main_label.setText("Error: Division by Zero")
            except Exception as e:
                self.main_label.setText("Error: Invalid expression")

        else: 
            self.main_label.setText(current_text + button.text())
            self.main_label_2.setText(current_text + button.text())

        if button.text() == "DEL":
            self.main_label.setText("0")
            self.main_label_2.setText("")
    
    # Logarithm 
    def on_log_click(self):
        current_text = self.main_label.text()
        try: 
            number = float(current_text)
            if number <= 0: 
                self.main_label("Error: Negative Number")
            else: 
                result = math.log(number)
                self.main_label.setText(str(result))
                self.main_label_2.setText(f"log({current_text})")
        except ValueError:
            self.main_label.setText("Error: Invalid Input")

    # Factorial 
    def on_factorial_click(self):
        current_text = self.main_label.text()
        try: 
            number = int(current_text)
            if number < 0: 
                self.main_label.setText("Error: Negative number")
            else: 
                result = math.factorial(number)
                self.main_label.setText(str(result))
                self.main_label_2.setText(f"{current_text}!")
        except ValueError: 
            self.main_label.setText("Error: Invalid Input!")

    # Sin, cos, tan, cotan 
    def on_sin_click(self):
        current_text = self.main_label.text()
        try: 
            degree = int(current_text)
            if degree < 0: 
                self.main_label.setText("Error: Negative number")
            else:
                radian = math.radians(degree)
                result = math.sin(radian)
                self.main_label.setText(str(result))
                self.main_label_2.setText(f"sin({degree})")
        except ValueError:
            self.main_label.setText("Error: Invalid Input!")

    def on_cos_click(self):
        current_text = self.main_label.text()
        try: 
            degree = int(current_text)
            if degree < 0: 
                self.main_label.setText("Error: Negative number")
            else:
                radian = math.radians(degree)
                result = math.cos(radian)
                self.main_label.setText(str(result))
                self.main_label_2.setText(f"cos({degree})")
        except ValueError:
            self.main_label.setText("Error: Invalid Input!")

    def on_tan_click(self):
        current_text = self.main_label.text()
        try: 
            degree = int(current_text)
            if degree < 0: 
                self.main_label.setText("Error: Negative number")
            else:
                radian = math.radians(degree)
                result = math.tan(radian)
                self.main_label.setText(str(result))
                self.main_label_2.setText(f"tan({degree})")
        except ValueError:
            self.main_label.setText("Error: Invalid Input!")
    
    def on_cotan_click(self):
        current_text = self.main_label.text()
        try: 
            degree = int(current_text)
            if degree < 0: 
                self.main_label.setText("Error: Negative number")
            else:
                radian = math.radians(degree)
                result = 1 / (math.tan(radian))
                self.main_label.setText(str(result))
                self.main_label_2.setText(f"cotan({degree})")
        except ValueError:
            self.main_label.setText("Error: Invalid Input!")


    # Hoán vị 
    def on_hvi_click(self):
        current_text = self.main_label.text()
        try:
            number = int(current_text)
            if number <= 0: 
                self.main_label.setText("Error: Negative number")
            else: 
                result = math.factorial(number)
                self.main_label.setText(str(result))
                self.main_label_2.setText(f"Hoan vi cua {current_text} = {result}")
        except ValueError: 
            self.main_label.setText("Error: Invalid Input!")

    # Abs 
    def on_abs_click(self):
        current_text = self.main_label.text()
        number = int(current_text)
        result = math.fabs(number)
        self.main_label.setText(str(result))
        self.main_label_2.setText(f"|{number}|")
    
    #sqrt 
    def on_sqrt_click(self):
        current_text = self.main_label.text()
        try: 
            number = int(current_text)
            if number <= 0: 
                self.main_label.setText("Error: Invalid number") 
            else:
                result = math.sqrt(number)
                self.main_label.setText(str(result))
                self.main_label_2.setText(f"√{number}")
        except ValueError:
            self.main_label.setText("Error: Invalid Input")

    # thua so nguyen to
    @staticmethod
    def PhanTichThuaSoNguyenTo(number):
        i = 2
        thua_so = []
        while i * i <= number:
            if number % i:
                i += 1
            else:
                number //= i
                thua_so.append(i)
        if number > 1:
            thua_so.append(number)
        return thua_so

    def on_tsnt_click(self):
        current_text = self.main_label.text()
        try: 
            number = int(current_text)
            if number < 2: 
                self.main_label.setText("Error: Invalid number")
            else: 
                result = self.PhanTichThuaSoNguyenTo(number)
                self.main_label.setText(f"{result}")
                self.main_label_2.setText(f"TSNT: {number}")
        except ValueError: 
            self.main_label.setText("Error: Invalid input")

    def open_gcd_window(self):
        self.gcd_ui = Gcd_Window()
        self.gcd_ui.show()

    def open_lcm_window(self):
        self.lcm_ui = Lcm_Window()
        self.lcm_ui.show()

    # BIN 
    def on_e_click(self):
        current_text = self.main_label.text()
        try:
            number = int(current_text)
            result = bin(number)
            self.main_label_2.setText(f"BIN({number})")
            self.main_label.setText(f"{result}")
        except ValueError:
            self.main_label.setText("Invalid")

    # Tổ hợp, chỉnh hợp, summation 
    def open_chinhHop_window(self):
        self.chinhHop_ui = Find_chinhHop()
        self.chinhHop_ui.show()

    def open_toHop_window(self):
        self.toHop_ui = Find_toHop()
        self.toHop_ui.show()

    def open_summation_window(self):
        self.summation_ui = Find_Summation()
        self.summation_ui.show()

    # Openning new window 
    def open_ptb1_window(self):
        self.ptb1_ui = Ptb1_Window()  # Initialize the UI for ptb1
        self.ptb1_ui.show()  # Show the new window

    def open_ptb2_window(self):
        self.ptb2_ui = Ptb2_Window()  # Initialize the UI for ptb2
        self.ptb2_ui.show()  # Show the new window

    def open_ptb3_window(self):
        self.ptb3_ui = Ptb3_Window()  # Initialize the UI for ptb3
        self.ptb3_ui.show()  # Show the new window