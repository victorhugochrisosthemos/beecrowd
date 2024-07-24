dias = int(input())
ano = int(dias // 365)
mes = int((dias - ano * 365) // 30)
dia = dias - ano * 365 - mes * 30

print("{} ano(s)".format(ano))
print("{} mes(es)".format(mes))
print("{} dia(s)".format(dia))