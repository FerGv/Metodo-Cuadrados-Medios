def mixed_congruential(initial_seed, multiplicative_constant, additive_constant, module):
    """
        Arguments:
        -> initial_seed -- type: float => Initial seed to generate random numbers
        -> multiplicative_constant -- type: float => Number to multiply by the seed
        -> additive_constant -- type: float => Number to add to the seed
        -> module -- type: float

        Return a list.
    """

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

    initial_seed = float(input("Semilla: "))
    a = float(input("Constante multiplicativa (a): "))
    c = float(input("Constante aditiva (c): "))
    m = float(input("Módulo (m): "))

    print(mixed_congruential(initial_seed, a, c, m))
    

if __name__ == '__main__':
    main()