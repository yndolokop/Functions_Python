
history_item = []  #  список товаров
history_price = []  # список цен
balance_sum = []  #  хранит суммы пополнений


def main_menu():
    global result
    result = 0
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            balance = int(input('Пополните счет. Введите сумму пополнения: '))
            balance_sum.clear()
            balance_sum.append(result)
            print('Ваш баланс: ')
            result = bal(balance)
        elif choice == '2':
            price = int(input('Введите сумму покупки: '))
            if price > result:
                print('Недостаточно денег. Пополните счет')
            elif price <= result:
                item_name = input('Введите название товара: ')
                result = result - price  # и вычитать из нее сумму покупок перезаписав в result
                print(balance_sum)
                print('Остаток на счету: ', result)
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
            return result


def bal(val):  # Функция будет принимать переменную balance и в случае повторного пополнения
    new_balance = 0
    balance_sum.append(val)
    for i in balance_sum:
        new_balance += i  # суммировать их в переменную new_balance
    print(new_balance)
    return new_balance


def shopping_history():  #  функция печатает историю покупок из двух списков: названий товара и цен
    dict_history = dict(zip(history_item, history_price))
    print('История покупок:\n', dict_history)


main_menu()
