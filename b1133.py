x = int(input())
y = int(input())
if x > y:
    maior = x
    menor = y
else:
    maior = y
    menor = x
for i in range(menor + 1, maior):
    if i % 5 == 2 or i % 5 == 3:
        print(str(i))