first_line = int(input(''))
text = input('')
'''
# Testes
first_line = 5
text = "-1 1 -1 -1 1"
'''
line = text.split(" ")

matrix = [line]

for _ in range(first_line - 1):
    new_line = []
    for i in range(len(line) - 1):  
        if (line[i] == '-1' and line[i + 1] == '1') or (line[i] == '1' and line[i + 1] == '-1'):
            new_line.append('-1')
        elif (line[i] == '-1' and line[i + 1] == '-1') or (line[i] == '1' and line[i + 1] == '1'):
            new_line.append('1')
        else:
            new_line.append('0')
    matrix.append(new_line)
    line = new_line  

'''
# Testes
for i in range(first_line):
    print(matrix[i])
'''

if matrix[first_line-1][0] == '-1':
    print('branca')
else:
    print('preta')