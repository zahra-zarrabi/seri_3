import random
computer_score, user_score = 0, 0
item=['rock','paper','scissor']
x=0
while x<5:
    computer_choice = random.choice(item)
    user_choice = item[int(input('Enter 0 for rock, 1 for paper and 2 for scissor'))]
    if (computer_choice=='rock' and user_choice=='scissor') or\
        (computer_choice=='paper' and user_choice=='rock')\
        or (computer_choice=='scissor' and user_choice=='paper'):

        computer_score +=1
    else:
        #user_choice=='scissor' and computer_choice=='paper' or user_choice=='rock' and computer_choice=='scissor' or user_choice=='paper' and computer_choice=='rock'

        user_score += 1
    x+=1
print('Computer Score: ',computer_score ,'   ','User Score: ', user_score)
if computer_score > user_score:
    print('Computer Wins')
else:
    print('User Wins')

