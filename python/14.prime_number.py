value = int(input('Enter number to check prime or not\n'))
if value > 2:
    for i in range(2, int(value/2)+1):
        if value % i == 0:
            print('It is Not prime number')
            break
    else:
        print('It is prime number')
else:
    print('It is prime number')


