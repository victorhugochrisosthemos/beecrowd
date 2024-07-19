first = int(input(''))
second = int(input(''))

if first > second:
    auxiliar = second
    second = first
    first = auxiliar

sum = 0
for i in range(first, second+1):
    if i % 13 != 0:
        sum += i

print(sum)