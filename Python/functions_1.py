from itertools import product
from shutil import _ntuple_diskusage


letters = ["a", "b", "d", "e", "i", "j", "o"]


def filter_vowels(letter):
    vowels = ["a", "e", "i", "o", "u"]

    if letter in vowels:
        return True
    else:
        return False


filtered_vowels = filter(filter_vowels, letters)

for vowel in filtered_vowels:
    print(vowel)

print(type(letters))

products = [
    ("Product-1", 32),
    ("Product-2", 45),
    ("Product-3", 10),
    ("Product-4", 23),
]
products.sort(key=lambda products: products[1])
# print(products)


my_list_1 = [1, 2, 10, 11, 5, 3, 34]

new_list_1 = filter(lambda x: (x % 2 == 0), my_list_1)
# for num in new_list_1:
# print(num)

list_num = list(new_list_1)
print(list_num)

# result = zip(ceva1, ceva2)
# print(set(result_set))
