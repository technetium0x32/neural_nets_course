desks = [int(input()) for i in range(3)]
S = 0
for i in desks:
    S+= i //2 + i % 2
print(S)
