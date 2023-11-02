a = [3, 13, 44, 14, 18, 35, 32, 12]
def zamena(a):
    n = len(a)
    for i in range(n):
        if a[i]<15:
            a[i]*= 2
    return a
print("массив:", a)
izm_a = zamena(a)
print("измененный массив:", izm_a)