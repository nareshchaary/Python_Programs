lower = int(input('Enter lower number'))
upper = int(input('Enter Upper number'))
for i in range(lower, upper+1):
    if i > 1:
        for j in range(2, i+1):
            if i % j ==0:
                break
        else:
            print(i)