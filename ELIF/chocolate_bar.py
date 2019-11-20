n, m, k = [int(input()) for i in range(3)]

if k % n == 0 and k // n <= m:
    print("YES")
elif k % m == 0 and k // m <= n:
    print("YES")
else:
    print("NO")
