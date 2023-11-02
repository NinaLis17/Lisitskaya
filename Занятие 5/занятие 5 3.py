N = int(input("Введите число N: "))
def bolsh(N):
    suma = 0
    res = 1
    while res <= N:
        suma += 1
        res *= 2
    return suma - 1, res // 2

N = int(input("Введите число N: "))
suma, res = bolsh(N)
print('Наибольшая целая степень двойки, не превосходящая N, это 2^',suma, ' = ', res)
