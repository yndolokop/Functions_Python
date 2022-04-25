
history_item = []  #  список товаров
history_price = []  # список цен
# sum_price = []
balance_sum = []  #  хранит суммы пополнений


def main_menu():
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню: ')

        if choice == '1':
            balance = int(input('Пополните счет. Введите сумму пополнения: '))
            result = bal(balance)
        elif choice == '2':
            price = int(input('Введите сумму покупки: '))
            if price > result:
                print('Недостаточно денег. Пополните счет')
            elif price <= result:
                item_name = input('Введите название товара: ')
                shopping(result, price)
                history_item.append(item_name)
                history_price.append(price)
                print('Список покупок:\n', history_item)
            else:
                print('Обратитесь в техподдержку')
        elif choice == '3':
            shopping_history()
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
    return


def bal(val):  # Функция будет принимать переменную balance и в случае повторного пополнения
    new_balance = 0
    balance_sum.append(val)
    for i in balance_sum:
        new_balance += i  # суммировать их в переменную new_balance
    print(new_balance)
    return new_balance


def shopping(val, price):  # функция будет принимать new_balance
    ostatok = 0
    sum_price.append(price)
    ostatok = val - sum(sum_price)  #  и вычитать из нее сумму покупок записывая в ostatok
    print('Ваш баланс: ', ostatok)
    return ostatok



def shopping_history():  #  функция печатает историю покупок из двух списков: названий товара и цен
    dict_history = dict(zip(history_item, history_price))
    print('История покупок:\n', dict_history)


main_menu()
