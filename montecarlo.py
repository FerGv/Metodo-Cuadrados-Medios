def montecarlo(frequencies, numbers):
    """
        Arguments:
        -> frequencies -- type: list => [(value_1, frequency_1), ..., (value_n, frequency_n)]
        -> numbers -- type: list => [number_1, ..., number_n]

        Return a list.
    """

    acumulated_frequency = 0
    acumulated_frequencies = []
    random_numbers = []
    for value,frequency in frequencies:
        acumulated_frequency += frequency
        if acumulated_frequency > 1: raise Exception('No es una función de probabilidad')
        acumulated_frequencies.append((value, acumulated_frequency))

    for number in numbers:
        for value,frequency in acumulated_frequencies:
            if number < frequency:
                random_numbers.append(value)
                break

    return random_numbers


def main():
    """ Example """
    
    frequencies = [(1,0.1), (2,0.5), (3,0.4)]
    numbers = [0.7, 0.3, 0.01, 0.9]
    print(montecarlo(frequencies, numbers))


if __name__ == '__main__':
    main()