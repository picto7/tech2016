'''
проверка числа на простоту

'''
print('введите число')
n = int(input())
for i in range (2,n):
    if n % i == 0:
        print('составное число, делители',i)
else:
    print ('простое число')
