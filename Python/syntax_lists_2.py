# sorting lists

numbers = [654, 54, 34, 1, 666, 111, 5]
print(sorted(numbers, reverse=True))
print(sorted(numbers, reverse=False))

# sorting list with tupils

products = [
    ("Cup", 5),
    ("Hat", 19),
    ("Watch", 20),
    ("Mug", 10),
]


def sort_products(product):
    return product[1]


products.sort(key=sort_products)


def sort_products_1(product_1):
    return product_1[0]


products.sort(key=sort_products_1)
print(products)
