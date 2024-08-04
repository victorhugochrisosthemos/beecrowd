iterations = int(input(''))
x = []
y = []

for i in range(iterations):
    aux_x, aux_y = input('').split(' ')
    aux_x = int(aux_x)
    aux_y = int(aux_y)
    x.append(aux_x)
    y.append(aux_y)

for i in range(iterations):
    sum = 0
    while y[i] != 0:
        if x[i] % 2 != 0:
            sum += x[i]
            y[i] -= 1
        x[i] += 1
    print(sum)
