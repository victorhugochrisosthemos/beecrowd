
line = ""
while line != "0 0":
    line = input("")
    d, n = line.split(" ")
    d = int(d)
    n = int(n)
    if d >= 1 and d <= 9 and n >= 1 and n <= 10**100:
        value = ""
        string_n = str(n)
        
        for i in range(len(str(n))):
            if str(d) != string_n[i]:
                value += string_n[i]
                
        if value != "":
            value = int(value)
            value = str(value)
        elif value != "0 0":
            value = "0"
        print(value)
