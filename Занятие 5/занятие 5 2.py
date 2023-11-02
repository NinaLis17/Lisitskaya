def small(n):
    delitel = 2
    while n % delitel != 0:
        delitel += 1
    return delitel

n = int(input("Введите целое число (не меньше 2): "))
delit = small(n)
print('Наименьший натуральный делитель числа', n, 'отличный от 1, это', delit)