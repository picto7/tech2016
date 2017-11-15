N = int (input())
Ms = []
for i in range (N):
    Ms.append(int(input()))
m1 = 10005
for i in range (N):
    if Ms[i]%3 !=0 and Ms[i] <= m1:
        m2 = m1
        m1 = Ms[i]
R = int(input())
s = m1+m2
print ('вычисленное контрольное значение = ',s)
if R == s:
    print ('контроль пройден')
else:
    print ('контроль не пройден')
