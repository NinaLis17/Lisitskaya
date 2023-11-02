D=[2,10,45,15,6,7,9]
def summa(a):
    n=len(a)
    sum=0
    for i in range(n):
        if i%2!=0:
            sum+=a[i]
    return sum

print("массив:",D)
sum_nechet=summa(D)
print("сумма нечетных элементов:",sum_nechet)