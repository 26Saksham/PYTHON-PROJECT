import random
#print The Board
def printBoard(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end="")
        print('')
#update the board any Valid Input Enter
def updateBoard(mat,turn,value):
    xo=''
    if(turn ==1):
        xo='x'
    else:
        xo='o'
    if(value == 1):
        mat[1][1] = xo
    elif(value == 2):
        mat[1][3] = xo
    elif(value == 3):
        mat[1][5] = xo
    elif(value == 4):
        mat[3][1] = xo
    elif(value == 5):
        mat[3][3] = xo
    elif(value == 6):
        mat[3][5] = xo
    elif(value == 7):
        mat[5][1] = xo
    elif(value == 8):
        mat[5][3] = xo
    elif(value == 9):
        mat[5][5] = xo
    printBoard(mat)
#check the value,it Enter by own aur not
def checkOwn(player,inputValue):
    for i in player:
        if(inputValue==i):
            return False
    return True
#check the value,it Enter by Other aur not

def checkOther(otherPlayer,inputValue):
    for i in otherPlayer:
        if(inputValue==i):
            return False
    return True
def drawCondition(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if(mat[i][j]>='1' and mat[i][j]<='9'):
                return False
    return True

 
def winGame(player):
    win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [
        1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    copyPlayer = player.copy()
    if(len(copyPlayer)<3):
        return False
    for wincon in win:
        subArr=0
        for num in wincon:
            if(copyPlayer.count(num)!=0):
                subArr+=1
        if(subArr==3):
            return True
   
    return False

print("Welcome to Tic Tac Toe Game")
playByRobert=int(input("Press 1 for play with other Player\nPress 2 for play with Computer"))
name1=''
name2=''
if(playByRobert==1):
    name1=input("Enter the Player 1 Name")
    name2=input("Enter the Player 2 Name")
else:
    name1 = input("Enter the Player 1 Name")
    name2="Computer"
StopPlay = True
ScorePlayer1 = 0
ScorePlayer2 = 0
drawmatch = 0
while(StopPlay):
    mat = [['-', '-', '-', '-', '-', '-', '-'],
           ['|', '1', '|', '2', '|', '3', '|'],
           ['-', '-', '-', '-', '-', '-', '-'],
           ['|', '4', '|', '5', '|', '6', '|'],
           ['-', '-', '-', '-', '-', '-', '-'],
           ['|', '7', '|', '8', '|', '9', '|'],
           ]
    printBoard(mat)
    p1=[]
    p2=[]
    turn=1
    while(True):
        if(turn==1 or turn==2):
            value = int(input("Enter the Number"))
        elif(turn==3):
            value=random.randint(1,9)
        if(value >= 1 and value <= 9):
            if(turn == 1):
                if(checkOwn(p1, value)):
                    if(checkOther(p2, value)):
                        updateBoard(mat, turn, value)
                        p1.append(value)
                        if(playByRobert==2):
                            turn=3
                        else:
                            turn = 2
                        if(winGame(p1)):
                            print(name1+" win the Game")
                            ScorePlayer1+=1
                            break
                        if(drawCondition(mat)):
                            print("Match Draw")
                            drawmatch+=1
                            break
                    else:
                        print("This Value Enter by "+name2)
                else:
                    print("you Already Enter the Same Number,Please Enter the Other Number")
            elif(turn == 2 or turn==3):
                if(checkOwn(p2, value)):
                    if(checkOther(p1, value)):
                        updateBoard(mat, turn, value)
                        p2.append(value)
                        turn = 1
                        if(winGame(p2)):
                            print(name2+" win the game")
                            ScorePlayer2+=1
                            break
                        if(drawCondition(mat)):
                            print("Match Draw")
                            drawmatch+=1
                            break
                    else:
                        print("This Value Enter by "+name1)
                else:
                    print("you Already Enter the Same Number,Please Enter the Other Number")
    
        else:
            print("Enter Number Only 1-9")
    continueGame=int(input("0 for Exit the Game \nPress any key for Continue the game"))
    if(continueGame==0):
        StopPlay=False

if(ScorePlayer1>ScorePlayer2):
    print("Congrats for "+ name1 +" your Score is ",end='')
    print(ScorePlayer1)
    print((ScorePlayer1/(ScorePlayer1+ScorePlayer2+drawmatch))*100,end='')
    print("% Score in the total")
if(ScorePlayer1 < ScorePlayer2):
    print("Congrats for"+name2+"your Score is ", end='')
    print(ScorePlayer2)
    print((ScorePlayer2/(ScorePlayer1+ScorePlayer2+drawmatch))*100,end='')
    print("% Score in the total")
if(ScorePlayer1==ScorePlayer2):
    print("Congrats for "+name1+ "and"+ name2 +" Score is ", end='')
    print(ScorePlayer1)
print("Total Draw matches is ",end='')
print(drawmatch)
print("Thank-you!")

