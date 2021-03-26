import math
a=int(input('Enter the number:'))
while a>1:
    for m in range(2,a+1):
        if a%m==0:
            a=a/m
        else:
            break
    if a==1:
        print('yes')
    else:
        print('no')
        break