import math
x =3.74*10**-2
y = -0.825
z = 0.16*10**2
s = (1 + (math.sin(x + y))**2)/ (math.fabs(x - 2*y/(1+ (x**2) * (y**2) ))) * (x**math.fabs(y)) + math.cos((math.atan(1/z)))**2
print(s)