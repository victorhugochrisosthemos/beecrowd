value = int(input(''))
for i in range(value):
    if value % (i + 1) == 0:
        print(i + 1)