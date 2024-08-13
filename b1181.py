line = int(input(''))
operation = input('')
values = []

for i in range(12):
    for j in range(12):
        n = input()
        if i == line:
            values.append(float(n))

total = sum(values)
average = sum(values)/len(values)
if operation == 'S':
    print(f"{total:.1f}")
else:
    print(f"{average:.1f}")