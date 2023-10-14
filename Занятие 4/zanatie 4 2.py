#2
a = 9
b = 50
A = []
if a < b:
    for i in range(a,b+1):
        A.append(i)
else:
    for j in range(b,a+1):
        A.append(j)
    A.reverse()
print(A)