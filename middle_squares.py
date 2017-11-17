def middle_squares(seed, numbers):
    random_numbers = []
    
    for number in range(numbers):
        length_seed = len(seed)
        seed_squared = int(seed) ** 2
        seed_squared_string = str(seed_squared)
        length_seed_squared = len(seed_squared_string)
        seed = ""
        initial_position = length_seed_squared % length_seed

        if initial_position == 0:
            initial_position = length_seed_squared // length_seed
        elif length_seed_squared % 2 == 0:
            initial_position -= 1
        else:
            initial_position -= 2

        for i in range(length_seed):
            seed += seed_squared_string[initial_position]
            initial_position += 1

        random_numbers.append(seed)

    return random_numbers
    

def main():
    """ Example """
    seed = input("Semilla: ")
    numbers = int(input("Cuántos números desea obtener?: "))
    print(middle_squares(seed, numbers))

if __name__ == '__main__':
    main()
