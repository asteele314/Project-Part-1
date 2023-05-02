from view import *
from PyQt5.QtWidgets import *
import csv


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
        self.label_Bottom.setHidden(True)
        self.label_Input.setHidden(True)
        self.label_Shop.setHidden(True)
        self.label_Exit.setHidden(True)
        self.label_BottomDots.setHidden(True)
        self.label_MiddleDots.setHidden(True)
        self.label_TopDots.setHidden(True)
        self.lineEdit_Input.setHidden(True)
        self.label_Cookie.setHidden(True)
        self.label_Water.setHidden(True)
        self.label_Sandwich.setHidden(True)
        self.button_Enter.setHidden(True)
        self.button_Enter_2.setHidden(True)
        self.label_CartInput.setHidden(True)
        self.lineEdit_CartInput.setHidden(True)
        self.label_BottomLabels.setHidden(True)

        self.button_Enter.clicked.connect(lambda: self.enter())
        self.button_Enter_2.clicked.connect(lambda: self.enter2())

        self.main_menu()

    def main_menu(self) -> None:
        """
        Displays beginning Main Menu screen with options to go to Cart Menu screen or to Final Total screen.
        """
        self.label_Title.setHidden(False)
        self.label_Title.setText('MAIN MENU')
        self.label_Shop.setHidden(False)
        self.label_Exit.setHidden(False)
        self.label_Input.setHidden(False)
        self.lineEdit_Input.setHidden(False)
        self.button_Enter.setHidden(False)
        self.label_Bottom.setText('')

        self.label_Bottom.setHidden(True)
        self.label_BottomDots.setHidden(True)
        self.label_MiddleDots.setHidden(True)
        self.label_TopDots.setHidden(True)
        self.label_Cookie.setHidden(True)
        self.label_Sandwich.setHidden(True)
        self.label_Water.setHidden(True)
        self.label_CartInput.setHidden(True)
        self.lineEdit_CartInput.setHidden(True)
        self.button_Enter_2.setHidden(True)
        self.label_BottomLabels.setHidden(True)

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
        self.label_Bottom.setHidden(True)
        self.label_Input.setHidden(True)
        self.label_Shop.setHidden(True)
        self.label_Exit.setHidden(True)
        self.label_BottomDots.setHidden(True)
        self.label_MiddleDots.setHidden(True)
        self.label_TopDots.setHidden(True)
        self.lineEdit_Input.setHidden(True)
        self.button_Enter.setHidden(True)
        self.label_BottomLabels.setHidden(True)

        self.label_Title.setHidden(False)
        self.label_Title.setText('CART MENU')
        self.label_Water.setHidden(False)
        self.label_Cookie.setHidden(False)
        self.label_Sandwich.setHidden(False)
        self.label_CartInput.setHidden(False)
        self.lineEdit_CartInput.setHidden(False)
        self.button_Enter_2.setHidden(False)

    def final_total(self) -> None:
        """
        Displays the final screen with total numbers of foods ordered and grand total of the cost and writes orders to a csv file.
        """
        self.label_Title.setHidden(True)
        self.label_Input.setHidden(True)
        self.lineEdit_Input.setHidden(True)
        self.label_CartInput.setHidden(True)
        self.lineEdit_CartInput.setHidden(True)
        self.label_Cookie.setHidden(True)
        self.label_Water.setHidden(True)
        self.label_Sandwich.setHidden(True)
        self.button_Enter.setHidden(True)
        self.button_Enter_2.setHidden(True)
        self.label_Bottom.setText('')

        self.label_TopDots.setHidden(False)
        self.label_MiddleDots.setHidden(False)
        self.label_BottomDots.setHidden(False)
        self.label_Shop.setHidden(False)
        self.label_Exit.setHidden(False)
        self.label_BottomLabels.setHidden(False)
        self.label_Bottom.setHidden(False)

        self.label_Shop.setText(f'({self.cookie_num}) - Cookie = ${self.cookie_num * 1.5:.2f}')
        self.label_Exit.setText(f'({self.sandwich_num}) - Sandwich = ${self.sandwich_num * 4:.2f}')
        self.label_BottomLabels.setText(f'({self.water_num}) - Water = ${self.water_num * 1:.2f}')
        self.label_Bottom.setText(f'GRAND TOTAL = ${self.cookie_num*1.5 + self.sandwich_num*4 + self.water_num*1:.2f}')

        pricerow = [f'${self.cookie_num*1.5:.2f}', f'${self.sandwich_num*4:.2f}', f'${self.water_num*1:.2f}']
        with open('orders.csv', 'a', newline='') as ordersfile:
            writer = csv.DictWriter(ordersfile, fieldnames=['Cookie Number', 'Cookie Price',
                                                            'Sandwich Number', 'Sandwich Price',
                                                            'Water Number', 'Water Price'])
            writer.writerow({'Cookie Number': self.cookie_num, 'Cookie Price': pricerow[0],
                             'Sandwich Number': self.sandwich_num, 'Sandwich Price': pricerow[1],
                             'Water Number': self.water_num, 'Water Price': pricerow[2]})

    def enter2(self) -> None:
        """
        Determines which food was ordered and updates total numbers.
        """
        try:
            if self.lineEdit_CartInput.text().strip() == '1':
                self.lineEdit_CartInput.setText('')
                self.label_Bottom.setHidden(False)
                self.label_Bottom.setText('Added Cookie')
                self.cookie_num += 1
            elif self.lineEdit_CartInput.text().strip() == '2':
                self.lineEdit_CartInput.setText('')
                self.label_Bottom.setHidden(False)
                self.label_Bottom.setText('Added Sandwich')
                self.sandwich_num += 1
            elif self.lineEdit_CartInput.text().strip() == '3':
                self.lineEdit_CartInput.setText('')
                self.label_Bottom.setHidden(False)
                self.label_Bottom.setText('Added Water')
                self.water_num += 1
            else:
                raise ZeroDivisionError
        except ZeroDivisionError:
            self.lineEdit_CartInput.setText('')
            self.label_Bottom.setHidden(False)
            self.label_Bottom.setText('Invalid Input!  Please Enter 1, 2, or 3.')
        else:
            self.main_menu()
