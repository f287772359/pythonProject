import math
for num in range(1,10000):
    sum = 0
    for numd in range(1,num):
        if num % numd == 0:
            sum = sum + numd
    if sum == num:
        print(num,end = '')