iterations = int(input(''))

fibonacci = 0
last = 0
secondLast = 0
text = ''

for i in range(1, iterations + 1):
    if i == 2:
        fibonacci = 1
    else:
        fibonacci = last + secondLast
    secondLast = last
    last = fibonacci
    text += str(fibonacci)

    if i != iterations:
        text += ' '

print(text)