vector = []
for i in range(10):
    value = int(input(''))
    if value <= 0:
        vector.append(1)
    else:
        vector.append(value)

for i in range(10):
    print('X[' + str(i) + '] = ' + str(vector[i]))