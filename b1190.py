option = input()
selection = []

start = 11
counter = 0

for i in range(12):
    for j in range(12):
        value = float(input())
        if (i < 6 and j > 11 - i) or (i >= 6 and j > i):
            selection.append(value)
            counter += 1

answer = sum(selection)
if option.upper() == 'M':
    answer /= counter

print(f"{answer:.1f}")



