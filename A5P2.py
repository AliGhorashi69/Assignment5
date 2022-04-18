from colorama import Fore, Style 

import time


while True:
    print()
    Game_type=int(input("Please select the type of game: write 1 for playring with computer or 2 for two players game: "))
    if Game_type==1:
        print(Fore.BLUE+" Your Welcome !!! You select a game with computer: "+Style.RESET_ALL)
        break
    elif Game_type==2:
        print(Fore.BLUE+" Your Welcome !!! You select a game with another player: "+Style.RESET_ALL)
        break
    else:
        print("Try again!!! invalid number of Game Type")




game =  [["  _  ","  _  ","  _  "],
         ["  _  ","  _  ","  _  "],
         ["  _  ","  _  ","  _  "]]

a=time.time()

def show_gameboard():
    for j in range(3):
        for i in range(3):
            print(game[j][i],end='')
        print()


show_gameboard()

n=0

def player1(n):
    print("Player 1 turn")
    print()
    
    while True:
        row=int(input("enter the row: "))
        col=int(input("enthe coloumn: "))
        if row<3 and col<3:
            if game [row][col] == "  _  ":
                game [row][col] = Fore.RED+"  O  "+Style.RESET_ALL
                show_gameboard()
                break
            elif game [row][col] != "  _  " and n<9:
                print("Unavailable move by player 1!!! try again")
        else:
            print("Not Valid numbers !!! row and coloumn should be less than 3")
      

def player2(n):
    print("Player 2 turn")
    print()
   
    while True:
         row=int(input("enter the row: "))
         col=int(input("enthe coloumn: "))
         if row<3 and col<3:
            if game [row][col] == "  _  ":
                game [row][col] = Fore.GREEN+"  X  "+Style.RESET_ALL
                show_gameboard()
                break
            elif game [row][col] != "  _  " and n<9:
                print("Unavailable move by player 2!!! try again")
         else:
             print("Not Valid numbers !!! row and coloumn should be less than 3")

import random


def com(n):
    print("Computer Turn")
    print()

    while True:
     row=random.randint(0,3)
     col=random.randint(0,3)
     if row<3 and col<3:
            if game [row][col] == "  _  ":
                game [row][col] = Fore.GREEN+"  X  "+Style.RESET_ALL
                show_gameboard()
                break




def victory_check():
 for j in range(3):
    if game [j][0] == game[j][1] ==  game[j][2]== Fore.RED+"  O  "+Style.RESET_ALL\
        or game [0][j] == game[1][j] == game[2][j]== Fore.RED+"  O  "+Style.RESET_ALL\
        or game[0][0] == game[1][1] == game [2][2] == Fore.RED+"  O  "+Style.RESET_ALL\
        or game[2][0] == game[1][1] == game [0][2] == Fore.RED+"  O  "+Style.RESET_ALL:
        print()
        print(Fore.YELLOW+">>>     Player1   Won  !!!   OOO  <<"+Style.RESET_ALL)
        b=time.time()
        print(Fore.YELLOW+"The game took: ", int(b-a), ' seconds to finish'+Style.RESET_ALL)
        print()
        exit()
    if game [j][0] ==  game[j][1] ==  game[j][2]== Fore.GREEN+"  X  "+Style.RESET_ALL\
        or game [0][j] ==  game[1][j] ==  game[2][j]== Fore.GREEN+"  X  "+Style.RESET_ALL\
        or game[0][0] == game[1][1] == game [2][2] == Fore.GREEN+"  X  "+Style.RESET_ALL\
        or game[2][0] == game[1][1] == game [0][2] == Fore.GREEN+"  X  "+Style.RESET_ALL:
        print()
        print(Fore.YELLOW+" >> Player2 (or computer)   Won    !!! << "+Style.RESET_ALL)
        b=time.time()
        print(Fore.YELLOW+" The game took: ", int(b-a), '  seconds to finish'+Style.RESET_ALL)
        print()
        exit()


if Game_type==2:
    while n<9:
        player1(n)
        n=n+1
        victory_check()
        player2(n)
        n=n+1
        victory_check()
        print(n)
elif Game_type==1:
    while n<9:
        player1(n)
        n=n+1
        victory_check()
        com(n)
        n=n+1
        victory_check()
        print(n)

b=time.time
print (">>>>>>>>>>>>>>>    Tie !!!   <<<<<<<<<<<<<")
print("The game took: ", int(b-a), '  seconds to finish')
print()
    

  
    


