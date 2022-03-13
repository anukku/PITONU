def factorial(x):
    if x == 1:
        return 1
    else:
        return (int(x * factorial(x - 1)))


#num = input()
#num = 3
num = input("Enter the value: ")
print("The factorial of", int(num), "is", factorial(int(num)))
