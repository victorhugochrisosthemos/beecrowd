value = int(input(''))

text = ''

for j in range(value*4):
    if ((j+1) % 4) != 0:
        text += str(j+1) + ' '
    else:
        text += 'PUM'
        if ((value*4) != j+1):
            text += '\n'
        
print(text)