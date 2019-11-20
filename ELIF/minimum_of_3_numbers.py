a, b, c = [int(input()) for i in range(3)]

if a >= b:
    if b >= c:
        print(c)
    else:
        print(b)
else:
    if a >= c:
        print(c)
    else:
        print(a)
