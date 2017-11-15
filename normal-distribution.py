from functools import reduce
from random import random

def normal_distribution(mean, desviation, numbers):
    normalized_random_numbers = []

    for number in range(numbers):
        ranorum = reduce(lambda x, y: x + y, [random() for i in range(12)]) - 6
        random_number = mean + desviation*ranorum
        normalized_random_numbers.append(random_number)

    return normalized_random_numbers

def main():
    """ Example """
    mean = float(input("Media: "))
    desviation = float(input("Desviación estándar: "))
    numbers = int(input("Números aleatorios a generar: "))
    print(normal_distribution(mean, desviation, numbers))


if __name__ == '__main__':
    main()
