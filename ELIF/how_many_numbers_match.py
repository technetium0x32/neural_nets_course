a, b, c = [int(input()) for i in range(3)]

if a == b:
    if b == c:
        print(3)
    else:
        print(2)
else:
    if b == c:
        print(2)
    elif a == c:
        print(1)
    else:
        print(0)
