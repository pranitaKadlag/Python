from random import choice

players = ['pranita','smita','pratik','saurabh','akshay','maumita']
print(players)

#print(choice(players))

teamA = []
teamB = []

while len(players) >0:
    playerA = choice(players)
    teamA.append(playerA)
    players.remove(playerA)
    # print(playerA)
    # print('players left :', players)

    playerB= choice(players)
    teamB.append(playerB)
    players.remove(playerB)
    #print(playerB)
    #print('players left :', players)

print('teamA :' , teamA)
print('teamB :' , teamB)






