# Guess the random number
from random import randint, random

if __name__ == '__main__':
    while True:
        a = int(input("Enter first number here:\n"))
        b = int(input("Enter second number here:\n"))
        print(f"Our program have generated a random number between {a},{b} and you have to guess that.\nPlease Enter both player's name to continue:")
        P1name = input("Player1: ")
        P2name = input("Player2: ")

        p1tries = 0
        p2tries = 0
        random_number = randint(a, b)

        first = input("Who's coming first? ")
        second = [P2name if first == P1name else P1name]
        if first == P1name:
            p1guess = 0
            while p1guess != random_number:       
                p1tries += 1
                p1guess = int(input(f"Enter your guess {P1name}:\n"))
                if p1guess > random_number:
                    print("Hint: Your guess is higher than the random number.")
                elif p1guess < random_number:
                    print("Hint: You guess is lower than the random number.")
            print(f"Congrats! You guessed the number correctly in {p1tries} tries.")
            print(f"Now {P2name}'s turn.")
            p2guess = 0
            while p2guess != random_number:
                p2tries += 1
                p2guess = int(input(f"Enter your guess {P2name}:\n"))
                if p2guess > random_number:
                    print("Hint: Your guess is higher than the random number.")
                elif p2guess < random_number:
                    print("Hint: You guess is lower than the random number.")
            print(f"Congrats! You guessed the number correctly in {p2tries} tries.")
        
        
        elif first == P2name:
            
            p2guess = 0
            while p2guess != random_number:
                p2tries += 1
                p2guess = int(input(f"Enter your guess {P2name}:\n"))
                if p2guess > random_number:
                    print("Hint: Your guess is higher than the random number.")
                elif p2guess < random_number:
                    print("Hint: You guess is lower than the random number.")
            print(f"Congrats! You guessed the number correctly in {p2tries} tries.")
            print(f"Now {P1name}'s turn.")
            p1guess = 0
            while p1guess != random_number:       
                p1tries += 1
                p1guess = int(input(f"Enter your guess {P1name}:\n"))
                if p1guess > random_number:
                    print("Hint: Your guess is higher than the random number.")
                elif p1guess < random_number:
                    print("Hint: You guess is lower than the random number.")
            print(f"Congrats! You guessed the number correctly in {p1tries} tries.")
        

        else:
            print("Please enter one of the name you submitte before.")

        if p1tries > p2tries:
            print(f"{P2name} is the winner. \nHe took {p2tries} to guess the number and {P1name} took {p1tries}. ")
            
        elif p2tries > p1tries:
            print(f"{P1name} is the winner. \nHe took {p1tries} to guess the number and {P2name} took {p2tries}. ")
        
        else: 
            print(f"Match tied.\nYou both took {p1tries} to guess the number.")
        
        ask = input("Do you want to play again or want to quit?\n'c' to continue, 'q' to quit")
        if ask == 'c':
            continue
        if ask == 'q':
            break
        else:
            print("Please enter a valid input")






