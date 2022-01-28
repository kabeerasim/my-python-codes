from random import randint
from random import random

board = {
    "7": " ", "8": " ", "9": " ",
    "4": " ", "5": " ", "6": " ",
    "1": " ", "2": " ", "3": " " }

sboard = {
    "7": " ", "8": " ", "9": " ",
    "4": " ", "5": " ", "6": " ",
    "1": " ", "2": " ", "3": " " }


bkeys = []

for key in board:
    bkeys.append(key)

def bprint(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')

def user(turn):
    if board['7'] == board['8'] == board['9'] == turn != ' ':
        bprint(board)
        print("\nGame Over.\n")
        print(f"***{turn} WON***")
        return 1
    if board['4'] == board['5'] == board['6'] == turn != ' ':
        bprint(board)
        print("\nGame Over.\n")
        print(f"***{turn} WON***")
        return 1
    if board['1'] == board['2'] == board['3'] == turn != ' ':
        bprint(board)
        print("\nGame Over.\n")
        print(f"***{turn} WON***")
        return 1

    if board['9'] == board['6'] == board['3'] == turn != ' ':
        bprint(board)
        print("\nGame Over.\n")
        print(f"***{turn} WON***")
        return 1

    if board['1'] == board['5'] == board['9'] == turn != ' ':
        bprint(board)
        print("\nGame Over.\n")
        print(f"***{turn} WON***")
        return 1

    if board['7'] == board['4'] == board['1'] == turn != ' ':
        bprint(board)
        print("\nGame Over.\n")
        print(f"***{turn} WON***")
        return 1

    if board['7'] == board['5'] == board['3'] == turn != ' ':
        bprint(board)
        print("\nGame Over.\n")
        print(f"***{turn} WON***")
        return 1

    if board['2'] == board['5'] == board['8'] == turn != ' ':
        bprint(board)
        print("\nGame Over.\n")
        print(f"***{turn} WON***")
        return 1


def compu(*args):
    if board['7'] == board['8'] == board['9'] == comp != ' ':
                bprint(board)
                print("\nGame Over.\n")
                print(f"***{comp} WON***")
                return 1

    if board['4'] == board['5'] == board['6'] == comp != ' ':
                bprint(board)
                print("\nGame Over.\n")
                print(f"***{comp} WON***")
                return 1

    if board['1'] == board['2'] == board['3'] == comp != ' ':
                bprint(board)
                print("\nGame Over.\n")
                print(f"***{comp} WON***")
                return 1

    if board['7'] == board['4'] == board['1'] == comp != ' ':
                bprint(board)
                print("\nGame Over.\n")
                print(f"***{comp} WON***")
                return 1
                
    if board['7'] == board['4'] == board['1'] == comp != ' ':
                bprint(board)
                print("\nGame Over.\n")
                print(f"***{comp} WON***")
                return 1

    if board['9'] == board['6'] == board['3'] == comp != ' ':
                bprint(board)
                print("\nGame Over.\n")
                print(f"***{comp} WON***")
                return 1

    if board['1'] == board['5'] == board['9'] == comp != ' ':
                bprint(board)
                print("\nGame Over.\n")
                print(f"***{comp} WON***")
                return 1

    if board['7'] == board['5'] == board['3'] == comp != ' ':
                bprint(board)
                print("\nGame Over.\n")
                print(f"***{comp} WON***")
                return 1

    if board['2'] == board['5'] == board['8'] == comp != ' ':
                bprint(board)
                print("\nGame Over.\n")
                print(f"***{comp} WON***")  
                return 1

if __name__ == '__main__':
    turn = 'X'
    comp = 'O'
    count = 0
    lst = ["7", "3", "5", "1", "2", "6", "9", "8", "4"]

    while True:
        bprint(board)
        print(f"It's your turn {turn}. Move to which place?")
        umoves = []
        cmoves = []

        uinput = input()
        if board[uinput] == ' ':
            umoves.append(uinput)
            board[uinput] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
        
        while True:
            for i in lst:
                if board[i] == ' ':
                    cmoves.append(i)
                    board[i] = comp
                    count += 1
                    break
            break
                
        #checking which player has won
        if count >= 5 and user(turn) != 1 or compu(comp) != 1:   
            user(turn)
            if user(turn) == 1:
                ask = input("Do you want to play again? Y or N\n").lower()
                if ask == 'y':
                    board = sboard
                    continue
                elif ask == 'n':
                    break
                else:
                    print("Please enter a valid input. Y / N ?")
                
            elif compu(comp):
                if compu(comp) == 1:
                    ask = input("Do you want to play again? Y or N").lower()     
                    if ask == 'y':
                        board = sboard
                        continue
                    elif ask == 'n':
                        break
                    else:
                        print("Please enter a valid input. Y / N ?")
       
