def print_alternate_numbers():
    numbers = []
    number = int(input("Введите число: "))
    while number != 0:
        numbers.append(number)
        number = int(input("Введите число: "))

    for i in range(0, len(numbers), 2):
        print(numbers[i])


print_alternate_numbers()