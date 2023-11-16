def zamena_strok(matr, i, j):
    matr[i], matr[j] = matr[j], matr[i]

def zamena_stolbcov(matr, i, j):
    for row in matr:
        row[i], row[j] = row[j], row[i]

def max_znah(matr):
    max_value = matr[0][0]
    max_row = 0
    max_col = 0

    for i in range(len(matr)):
        for j in range(len(matr[0])):
            if matr[i][j] > max_value:
                max_value = matr[i][j]
                max_row = i
                max_col = j

    return max_row, max_col

def rearrange_matrix(matr):
    max_row, max_col = max_znah(matr)
    zamena_strok(matr, 0, max_row)
    zamena_stolbcov(matr, 0, max_col)

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

matr = []

for i in range(n):
    row = []
    print(f"Введите элементы {i+1}-й строки через пробел:")
    elements = input().split()
    for element in elements:
        row.append(float(element))
    matr.append(row)

rearrange_matrix(matr)

print("Матрица после перестановки:")
for row in matr:
    for element in row:
        print(element, end=" ")
    print()