hi, hf = list(map(int,input().split()))
if hf == hi:
    print("O JOGO DUROU 24 HORA(S)")
elif hf < hi:
    print("O JOGO DUROU {} HORA(S)".format(24 - hi + hf))
else:
    print("O JOGO DUROU {} HORA(S)".format(hf - hi))