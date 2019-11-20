def main():
    a = int(input())
    if a == 0:
        print(0)
    else:
        main()
        print(a)

main()
