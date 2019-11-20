x1, y1, x2, y2 = [int(input()) for i in range(4)]

if (x1 % 2 + y1 % 2) % 2==(x2 % 2+ y2 % 2) % 2:
    print("YES")
else:
    print("NO")
