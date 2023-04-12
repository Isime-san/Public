ticket_num = int(input("Сколько вам нужно билетов?: "))
no_cash = 0
cash = 0
payment = 0
for i in range(ticket_num):
    age = int(input('Введите возраст посетителя:'))
    if age<18:
        cash += 0
        no_cash += 1
        print ('Для вас проход бесплатный!')
    elif 18 <= age <25:
        cash += 990
        payment += 1
        print ('Цена билета: 990 руб.')
    else:
        cash += 1390
        payment += 1
        print('Цена билета: 1390 руб.')
if ticket_num > 3 and cash > 3960:
    print('Цена билетов: ', сash, 'руб.')
    print(f'Скидка 10% за ', {payment}, 'посетителей')

    cash = cash - ((cash/100)*10)

print (f'Всего: ', {cash}, 'руб.')
print (f'Бесплатно -', {no_cash}, 'посетителей')