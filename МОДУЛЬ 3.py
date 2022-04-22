
history_item = []
history_price = []


def main_menu():
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            top_up_your_account()
        elif choice == '2':
            shopping()
        elif choice == '3':
            shopping_history()
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')


def top_up_your_account():
    balance = 0
    saldo = int(input('Пополните счет. Введите сумму пополнения: '))
    balance += saldo
    return balance


def shopping():
    balance = top_up_your_account()
    price = 0
    price = int(input('Введите сумму покупки: '))
    if price > balance:
        print('Недостаточно денег. Пополните счет')
        main_menu()
    elif price <= balance:
        item_name = input('Введите название товара: ')
        balance -= price
        print('Ваш баланс: ', balance)
        history_item.append(item_name)
        history_price.append(price)
        print('Список покупок:\n', history_item)
    else:
        print('Обратитесь в техподдержку')
        # return item_name, price


def shopping_history():
    dict_history = dict(zip(history_item, history_price))
    print('История покупок:\n', dict_history)


main_menu()
