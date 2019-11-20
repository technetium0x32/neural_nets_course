N, M, x, y = [int(input()) for i in range(4)]

if N < M:
    N, M = M, N
    
if M - x < x:
    x = M - x
if N - y < y:
    y = N- y
        
if x > y:
    print(y)
else:
    print(x)

    
