# 1
def double_precision():
    s = 0
    print(s)

    exp = 10000000111
    c, i = 0, 0
    while (exp != 0):
        e = exp % 10
        c = c + e * pow(2, i)
        exp = exp // 10
        i = i + 1
    print(c)

    fraction = str(111010111001000000000000000000000000000000)
    f = 0
    i = 1
    for item in fraction:
        f = f + int(item) * (0.5**i)
        i = i + 1
    print(f)

    n = ((-1)**s)*(2**(c - 1023))*((1 + f))
    print(n)

    return
double_precision()