# Check the number is ARMSTRONG OR NOT
value = int(input('Enter the value to check it is Armstrong'))
count = 0
store = value
added = 0
while store > 0:
    store = store // 10 # 153 ==>3
    count +=1
    continue
for i in range(1, count+1):
    game = value % 10
    item = game ** count
    added = added + item
    value //= 10
print(added)

