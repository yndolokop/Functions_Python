'''
Программа позволяет пополнять многократно счет и вычитает цену товара из баланса на счету.
При повторном пополнении баланса после совершения покупок - суммирует остаток с новым пополнением.
Выводит историю покупок.
Не смог написать без введения глобальных переменных.
'''
history_item = []  # хранит список товаров
history_price = []  # хранит список цен
balance_sum = []  # хранит суммы пополнений
result = 0


def main_menu():
    global result
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            balance = int(input('Пополните счет. Введите сумму пополнения: '))
            balance_sum.clear()  # очищаем список от ранее добавленных значений
            balance_sum.append(result)  # и вносим result, то что осталось после совершения покупок
            result = bal(balance)  # присвоим переменной result значение которая вернула функция
            print('Ваш баланс: ', result)
        elif choice == '2':
            price = int(input('Введите сумму покупки: '))
            if price > result:
                print('Недостаточно денег. Пополните счет')
            elif price <= result:
                item_name = input('Введите название товара: ')
                result = result - price
                print('Остаток на счету: ', result)
                history_item.append(item_name)
                history_price.append(price)
                print('Список покупок: ', history_item)
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
        new_balance += i  # суммировать в переменную new_balance
    return new_balance


def shopping_history():  # функция печатает историю покупок из двух списков: названий товара и цен
    dict_history = dict(zip(history_item, history_price))
    print('История покупок: ', dict_history)


main_menu()
