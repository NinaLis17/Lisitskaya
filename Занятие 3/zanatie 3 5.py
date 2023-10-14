#5
a = int(input())
b = int(input())
c = int(input())
d = int(input())
def kletka (x1,y1,x2,y2):
    a = ''
    b = ''
    if x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0:
        if x1 < 9 and y1 < 9 and x2 < 9 and y2 < 9:
            if x1 != x2 and y1 != y2:
                if y1%2 == 0 and x1%2 == 0:
                    a = 'Черный'
                elif y1%2 == 0 and x1%2 != 0:
                    a = "Белый"
                elif y1%2 != 0 and x1%2 == 0:
                    a = 'Белый'
                elif y1%2 != 0 and x1%2 != 0:
                    a = "Черный"
                if y2%2 == 0 and x2%2 == 0:
                    b = 'Черный'
                elif y2%2 == 0 and x2%2 != 0:
                    b = "Белый"
                elif y2%2 != 0 and x2%2 == 0:
                    b = 'Белый'
                elif y2%2 != 0 and x2%2 != 0:
                    b = "Черный"
                if a == b:
                    print('Да')
                else:
                    print("Нет")
kletka(a,b,c,d)
