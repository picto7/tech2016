'''
среднее арифметическое от N до 100
'''
x = int( input('введите число целое = '))
summa = srednee = n = 0
summ_kvad = 0.00
for i in range (x,101):
    n +=1
    summa += i
    srednee = summa/n
    summ_kvad += i**2
print ('сумма = ', summa, 'количество чисел = ', n, 'среднее = ', srednee )
print ('сумма квадратов чисел от n до 100 =',summ_kvad)


