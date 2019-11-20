S = input().split()

def toLowerCase(s):
    cc = ord(s[0])
    s = chr(cc - 32) + s[1:]
    print(s, end = " ")

for i in S:
    toLowerCase(i)
