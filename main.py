def Euclidean_GCD(a, b):
    if b == 0:
        return a
    else:
        x = a % b
        return Euclidean_GCD(b, x)


if __name__ == "__main__":
    a = int(input(" Enter first number : "))
    b = int(input("Enter second number : "))
    print(Euclidean_GCD(a, b))
