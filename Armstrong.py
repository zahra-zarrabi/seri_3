a=input('Enter the number:')
y=0
p = len(a)
for m in range(p):
    x=int(a[m])**p
    y+=x
if y==int(a):
    print(a,'is Armstrong')
else:
    print(a,'Not Armstrong')