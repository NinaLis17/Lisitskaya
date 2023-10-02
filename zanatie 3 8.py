#8
n = int(input('размер дольки:'))
m = int(input('размер дольки:'))
k = int(input('долька:'))
def chocolate(a,b,c):
    if (a*b-c)%n == 0 or (a*b-c)%m == 0:
        print('Да')
    else:
        print('Нет')
chocolate(n,m,k)