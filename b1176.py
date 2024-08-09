iterations = int(input(''))

vector = []

for i in range(iterations):
    vector.append(int(input('')))

for i in range(iterations):
    if vector[i] == 0:
        answer = 0
    elif vector[i] == 1:
        answer = 1
    else:
        last = 1
        secondLast = 0
        for j in range(2, vector[i] + 1): 
            answer = last + secondLast
            secondLast = last
            last = answer
    print('Fib(' + str(vector[i]) + ') = ' + str(answer))