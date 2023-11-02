def kolvo():
    c = 0
    while True:
        b = int(input("Введите число: "))
        if b == 0:
            break
        c += 1
    return c

c = kolvo()
print('Количество членов последовательности:',c)