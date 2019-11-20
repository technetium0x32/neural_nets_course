a, n = [int(input()) for i in range(2)]

def power(a, n):
    res = 1
    if n >= 0:
        for i in range(n):
            res *= a
    else:
        for i in range(-n):
            res /= a
        
    return res

print(power(a, n))
