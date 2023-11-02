def sred():
    c = 0
    k = 0
    while True:
        n = int(input("Введите число : "))
        if n == 0:
            break
        c += 1
        k += n
    if c == 0:
        return 0
    else:
        return k / c

otvet = sred()
print('Среднее значение всех элементов последовательности:', otvet)