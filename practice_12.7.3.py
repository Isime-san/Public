per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
m = int(input ("Введите сумму для взноса:"))

a = per_cent ['ТКБ']
b = per_cent ['СКБ']
c = per_cent ['ВТБ']
d = per_cent ['СБЕР']

a1 = round (m/100*a)
b1 = round (m/100*b)
c1 = round (m/100*c)
d1 = round (m/100*d)
deposit = [a1, b1, c1, d1]
print (deposit)

print ('Максимальная сумма, которую вы можете заработать —', max (deposit))