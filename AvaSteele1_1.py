def main():
    cookie_num = 0
    sandwich_num = 0
    water_num = 0

    choice = main_menu()

    while choice == 's':
        option = cart_menu()
        if option == '1':
            cookie_num += 1
            print('Added cookie')
            choice = main_menu()
        elif option == '2':
            sandwich_num += 1
            print('Added sandwich')
            choice = main_menu()
        elif option == '3':
            water_num += 1
            print('Added water')
            choice = main_menu()

    print('----------------------------------')
    print(f'({cookie_num}) - Cookie = ${cookie_num * 1.5:.2f}')
    print(f'({sandwich_num}) - Sandwich = ${sandwich_num * 4:.2f}')
    print(f'({water_num}) - Water = ${water_num * 1:.2f}')
    print('----------------------------------')
    print(f'GRAND TOTAL = ${cookie_num*1.5 + sandwich_num*4 + water_num*1:.2f}')
    print('----------------------------------')


def cart_menu():
    print('----CART MENU----')
    print('1: Cookie - $1.50')
    print('2: Sandwich - $4.00')
    print('3: Water - $1.00')
    choice = input('Item: ').strip()

    while choice != '1' and choice != '2' and choice != '3':
        choice = input('Invalid (1-3): ').strip()

    return choice


def main_menu():
    print('----MAIN MENU----')
    print('s: Shop')
    print('x: Exit')
    choice = input('Option: ').lower().strip()

    while choice != 's' and choice != 'x':
        choice = input('Invalid (s/x): ').lower().strip()

    return choice


main()
