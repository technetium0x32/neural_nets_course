n = int(input())
def template(word, num1, num2):
    print("The ", word, " number for the number ", num1, " is ", num2, ".", sep  = "")

template("next", n, n +1)
template("previous", n, n - 1)
