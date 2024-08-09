vector = []

for i in range(100):
    vector.append(float(input('')))

for i in range(100):
    if vector[i] <= 10:
        print('A[' + str(i) + '] = ' + str(vector[i]))