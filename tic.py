import random

def printb(board):
    for i in board:
        print(i)
        
board = [["-"]*3 for i in range(3)]

player = 'x'
computer = 'o'
printb(board)

def playerinput(board):
        try:
            inp_row= int(input("insert row number "))
            inp_col= int(input("insert col number "))
            if inp_row >=1 and inp_row <=3  and inp_col>=1 and inp_col<=3 and board[inp_row-1][inp_col-1]=='-':
                board[inp_row-1][inp_col-1]=player
        except: 
            print ("aaaaa")
        return board
def wincheck(board):
     for i in range(3):
          if board[i][0]==board[i][1]==board[i][2] and board[i][0]!='-':
               print(board[i][0]+ "wins")
               return True
          if board[0][i]==board[1][i]==board[2][i] and board[0][i]!='-':
               print(board[0][i]+ "wins")
               return True
     if board[0][0]==board[1][1]==board[2][2] and board[0][0]!='-':
          print (board[0][0]+ "wins")
          return True
     if board[0][2]==board[1][1]==board[2][0] and board[0][2]!='-':
          print (board[0][2]+ "wins")
          return True
     if '-' not in board[0] and '-' not in board[1]and'-' not in board[2]:
          print("tie")
          return True
     return False
def ai(board):
     while True:
          random.seed
          ai_row= random.randrange(0,3)
          ai_col= random.randrange(0,3)
          if board[ai_row][ai_col]=='-' and board[ai_row][ai_col]!='x':
               board[ai_row][ai_col]=computer
               return True
          else: continue
     #return False
while True:                 
    playerinput(board)
    printb(board)
    ai(board)
    print ("\n")
    printb(board)
    wincheck(board)
    if wincheck(board) == True:
         printb(board)
         break
    #break
     