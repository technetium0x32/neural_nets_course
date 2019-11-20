from math import sqrt

x1, y1, x2, y2 = [float(input()) for i in range(4)]

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

res = distance(x1, y1, x2, y2)
print("%.5f" % res)
