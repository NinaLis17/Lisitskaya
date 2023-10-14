#4
a = int(input('расстояние между рядами:'))
b = int(input('расстояние между дырочками:'))
l = int(input('длина свободного конца шнурка:'))
N = int(input('количество дырочек:'))

def shnurok (x,y,z,c):
    return (((c/2)-1)*x*2) + (((c/2)-1)* y * 2) + y + (2 * z)

def minn (x,y,z):
    return min(x,y,z)

print(minn(a,b,l))