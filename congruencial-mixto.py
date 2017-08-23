initial_seed = int(input("Semilla: "))
a = int(input("Constante multiplicativa (a): "))
c = int(input("Constante aditiva (c): "))
m = int(input("Módulo m: "))
next_seed = None
seed = initial_seed
random_numbers = []
while next_seed != initial_seed:
    next_seed = (a * seed + c) % m
    seed = next_seed
    random_numbers.append(seed/m)
print(random_numbers)
