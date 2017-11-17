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
    mean = float(input("-> Media: "))
    desviation = float(input("-> Desviación estándar: "))
    numbers = int(input("-> Números aleatorios a generar: "))
    reference_number = int(input("\n\t -> Número de referencia: "))
    option = input(""" 
            ¿Qué valores desea conocer con respecto al número de referencia?
            a) Mayores
            b) Menores

            Opción: """)
    normalized_random_numbers = normal_distribution(mean, desviation, numbers)
    result = list(filter(lambda x: x > reference_number, normalized_random_numbers)) if option.lower() == 'a' else list(filter(lambda x: x < reference_number, normalized_random_numbers))

    print("\n\n -> Valores obtenidos: {result_len} \n\n{result}".format(result_len=len(result), result=result))


if __name__ == '__main__':
    main()
