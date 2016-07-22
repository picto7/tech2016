'''
проверка числа на простоту

'''
print()
n = int(input())
for i in range (2,n):
    if n % i == 0:
        print('составное число')
        break
else:
    print('простое число')