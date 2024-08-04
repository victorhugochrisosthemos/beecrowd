exit = 0

while exit == 0:
    value = int(input(''))
    if value == 0:
        break
    else:
        if value % 2 != 0:
            value += 1
        sum = 0
        for i in range(5):
            sum += value
            value += 2
        print(sum)