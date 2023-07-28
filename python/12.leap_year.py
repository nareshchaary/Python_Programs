value = int(input('Enter value to check leap year ==> '))
if (value % 400 ==0) and (value % 100 ==0):
    print(f'{value} is leap year')
elif (value % 4 ==0) and (value % 100 !=0):
    print(f'{value} is leap year')
else:
    print(f'{value} is not leap year')