'''
Дан набор из N целых положительных чисел. Необходимо выбрать из набора
произвольное количество чисел так, чтобы их сумма была как можно больше
и при этом не делилась на 6. В ответе нужно указать количество выбранных
чисел и их сумму, сами числа выводить не надо
'''
N = 3
mn = 10001
summ1 = 0
for i in range (3):
    x = int(input())
    summ1 += x
    if x%6 != 0 and x < mn:
        mn = x
if summ1%6 != 0:
    k = N
else:
    if mn < 10008:
        k = N-1
        summ1 = summ1-mn
    else:
        summ1 = 0
        k = 0
print (summ1,k)





