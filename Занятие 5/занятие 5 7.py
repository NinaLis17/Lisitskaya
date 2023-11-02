def c_el():
    co = -1
    nu = 0
    while True:
        n = int(input("Введите число : "))
        if n == 0:
            break
        if n > nu:
            co += 1
        n = nu
    return co

co = c_el()
print('Количество элементов последовательности, больших предыдущего элемента:', co)