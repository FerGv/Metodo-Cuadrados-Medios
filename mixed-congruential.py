def mixed_congruential(seed, multiplicative_constant, additive_constant, module):
    next_seed = None
    seed = initial_seed
    random_numbers = []

    while next_seed != initial_seed:
        next_seed = (multiplicative_constant * seed + additive_constant) % module
        seed = next_seed
        random_numbers.append(seed/module)

    return random_numbers


def main():
    """ Example """
    initial_seed = int(input("Semilla: "))
    a = int(input("Constante multiplicativa (a): "))
    c = int(input("Constante aditiva (c): "))
    m = int(input("Módulo m: "))
    print(mixed_congruential(seed, a, c, m))
    

if __name__ == '__main__':
    main()