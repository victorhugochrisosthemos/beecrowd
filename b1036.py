bhas=input().split()

A=float(bhas[0])
B=float(bhas[1])
C=float(bhas[2])

delta= (B**2) - (4*A*C)

if (delta<0 or A<=0):
     print("Impossivel calcular")
else:
     rd=delta**0.5
     R1= (-B +rd)/(2*A)
     R2= (-B - rd)/(2*A)
     print("R1 = %.5f" %R1)
     print("R2 = %.5f" %R2)