#7
a = int(input('ввведите число:'))
b = int(input('ввведите число:'))
c = int(input('ввведите число:'))
def sovpadenie (x,y,z):
    if x == y == z:
        print(3)
    elif x == y or y == z or z == x:
        print(2)
    else:
        print(0)
sovpadenie(a,b,c)
