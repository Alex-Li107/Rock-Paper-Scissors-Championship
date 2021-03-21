import random

#Plays rock paper scissor between two players, where:
#0 = rock
#1 = paper
#2 = sissor
#Returns whether player1 wins the match or loses
def rockPaperScissors():
    #while no winner is found keep playing
    while(True):
        #generates a random number from 0 to 2 for each player to act as rock, paper, or scissors
        player1 =  random.randint(0, 2)  
        player2 =  random.randint(0, 2)  
        #if the numbers are equal re-roll them
        if player1 == player2: continue
        #compares whether player1 lost or won
        elif player1 == 0 and player2 == 2: return True
        elif player1 == 1 and player2 == 0: return True
        elif player1 == 2 and player2 == 1: return True
        else: return False

#Plays rock paper scissor between two players, where:
#0 = rock
#1 = paper
#2 = sissor
#param p1     is a string that will hold the first player's name
#param p2     is a string that will hold the second player's name
#Returns whether player1 wins the match or loses. Also prints out the details of the round of who beat who with what and who the champion is
def rockPaperScissorsFinals(p1, p2):
    #while no winner is found keep playing
    while(True):
        #generates a random number from 0 to 2 for each player to act as rock, paper, or scissors
        player1 =  random.randint(0, 2)  
        player2 =  random.randint(0, 2)  
        #if the numbers are equal re-roll them
        if player1 == player2: continue
        #compares whether player1 lost or won and prints how each player beat the other
        elif player1 == 0 and player2 == 2:
           print(p1, "beats", p2, "with rock over scissors!\n"+ p1, "is the tournament CHAMPION!")
           return True
        elif player1 == 1 and player2 == 0: 
            print(p1, "beats", p2, "with paper over rock!\n"+ p1, "is the tournament CHAMPION!")
            return True
        elif player1 == 2 and player2 == 1: 
            print(p1, "beats", p2, "with scissors over paper!\n"+ p1, "is the tournament CHAMPION!")
            return True
        elif player2 == 0:
            print(p2, "beats", p1, "with rock over scissors!\n"+ p2, "is the tournament CHAMPION!")
            return False
        elif player2 == 1:
            print(p2, "beats", p1, "with paper over rock!\n"+ p2, "is the tournament CHAMPION!")
            return False
        else: 
            print(p2, "beats", p1, "with scissors over paper!\n" + p2, "is the tournament CHAMPION!")
            return False

#main
#int to hold the amount of players
playerCount = int(input("Welecome to the Rock Paper Scissors Championship\nHow many contestants are there? "))
#list of potential first names
firstNames = ["Aaren", "Jessica", "James", "Richard", "Jeremy", "Emily", "John", "Scott", "Zachary", "Haley"]
#list of potential last names
lastNames = ["Smith", "Sun", "May", "Hammond", "Clarkson", "Wright", "Wick", "Wang", "Lau", "Li"]
#array to hold the contestants' full name
Names = []
#dictionary to hold the lists of who beat who
winnersList = {}
#int to track the round number
roundCount = 1
#asks if the user is ready to start. It will keep on prompting the user until they enter either a lowercase or uppercase 'y'
rdy = input("Ready to start? ")
while rdy != 'y' and rdy != 'Y':
    rdy = input("Ready to start? ")
#name generation
#while there are still players that neeed names, keep on looping
for i in range (0,playerCount):
    #temp is an int that will point to the index of the current player's first name in the firstNames array
    temp = random.randint(0,playerCount-1)
    #temp2 is an int that will point to the index of the current player's last name in the lastNames array
    temp2 = random.randint(0,playerCount-1)
    #adds the full name to the Names array 
    Names.append(firstNames[temp] + " " +lastNames[temp2])
    #removes the string at index temp in the firstNames array to prevent it from being chosen again
    firstNames.pop(temp)
    #removes the string at index temp2 in the lastNames array to prevent it from being chosen again
    lastNames.pop(temp2)
    playerCount-=1
    #addes the players full name into the dictionary with an empty array that will hold who they beat in the tournament 
    winnersList[Names[i]] = []
#match making; continue looping until 2 or less players are still able to play
while (len(Names) > 2):
    print("Round", roundCount, "results")
    #while there is people that need to be matched, keep on looping until there is only one person left
    for i in range (len(Names), 1, -2):
        #temp points to a random index in the Names array, this will be the player1 in the current match
        temp = random.randint(0, i-1)
        #get the string at Names[temp]
        player1 = Names[temp]
        #removed the name so that it will not be matched again
        Names.pop(temp)
        #temp2 points to a random index in the Names array, this will be the player2 in the current match
        temp2 = random.randint(0, i-2)
        #if player1 wins the match
        if rockPaperScissors(): 
            print(player1, "beats", Names[temp2])
            #add the name of player2 (the loser) to the list of who player1 beat
            winnersList[player1].append(Names[temp2])
        #if player1 loses the match
        else: 
            print(Names[temp2], "beats", player1)
            #add the name of player1 (the loser) to the list of who player2 beat
            winnersList[Names[temp2]].append(player1)
        #removed the name of player2 so that they will will not be matched again
        Names.pop(temp2)
    #if there is still one player...
    if len(Names) == 1:
        print(Names[0], "had a bye")
        #add a blank to their list of who they beat. 
        winnersList[Names[0]].append("")
        #remove the name from the array of avaible players
        Names.pop(0)
    #loops through the map
    for key, values in winnersList.items():
        #if the length of the list under each player's name is equal to the round number, add them back into the names list to play the next round
        if len(values) == roundCount: Names.append(key)
    #increment the round count
    roundCount+= 1
#final round
print("Round", roundCount, "results")
#checks if the match started with only one player 
if len(Names) == 1: print(Names[0], "was the only player, they win by default\nThey did not beat anyone")
#if the first player in the Names array beat the second player (based on their indexs)
elif(rockPaperScissorsFinals(Names[0], Names[1])):
    #prints the detailed results of the match
    print(Names[0], "beat [" + Names[1], end = '')
    #loops theit list of who they beat and prints out every name that is not a blank 
    for i in winnersList[Names[0]]:
        if i != '': print(",", i, end = '')
    print("]")
#if the first player in the Names array lost to the second player (based on their indexs)
else: 
    #prints the detailed results of the match
    print(Names[1], "beat [" + Names[0], end = '')
    #loops theit list of who they beat and prints out every name that is not a blank 
    for i in winnersList[Names[1]]:
        if i != '': print(",", i, end = '')
    print("]")