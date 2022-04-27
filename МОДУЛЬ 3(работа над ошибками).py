history_item = []  # хранит список товаров
history_price = []  # хранит список цен
new_balance = 0


def shopping_history():  # функция печатает историю покупок из двух списков: названий товара и цен
    dict_history = dict(zip(history_item, history_price))
    print('История покупок: ', dict_history)


def buy(new_balance):
    price = int(input('Введите сумму покупки: '))
    if price > new_balance:
        print('Недостаточно денег. Пополните счет')
    elif price <= new_balance:
        item_name = input('Введите название товара: ')
        new_balance -= price
        print('Остаток на счету: ', new_balance)
        history_item.append(item_name)
        history_price.append(price)
        print('Список покупок: ', history_item)
    else:
        print('Обратитесь в техподдержку')
    return new_balance

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(f'Ваш счет: {new_balance}')
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        balance = int(input('Пополните счет. Введите сумму пополнения: '))
        new_balance += balance
    elif choice == '2':
        new_balance = buy(new_balance)
    elif choice == '3':
        shopping_history()
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')





