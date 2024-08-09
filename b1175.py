vector = []

for i in range(20):
    vector.append(int(input('')))
'''

for i in range(1, 20+ 1):
    vector.append(i)
'''
text = ''
iterations = 20
for i in range(20):
    iterations -= 1
    text += 'N[' + str(i) + '] = ' + str(vector[iterations])
    if iterations != 0:
        text += '\n'

print(text)