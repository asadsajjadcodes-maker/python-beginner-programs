import random

print("Welcome to the rock , paper, scissors game.")
name = input("\nEnter your name: ")

def ch (a) :
    if a == 1 :
        return "rock"
    elif a == 2 :
        return "paper"
    elif a == 3 :
        return "scissors"
    


print("Choose an option by entering the number from 1 to 4.")

while True :
    print("\n1: rock \n2: paper \n3: scissors \n4: quit")
    try :
        a = int(input("Enter your choice: "))
    except ValueError :
        print("Invalid choice, only choose between numbers from 1 to 4.")
        continue

    if a == 4 :
        print(f"\n{name}, Thank you for playing.")
        break
    elif a < 1 or a > 4 :
        print("\nInvalid entry , only choose from 1 to 4.")
        continue
    player_choice = ch(a)

    b = random.randint(1, 3)
    choice = ch(b)
    print(f"Computer choice:{choice} ")
    if choice == player_choice :
        print("Its a draw")
        continue
    elif choice == "rock" and player_choice == "paper" :
        print(f"\n{name}, You win.")
    elif choice == "paper" and player_choice == "scissors" :
        print(f"\n{name}, You win.")
    elif choice == "scissors" and player_choice == "rock" :
        print(f"\n{name}, You win.")
    else :
        print(f"\n{name}, You lose, try again")
