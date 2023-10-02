#3
a = 64
b = 9
A = []
if a > b:
    for i in range(a,b+1,-1):
        if i%2 != 0:
            A.append(i)
print(A)