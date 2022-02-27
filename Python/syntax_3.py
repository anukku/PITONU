# functions

def nume():
        print("Ciobanu")

nume()

succes = True

def operation():
    if succes:
        print("Yay!!!")

operation()

def sum():
    for number in range(4, 10, 2):
        print(number)

sum()

def arithmetic_operations(x, y):
    print(f"{x} + {y} = {x + y}")
    print(f"{x} * {y} = {x * y}")
    print(f"{x} / {y} = {x / y}")
    print(f"{x} - {y} = {x - y}")
    
arithmetic_operations(8,4)

def legal_age(Name, Age):
    if Age >= 18:
        print(f"{Name} is old enough")
    else:
        print(f"{Name} is not old enough")

legal_age("Ciobanu", 20)
legal_age("Ruxy", 14)

# return in functions

def ceva(x, y):
    if x == y:
        return("Succes")
altceva = ceva(5,5)
print(f"{altceva}")

def multiply(number, by):
    return number * by

result = multiply(number=10, by=5)
print(result)



