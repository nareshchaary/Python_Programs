import cmath
a = b = c = 5
d = (b**2) - (4 * a * c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print(f'Quadratic equation are {sol1} and {sol2}')