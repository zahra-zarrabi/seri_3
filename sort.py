x=[]
a=int(input('Please specify the length of the array:'))
for m in range(a+1):
    b=int(input('number'+str(m)+' '))
    x.append(b)
if x==sorted(x):
    print('The array is arranged')
else:
    print('The array is not tidy')