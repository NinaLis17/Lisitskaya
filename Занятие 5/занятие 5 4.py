def days(x,y):
    day=1
    distance=x
    while distance<y:
            distance*=1.1
            day+=1
    return day
x = float(input("Введите пробег в первый день (в км): "))
y = float(input("Введите целевой пробег (в км): "))
day = days(x, y)
print('Пробег спортсмена составит не менее', y,'км на', day, 'день')