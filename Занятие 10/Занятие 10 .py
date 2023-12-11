matr = []
with open('Лисицкая_У233_vvod.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.split()))
        matr.append(row)
def is_symmetri(matr):
    n = len(matr)

    # Проверяем каждый элемент матрицы
    for i in range(n):
        for j in range(n):
            # Если элементы не симметричны относительно главной диагонали,
            # то матрица не является симметричной
            if matr[i][j] != matr[j][i]:
                return False

    # Если все элементы симметричны, то матрица является симметричной
    return True

if is_symmetri(matr):
    s = print("Матрица симметрична")
else:
   s = print("Матрица не симметрична")
with open('Лисицкая_У233_vivod.txt', 'w') as file:
    file.write(s)