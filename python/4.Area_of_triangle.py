a = b = c = 25
# use Heron's Formula
# Find 's' ==> semi perimeter
s = (a + b + c)/2
area = ((s * (s-a) * (s-b) * (s-c)) ** 0.5)
print('The area of Traingle is %0.2f' %area)

