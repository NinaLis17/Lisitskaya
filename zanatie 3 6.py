#6
x = int(input('введите число:'))
def year (a):
    if  a%4 == 0 and  a%100 != 0:
        print('Да')
    elif a%400 == 0:
        print('Да')
    else:
        print('Нет')
year(x)

