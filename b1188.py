operation = input()
counter = 0
values = []

start = 5
end = 7

for i in range(12):
    for j in range(12):
        variable = float(input())
        if i >= 7 and j >= start and j < end:
            values.append(variable)
            counter += 1
    if i >= 7:
        start -= 1
        end += 1

answer = sum(values)
if operation == 'M':
    answer /= counter

print(f"{answer:.1f}")

