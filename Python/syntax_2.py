# for loop

status = True
for x in range(10):
    print(f"The code has run for {x} times")
    if status:
        print("Succes")
        break
    
for y in range(0, 100, 10):
    print(f"Programul de executa de {y} ori")
    if status:
        print("Succes")
        break
for z in range(10, 20):
    print(f"Programul se executa de {z} ori")
    if status:
        print("Succes")
        break
    
# x, y loops

for x in range(3):
    for y in range (5):
        for z in range (2):
            print(f"({x},{y},{z})")
            
# for in char

for char in "Ciobanww","Matthew":
    print(char)
    
# while

nota = 10
while nota >= 5:
    print(f"Ai trecut cu nota {nota}")
    nota = nota - 1