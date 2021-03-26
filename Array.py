import numpy.random as random
number=int(input('Please enter the length of the array:'))
while True:
    a = random.randint(1, 50, size=number)
    b=set(a)
    if len(b)==number:
        break
print('Array with random and non-duplicate numbers:',b)
