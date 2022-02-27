numbers = [23, 54, 67, 89, 15, 99]
fruits = ['Apple', "Orange", "Banana"]

numbers_2 = [num for num in numbers]
print(numbers_2)

numbers_3 = [num**2 for num in numbers]
print(numbers_3)

items = [item for item in fruits]
items_1 = [item[0] for item in fruits]
items_2 = [item[1] for item in fruits]
print(items)
print(items_1)
print(items_2)

products = [
    ("Cup", 5),
    ("Hat", 19),
    ("Watch", 20),
    ("Mug", 10),
]

items_3 = [item[1] for item in products if item[1] >= 10]
print(sorted(items_3))

modified_numbers = [num if num >= 50 else round(num / 2) for num in numbers]

print(sorted(modified_numbers))
