from audioop import reverse
import random



def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j],end="")
        print('')
def ChoiceValue():
    arr=[2,4,8]
    value1 = random.randint(0, 2)
    return arr[value1]
def randomValueput(board):
    colIndex=[1,3,5,7]
    rowIndex=[1,3,5,7]
    colRandom=random.randint(0,3)
    rowRandom = random.randint(0, 3)
    if(board[rowIndex[rowRandom]][colIndex[colRandom]] == ' '):
        board[rowIndex[rowRandom]][colIndex[colRandom]] = ChoiceValue()
        return False
    return True
def gameOverCondition(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j]==' '):
                return False
    printBoard(board)            
    print('Game Over')
    return True
def mergeRight(board,score):
    for i in range(1,8,2):
        temp=[]
        for j in range(7,-1,-2):
            if(board[i][j]!=' '):
               if(len(temp)==0):
                temp.append(board[i][j])
                board[i][j] = ' '
               else:
                if(temp[-1]==board[i][j]):
                    lastValue=temp[-1]
                    temp.pop()
                    score += (lastValue+board[i][j])
                    temp.append(lastValue+board[i][j])
                    board[i][j] = ' '
                else:
                    temp.append(board[i][j])
                    board[i][j] = ' '
        temp.reverse()                
        for j in range(7,-1,-2):
            if(len(temp)!=0):
                board[i][j]=temp[-1]
                temp.pop()


def mergeLeft(board,score):
    for i in range(1, 8, 2):
        temp = []
        for j in range(1, 8, 2):
            if(board[i][j] != ' '):
               if(len(temp) == 0):
                temp.append(board[i][j])
                board[i][j] = ' '
               else:
                if(temp[-1] == board[i][j]):
                    lastValue = temp[-1]
                    temp.pop()
                    score += (lastValue+board[i][j])
                    temp.append(lastValue+board[i][j])
                    board[i][j] = ' '
                else:
                    temp.append(board[i][j])
                    board[i][j] = ' '
        temp.reverse()
        for j in range(1, 8, 2):
            if(len(temp) != 0):
                board[i][j] = temp[-1]
                temp.pop()


def mergeUp(board,score):
    for i in range(1, 8, 2):
        temp = []
        for j in range(1, 8, 2):
            if(board[j][i] != ' '):
               if(len(temp) == 0):
                temp.append(board[j][i])
                board[j][i] = ' '
               else:
                if(temp[-1] == board[j][i]):
                    lastValue = temp[-1]
                    temp.pop()
                    score += (lastValue+board[j][i])
                    temp.append(lastValue+board[j][i])
                    board[j][i] = ' '
                else:
                    temp.append(board[j][i])
                    board[j][i] = ' '


        temp.reverse()
        for j in range(1, 8, 2):
            if(len(temp) != 0):
                board[j][i] = temp[-1]
                temp.pop()


def mergeDown(board,score):
    for i in range(1, 8, 2):
        temp = []
        for j in range(7, -1, -2):
            if(board[j][i] != ' '):
               if(len(temp) == 0):
                temp.append(board[j][i])
                board[j][i] = ' '
               else:
                if(temp[-1] == board[j][i]):
                    lastValue = temp[-1]
                    temp.pop()
                    score += (lastValue+board[j][i])
                    temp.append(lastValue+board[j][i])
                    board[j][i] = ' '
                else:
                    temp.append(board[j][i])
                    board[j][i] = ' '

        temp.reverse()
        for j in range(7, -1, -2):
            if(len(temp) != 0):
                board[j][i] = temp[-1]
                temp.pop()

board = [['-', '-', '-', '-', '-', '-', '-','-','-'],
         ['|', ' ', '|', ' ', '|', ' ', '|',' ','|'],
         ['-', '-', '-', '-', '-', '-', '-','-','-'],
         ['|', ' ', '|', ' ', '|', ' ', '|',' ','|'],
         ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
         ['|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
         ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
         ['|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
         ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ]
while(True):
    MaxScore = 0
    score=0
    randomValueput(board)
    randomValueput(board)
    while(True):
        printBoard(board=board)
        inputValue = int(input("Enter The Value"))
        if(inputValue == 2):
            mergeDown(board,score)
            if(gameOverCondition(board=board)):
                break
            while(randomValueput(board)):
                pass

        elif(inputValue == 4):
            mergeLeft(board, score)
            if(gameOverCondition(board=board)):
                break
            while(randomValueput(board)):
                pass

        elif(inputValue == 6):
            mergeRight(board, score)
            if(gameOverCondition(board=board)):
                break
            while(randomValueput(board)):
                pass

        elif(inputValue == 8):
            mergeUp(board, score)
            if(gameOverCondition(board=board)):
                break
            while(randomValueput(board)):
                pass
        else:
            break


    print("Score is ", end="")
    print(score)
    MaxScore=max(MaxScore,score)
    exitgame=input("Press 0 for continue the game")
    if(exitgame!=0):
        break
print("Best Score - ",end='')
print(MaxScore)
