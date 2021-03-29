import random
import turtle
import time

turtle.forward(60)
turtle.backward(40)
turtle.left(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(100)


def dar(i, x, y):
    turtle.speed(1)
    if i=='head':
        turtle.up()
        [x, y] = turtle.position()
        turtle.setpos(x - r, y - r)
        turtle.down()
        turtle.circle(r)
    elif i=='Body':
        turtle.up()
        [x, y] = turtle.position()
        turtle.setpos(x + r, y - r)
        turtle.down()
        turtle.forward(20)
    elif i=='hand left':
        [x, y] = turtle.position()

        turtle.right(60)
        turtle.forward(50)

    elif i=='hand right':
        turtle.setpos(x, y)
        turtle.left(120)
        turtle.forward(50)
    elif i=='Body2':
        turtle.setpos(x, y)
        turtle.right(60)
        turtle.forward(50)
        [x, y] = turtle.position()

    elif i=='leg left':
        turtle.right(30)
        turtle.forward(60)
    elif i=='leg right':
        turtle.setpos(x, y)
        turtle.right(-60)
        turtle.forward(60)
    return x, y


true_chars=[]
words=['PHP','Python', 'Android', 'Matlab', 'Bootstrap', 'JavaScript']
word=random.choice(words)
score=7
print(word)
l=['head','Body','hand left','hand right','Body2','leg left','leg right']
i,r,x,y= 0, 30, 0, 0
while True:
    for m in range(len(word)):
      if word[m].lower() in true_chars:
          print(word[m], end='')
      else:
          print('-', end='')
    if len(true_chars) == len(set(word)):
        break
    char = input('\nplease character').lower()
    if char in word.lower():
        true_chars.append(char)
    else:
        turtle.color('red')
        [x,y]=dar(l[i], x, y)
        i += 1
        score -= 1

    print('Your score is:',score)
    if score==0:
        print('game over')
        break
time.sleep(8)