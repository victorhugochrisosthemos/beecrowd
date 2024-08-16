matrix_order = int(input(''))
text = ''
for i in range(matrix_order):
    text += input('')

cels = matrix_order * matrix_order
index = 0
right = True

winner = 0
points = 0

line = 0

for i in range(1, cels + 1):
    
    if text[index] == 'o':
        points += 1
    elif text[index] == 'A':
        if points > winner:
            winner = points
        points = 0
        
    if i % matrix_order == 0:
        line += 1
        if line % 2 != 0:
            right = False
        else:
            right = True
    else:
        if right:
            index += 1
        else:
            index -= 1
    
    if i % matrix_order == 0 and not right:
        index += matrix_order
    elif i % matrix_order == 0 and right:
        index += matrix_order

if points > winner:
    winner = points

print(winner)
