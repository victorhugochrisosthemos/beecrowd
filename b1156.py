import math

numerator = 1
denumerator = 1
s = 0

while numerator != 39:
    s += numerator/denumerator

    numerator += 2
    denumerator = denumerator * 2

s = math.ceil(s)
print(f"{s:.2f}")