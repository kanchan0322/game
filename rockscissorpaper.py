from random import randint

#List of games

game=['rock','paper','scissors']

#Assigining a random option to computer
computer=game[randint(0,2)]

#Keep count for points
playersPoint=0
computerPoint=0
goOn=True

#Loop goOn until goOn is False
while(goOn):
    #    Ask for User Input
    player=input("Rock,Paper or Scissors ? or Enter Finish to end! ")
    # Check for Scenarios
    if player=='Finish' or player=='finish':
        goOn=False
    elif player==computer :
        print("Tie!")
    elif player=="Rock" or player=="rock":
        if computer=="Paper":
            print("You Loose.. ",computer ,"covers",player)
            computerPoint=computerPoint +1
        else:
            print("You Win!! ",player,"smashes",computer)
            playersPoint=playersPoint+1
    elif player=='Paper' or player=='paper':
        if computer=='Scissors':
            print("You Loose.. ",computer,"cut",player)
            computerPoint=computerPoint+1
        else:
            print("You Win!! ",player,"covers",computer)
            playersPoint=playersPoint+1
    elif player=='Scissors' or player=='scissors':
        if computer=='Rock':
            print("You Loose.. ",computer,"smashes",player)
            computerPoint=computerPoint+1
        else:
            print("You Win!1 ",player,"cut",computer)
            playersPoint=playersPoint+1
    else:
        print("This Not a Valid play,check you spelling..")

    computer=game[randint(0,2)]

#printing final points
print("**** Final Points *****")
print("Player : ",playersPoint)
print("Computer : ",computerPoint)



