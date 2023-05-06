from view import *
from PyQt5.QtWidgets import *


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes numbers of foods ordered and sets up display window.
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.cookie_num = 0
        self.sandwich_num = 0
        self.water_num = 0

        self.label_Title.setHidden(True)
        self.label_Cookie.setHidden(True)
        self.label_Sandwich.setHidden(True)
        self.label_Input.setHidden(True)
        self.lineEdit_Input.setHidden(True)
        self.label_Bottom.setHidden(True)
        self.label_BottomDots.setHidden(True)
        self.label_MiddleDots.setHidden(True)
        self.label_TopDots.setHidden(True)
        self.button_Enter.setHidden(True)
        self.button_Enter_2.setHidden(True)
        self.label_Water.setHidden(True)
        self.label_Exit.setHidden(True)
        self.label_Shop.setHidden(True)
        self.lineEdit_WaterInput.setHidden(True)
        self.lineEdit_CookieInput.setHidden(True)
        self.lineEdit_SandwichInput.setHidden(True)
        self.label_CookieEnd.setHidden(True)
        self.label_SandwichEnd.setHidden(True)
        self.label_WaterEnd.setHidden(True)
        self.label_Subtotal.setHidden(True)
        self.label_Tax.setHidden(True)

        self.button_Enter.clicked.connect(lambda: self.enter())
        self.button_Enter_2.clicked.connect(lambda: self.enter2())

        self.main_menu()

    def main_menu(self) -> None:
        """
        Displays beginning Main Menu screen with options to go to Cart Menu screen or to Final Total screen.
        """
        self.label_Cookie.setHidden(True)
        self.label_Sandwich.setHidden(True)
        self.label_BottomDots.setHidden(True)
        self.label_MiddleDots.setHidden(True)
        self.label_TopDots.setHidden(True)
        self.button_Enter_2.setHidden(True)
        self.label_Water.setHidden(True)
        self.lineEdit_WaterInput.setHidden(True)
        self.lineEdit_CookieInput.setHidden(True)
        self.lineEdit_SandwichInput.setHidden(True)
        self.label_CookieEnd.setHidden(True)
        self.label_SandwichEnd.setHidden(True)
        self.label_WaterEnd.setHidden(True)
        self.label_Subtotal.setHidden(True)
        self.label_Tax.setHidden(True)

        self.label_Title.setHidden(False)
        self.label_Title.setText('MAIN MENU')
        self.label_Shop.setHidden(False)
        self.label_Exit.setHidden(False)
        self.label_Input.setHidden(False)
        self.lineEdit_Input.setHidden(False)
        self.button_Enter.setHidden(False)
        self.label_Bottom.setText('')

    def enter(self) -> None:
        """
        Determines whether to move from Main Menu screen to Cart Menu screen or to Final Total screen
        and moves to that screen.
        """
        try:
            if self.lineEdit_Input.text().strip().lower() == 's':
                self.lineEdit_Input.setText('')
                self.label_Bottom.setText('')
                self.label_Bottom.setHidden(True)
                self.cart_menu()
            elif self.lineEdit_Input.text().strip().lower() == 'x':
                self.lineEdit_Input.setText('')
                self.label_Bottom.setText('')
                self.label_Bottom.setHidden(True)
                self.final_total()
            else:
                raise ZeroDivisionError
        except ZeroDivisionError:
            self.lineEdit_Input.setText('')
            self.label_Bottom.setHidden(False)
            self.label_Bottom.setText('Invalid Input!  Please Enter s or x.')

    def cart_menu(self) -> None:
        """
        Displays the foods that are available to order and allows them to be selected.
        """
        self.label_Input.setHidden(True)
        self.lineEdit_Input.setHidden(True)
        self.label_Bottom.setHidden(True)
        self.label_BottomDots.setHidden(True)
        self.label_MiddleDots.setHidden(True)
        self.label_TopDots.setHidden(True)
        self.button_Enter.setHidden(True)
        self.label_Exit.setHidden(True)
        self.label_Shop.setHidden(True)
        self.label_CookieEnd.setHidden(True)
        self.label_SandwichEnd.setHidden(True)
        self.label_WaterEnd.setHidden(True)
        self.label_Subtotal.setHidden(True)
        self.label_Tax.setHidden(True)

        self.label_Title.setHidden(False)
        self.label_Title.setText('CART MENU')
        self.label_Cookie.setHidden(False)
        self.label_Sandwich.setHidden(False)
        self.label_Water.setHidden(False)
        self.lineEdit_SandwichInput.setHidden(False)
        self.lineEdit_CookieInput.setHidden(False)
        self.lineEdit_WaterInput.setHidden(False)
        self.button_Enter_2.setHidden(False)

    def enter2(self) -> None:
        """
        Determines which food was ordered and updates total numbers.
        """
        try:
            cookie_input = self.lineEdit_CookieInput.text().strip()
            sandwich_input = self.lineEdit_SandwichInput.text().strip()
            water_input = self.lineEdit_WaterInput.text().strip()

            if cookie_input == '':
                num_cookies = 0
            else:
                num_Cookies = float(cookie_input)
                num_cookies = int(num_Cookies)

            if sandwich_input == '':
                num_sandwiches = 0
            else:
                num_Sandwiches = float(sandwich_input)
                num_sandwiches = int(num_Sandwiches)

            if water_input == '':
                num_water = 0
            else:
                num_Water = float(water_input)
                num_water = int(num_Water)

        except ZeroDivisionError:
            self.lineEdit_CookieInput.setText('')
            self.lineEdit_SandwichInput.setText('')
            self.lineEdit_WaterInput.setText('')
            self.label_Bottom.setHidden(False)
            self.label_Bottom.setText('Invalid Input!  Please Enter a Number.')

        except TypeError:
            self.lineEdit_CookieInput.setText('')
            self.lineEdit_SandwichInput.setText('')
            self.lineEdit_WaterInput.setText('')
            self.label_Bottom.setHidden(False)
            self.label_Bottom.setText('Invalid Input!  Please Enter a Number.')

        except:
            self.lineEdit_CookieInput.setText('')
            self.lineEdit_SandwichInput.setText('')
            self.lineEdit_WaterInput.setText('')
            self.label_Bottom.setHidden(False)
            self.label_Bottom.setText('Invalid Input!  Please Enter a Number.')

        else:
            self.lineEdit_CookieInput.setText('')
            self.lineEdit_SandwichInput.setText('')
            self.lineEdit_WaterInput.setText('')

            self.cookie_num += num_cookies
            self.sandwich_num += num_sandwiches
            self.water_num += num_water

            self.main_menu()

    def final_total(self) -> None:
        """
        Displays the final screen with total numbers of foods ordered and grand total of the cost.
        """
        self.label_Title.setHidden(True)
        self.label_Cookie.setHidden(True)
        self.label_Sandwich.setHidden(True)
        self.label_Input.setHidden(True)
        self.lineEdit_Input.setHidden(True)
        self.button_Enter.setHidden(True)
        self.button_Enter_2.setHidden(True)
        self.label_Water.setHidden(True)
        self.label_Exit.setHidden(True)
        self.label_Shop.setHidden(True)
        self.lineEdit_WaterInput.setHidden(True)
        self.lineEdit_CookieInput.setHidden(True)
        self.lineEdit_SandwichInput.setHidden(True)

        self.label_BottomDots.setHidden(False)
        self.label_MiddleDots.setHidden(False)
        self.label_TopDots.setHidden(False)
        self.label_Bottom.setHidden(False)
        self.label_CookieEnd.setHidden(False)
        self.label_SandwichEnd.setHidden(False)
        self.label_WaterEnd.setHidden(False)
        self.label_Subtotal.setHidden(False)
        self.label_Tax.setHidden(False)

        cookie_price = self.cookie_num * 1.5
        sandwich_price = self.sandwich_num * 4
        water_price = self.water_num * 1
        subtotal = cookie_price + sandwich_price + water_price
        tax = subtotal * 0.07
        total = subtotal + tax

        self.label_CookieEnd.setText(f'({self.cookie_num}) - Cookies = ${cookie_price:.2f}')
        self.label_SandwichEnd.setText(f'({self.sandwich_num}) - Sandwiches = ${sandwich_price:.2f}')
        self.label_WaterEnd.setText(f'({self.water_num}) - Waters = ${water_price:.2f}')
        self.label_Subtotal.setText(f'SUBTOTAL = ${subtotal:.2f}')
        self.label_Tax.setText(f'7% Sales Tax = ${tax:.2f}')
        self.label_Bottom.setText(f'GRAND TOTAL = ${total:.2f}')

def main() -> None:
    application = QApplication([])
    window = Controller()
    window.show()
    application.exec_()


if __name__ == '__main__':
    main()