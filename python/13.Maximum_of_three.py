a = float(input('Enter \'a\' value ==> '))
b = float(input('Enter \'a\' value ==> '))
c = float(input('Enter \'a\' value ==> '))

if (a>b) and (a>c):
    print(f'{a} is Maximum of {b} and {c}')
elif (a<b) and (b>c):
    print(f'{b} is Maximum of {a} and {c}')
else:
    print(f'{c} is Maximum of {a} and {b}')