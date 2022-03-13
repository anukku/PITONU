from sys import getsizeof
from array import array

numbers = array("i", [1, 2, 3])
numbers.append(4)
print(numbers)


number = (x * 2 for x in range(10))

print("Generator Object: ", getsizeof(number))

# * -> for unpacking
