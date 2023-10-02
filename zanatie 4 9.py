n = int(input())
f1 = 1
f2 = 1
f = 0
c = 0
A = [1,1]
while c < n-2:
    f = f1 + f2
    A.append(f)
    f1 = f2
    f2 = f
    c += 1
print(sum(A))