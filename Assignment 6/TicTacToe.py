import pyfiglet
import random
from colorama import Fore
import datetime

def show():
    for row in Game_Board:
        for cell in row:
            if cell == "X":
                print(Fore.RED + "X", end = " ")
            elif cell == "O":
                print(Fore.BLUE + "O", end = " ")
            else:
                print(Fore.RESET + cell, end = " ")
        print(Fore.RESET)
        
def check_game():
    if Game_Board[0][0] == "X" and Game_Board[0][1] == "X" and Game_Board[0][2] == "X":
        print("Player 1 Wins!")
    elif Game_Board[1][0] == "X" and Game_Board[1][1] == "X" and Game_Board[1][2] == "X":
        print("Player 1 Wins!")
    elif Game_Board[2][0] == "X" and Game_Board[2][1] == "X" and Game_Board[2][2] == "X":
        print("Player 1 Wins!")
        
    elif Game_Board[0][0] == "O" and Game_Board[0][1] == "O" and Game_Board[0][2] == "O":
        print("Player 2 Wins!")
    elif Game_Board[1][0] == "O" and Game_Board[1][1] == "O" and Game_Board[1][2] == "O":
        print("Player 2 Wins!")
    elif Game_Board[2][0] == "O" and Game_Board[2][1] == "O" and Game_Board[2][2] == "O":
        print("Player 2 Wins!")
        
    elif Game_Board[0][0] == "X" and Game_Board[1][0] == "X" and Game_Board[2][0] == "X":
        print("Player 1 Wins!")
    elif Game_Board[0][1] == "X" and Game_Board[1][1] == "X" and Game_Board[2][1] == "X":
        print("Player 1 Wins!")
    elif Game_Board[0][2] == "X" and Game_Board[1][2] == "X" and Game_Board[2][2] == "X":
        print("Player 1 Wins!")
        
    elif Game_Board[0][0] == "O" and Game_Board[1][0] == "O" and Game_Board[2][0] == "O":
        print("Player 2 Wins!")
    elif Game_Board[0][1] == "O" and Game_Board[1][1] == "O" and Game_Board[2][1] == "O":
        print("Player 2 Wins!")
    elif Game_Board[0][2] == "O" and Game_Board[1][2] == "O" and Game_Board[2][2] == "O":
        print("Player 2 Wins!")
        
    elif Game_Board[0][0] == "X" and Game_Board[1][1] == "X" and Game_Board[2][2] == "X":
        print("Player 1 Wins!")
    elif Game_Board[0][2] == "X" and Game_Board[1][1] == "X" and Game_Board[2][0] == "X":
        print("Player 1 Wins!")
    
    elif Game_Board[0][0] == "O" and Game_Board[1][1] == "O" and Game_Board[2][2] == "O":
        print("Player 2 Wins!")
    elif Game_Board[0][2] == "O" and Game_Board[1][1] == "O" and Game_Board[2][0] == "O":
        print("Player 2 Wins!")
    else:
        return 0
    return 1
    
    

title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(title)

while True:
    Start = datetime.datetime.now().replace(microsecond = 0)
    print("Choice Number OF Player")
    print("For 'Player vs Player' Enter 1 : ")
    print("For 'Player vs CPU' Enter 2 : ")
    Number_Player = int(input())
    if Number_Player == 1 or Number_Player == 2:
        break
    else:
        print("mese adam vared kon :|")
    
        

Game_Board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]

for row in Game_Board:
    for cell in row:
        print(cell, end=" ")
    print()
    


Counter = 0
while True:
    print("Player 1")
    
    while True:
        row = int(input("Row: "))
        col = int(input("Col: "))
        
        if 0 <= row <= 2 and 0 <= col <=2:
            if Game_Board[row][col] == "-":
                Game_Board[row][col] = "X"
                break
            else:
                print("jer nazan :/")
        else:
            print("mese adam vared kon :|")
    Counter += 1  
    show()
    Check = check_game()
    if Check == 1:
        End = datetime.datetime.now().replace(microsecond = 0)
        print("Game Time:", End - Start)
        break
    
    if Counter == 9:
        print("DRAW!")
        End = datetime.datetime.now().replace(microsecond = 0)
        print("Game Time:", End - Start)
        break
    
    if Number_Player == 1:
        print("Player 2")
        while True:
            row = int(input("Row: "))
            col = int(input("Col: "))
            
            if 0 <= row <= 2 and 0 <= col <=2:
                if Game_Board[row][col] == "-":
                    Game_Board[row][col] = "O"
                    break
                else:
                    print("jer nazan :/")
            else:
                print("mese adam vared kon :|")
    elif Number_Player == 2:
        print("CPU")
        while True:
            Row_Random = random.randint(0, 2)
            Col_Random = random.randint(0, 2)
            if Game_Board[Row_Random][Col_Random] == "-":
                Game_Board[Row_Random][Col_Random] = "O"
                break
    Counter += 1    
    show()
    Check = check_game()
    if Check == 1:
        End = datetime.datetime.now().replace(microsecond = 0)
        print("Game Time:", End - Start)
        break
    
    
    