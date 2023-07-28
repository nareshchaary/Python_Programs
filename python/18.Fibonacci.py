value = int(input('Enter number of terms'))
n1, n2 = 0, 1
count = 0
if value <=0:
    print('Enter positive value')
elif value ==1:
    print(f'The fibonacci series for upto {value} is ')
    print(n1)
else:
    while count <= value:
        print('n1')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count+=1