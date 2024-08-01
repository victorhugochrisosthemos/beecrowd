n = float(input())
acumulado = 0
if 0 <= n <= 2000:
    print("Isento")
else:
    n -= 2000
    if n - 1000 > 0:
        acumulado += 1000 * 0.08
        n -= 1000
        if n - 1500 > 0:
            acumulado += 1500 * 0.18
            n -= 1500
            if n > 0:
                acumulado += n * 0.28
        else:
            acumulado += n * 0.18
    else:
        acumulado += n * 0.08
    print("R$ {:.2f}".format(acumulado))