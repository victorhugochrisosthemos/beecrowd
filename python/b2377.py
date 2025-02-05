first_line = input("")
second_line = input("")

l, d = first_line.split(' ')
k, p = second_line.split(' ')

l = int(l)
d = int(d)
k = int(k)
p = int(p)

if l >= 1 and d <= 10**4 and k >= 1 and p <= 10**4:
    price = ((l // d) * p) + (l * k)
    
print(price)
