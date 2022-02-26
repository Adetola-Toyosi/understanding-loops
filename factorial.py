for i in range(5):
    num = int(input("Number:\n"))
    factorial = 1

    if num < 0:
        print("must be positive")
    elif num == 0:
        print("Factorial of 0 is 1")
    else:
        for j in range(1, num + 1):
            factorial = factorial * j
    print(factorial)