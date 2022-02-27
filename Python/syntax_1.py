# BOOLEAN
value_1 = True
value_2 = False

# Variable Type
x = 10
y = 10.00
print(x, y)
print(type(x), type(y))
print(type(value_1))
print(type(value_2))

# List
list = [1, 2, 3, True, False, [1.00, 2.00, 3.00]]

# Dictionary
user_info = {"user_name": "awesome50", "user_id": 50}
print(user_info)
print(type(user_info))

# Tuple
tuple = (1, 2, 3, True, False, [1.00, 2.00, 3.00])
print(tuple)
print(type(tuple))

# Set
set = {1, 2, 3, "Python", 101}
print(set)
print(type(set))

# String Methods
nume = "Ciobanu"
print(len(nume))
print(nume[0])
print(nume[0:6])
prenume = "matei"
#nume_complet = nume + " " + prenume
nume_complet = f"{nume}, {prenume}"
print(nume_complet)

# Lower, Upper, Title\

print(nume.lower())
print(prenume.upper())
print(nume_complet.title())

# Strip, Lstrip, Rstrip

job = "   Programmer   "
print(job.strip())
print(job.lstrip())
print(job.rstrip())

# Find

print(job.find("m"))
print(job.replace("P", "p"))

# In , Not

print("mm" in job)
print("mm" not in job)

# " in a string -> \" \' , new line -> \n

# putere -> 2 ** 5

# rotunjire -> round()

# abs()

#math.sin() / math.cos() / math.ceil()

# ord() -> numeric representation

# if - or - and
