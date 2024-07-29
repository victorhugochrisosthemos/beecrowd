a,b,c=list(map(float,input().split()))
if(a < b):
    temp = a
    a = b
    b = temp
if(b < c):
    temp = b
    b = c
    c = temp
if(a < b):
    temp = a
    a = b
    b = temp
if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    elif a**2 > (b**2 + c**2):
        print("TRIANGULO OBTUSANGULO")
    elif a**2 < (b**2 + c**2):
        print("TRIANGULO ACUTANGULO")
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c:
        print("TRIANGULO ISOSCELES")