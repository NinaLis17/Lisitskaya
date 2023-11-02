t1 = (5, 10)
t2 = (6, 8)
def katet(c1, c2):
    gip=(c1**2 + c2**2)**0.5
    return gip

def gipoten(t1, t2):
    gip1=katet(t1[0],t1[1])
    gip2=katet(t2[0],t2[1])
    if gip1>gip2:
        return "У первого треугольника гипотенуза больше."
    elif gip1<gip2:
        return "У второго треугольника гипотенуза больше."
    else:
        return "Гипотенузы треугольников равны."

print("Катеты первого:", t1)
print("Катеты второго:", t2)

result=gipoten(t1, t2)
print(result)