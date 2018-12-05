theBoard = {'top-l':' ', 'top-m':' ','top-r':' ',
            'mid-l':' ','mid-m':' ','mid-r':' ',
            'low-l':' ','low-m':' ','low-r':' '}

def printBoard(board):
    print(board['top-l'] + '|' +  board['top-m']  + '|' +  board['top-r'])
    print("________")
    print(board['mid-l'] + '|' + board['mid-m']  + '|'  +  board['mid-r'])
    print("________")
    print(board['low-l'] + '|' + board['low-m']  + '|'  +  board['low-r'])
    checkForBingo(board)



def enterUserValues():
    for i in range(9):
        turn  = input("enter X or O?: ")
        print("Turn of: ",turn)
        move = input("Enter you move on space: ")
        theBoard[move] = turn
        printBoard(theBoard)
        if(turn=='X'):
            turn = 'O'
        else:
            turn = 'X'
    

def checkForBingo(board):
    if(board['top-l'] and board['top-m'] and board['top-r']):
        print("Bingo!!!!!!!!"+str(board['top-l'])+"Won")
    elif(board['mid-l'] == board['mid-m'] == board['mid-r']):
        print("Bingo!!!!!!!!"+str(board['mid-l'])+"Won")
    elif(board['low-l'] == board['low-m'] == board['low-r']):
        print("Bingo!!!!!!!!"+str(board['low-l'])+"Won")
    elif(board['top-l'] == board['mid-m'] == board['low-r']):
        print("Bingo!!!!!!!!"+str(board['top-l'])+"Won")
    elif(board['top-r'] == board['mid-m'] == board['low-l']):
        print("Bingo!!!!!!!!"+str(board['top-l'])+"Won")

def main():
    enterUserValues()
    printBoard(theBoard)

main()    
            


        



