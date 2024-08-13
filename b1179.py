even = []
odd = []

iteration = 15

for i in range(iteration):
    value = int(input(''))
    if value % 2 == 0:
        even.append(value)
        if len(even) == 5 or (i+1) == iteration:
            for j in range(len(even)):
                print('par[' + str(j) + '] = ' + str(even[j]))
            even = []
    else:
        odd.append(value)
        if len(odd) == 5 or (i+1) == iteration:
            for j in range(len(odd)):
                print('impar[' + str(j) + '] = ' + str(odd[j]))
            odd = []

if len(even) != 0:
    for j in range(len(even)):
        print('par[' + str(j) + '] = ' + str(even[j]))

if len(odd) != 0:
    for j in range(len(odd)):
        print('impar[' + str(j) + '] = ' + str(odd[j]))