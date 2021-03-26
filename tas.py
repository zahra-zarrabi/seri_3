import random
char=input("Roll the dice?(y/n)")
if char=="y":
    Tas = random.randint(1, 6)
    print('Dice number:',Tas)
    while True:
        if Tas==6:
            Tas = random.randint(1, 6)
            print('Prize number 6: ',Tas)
        else:
            break
else:
    exit

