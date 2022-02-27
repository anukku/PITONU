# non keywords arguments

def subtract(*nums):
        number = 100
        for x in nums:
            number = number - x
        return number 

print(subtract(2, 3, 5, 25, -45, 111))

def employee(**info):
    print(info)
    
employee(name="Ciobanu", last_name="Matei", age=19)
    
# global - global variables can be used in functions