#rock paper sizzer game

from random import randint

player = input('rock(r), paper(p), sizzer(s)?')

print(player, 'vs' ,end=' ')

chosen =randint(1,3)
#print(chosen)

if chosen ==1:
    computer = 'r'

elif chosen ==2:
    computer = 'p'

else:
    computer = 's'

print(computer)

if player == computer:
    print('DRAW')
elif player == 'r' and computer == 's':
    print("player wins !!")
elif player == 'r' and computer == 'p':
    print("computer wins !!")
elif player == 'p' and computer == 'r':
    print("player wins !!")
elif player == 'p' and computer == 's':
    print("computer wins !!")
