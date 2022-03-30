def EvenorOdd(x):
    if x%2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    x = int(input("enter the value of x: "))

    evenorodd = EvenorOdd(x)
    print(evenorodd)

