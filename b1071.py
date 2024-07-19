n1 = int(input(' '))
n2 = int(input(' '))

if(n2 < 0):
    n2 = n2

acumulator = 0
for i in range(n2 + 1,n1):
    if(i % 2 != 0):
        acumulator = acumulator + i

print(acumulator)