# lists

even_numb = [2, 4, 6, 8, 10]
odd_nums = [1, 3, 5, 7, 9]
cities = ["New York", "London"]
boolean = [True, False]
mixed_data = even_numb + odd_nums + cities + boolean
print(mixed_data)

numbers = list(range(10, 20, 3))
print(numbers)

name = list("Matei")
print(name)
print(len(name))

# list index

collection = ["Matei", "Parmi", "Ratiu", "Ruxy", "Cosmin"]
var = collection[0]
collection[0] = collection[1]
collection[1] = var
print(collection)

prieten1, eu, *prieteni = collection
print(prieteni)

# for in lists

mix = ["a", "b", "c"]

for index, x in enumerate(mix):
    print(index, x)

mix.append("d")
print(mix)
mix.insert(0, "0")
print(mix)
mix.pop(-1)
print(mix)
mix.remove("c")
print(mix)

del name[1:4]
print(name)

# modifying

fruits = ["Banana", "Orange", "Apple", "Banana", "Orange", "Apple"]
fruits.reverse()
print(" , ".join(fruits))

print(fruits.index("Orange"))
print(fruits.count("Banana"))
