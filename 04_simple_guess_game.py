import random
secret_number = random.randint(1, 10) # thid will select a random number from 1 to 10
name = input("Enter your name: ").strip()
print("I am thinking about a number between 1 to 10, lets see you can guess it!")


while True :
     try :
          guess = int(input("Enter your guess: "))
          
          if guess < 0 or guess > 10 :
              print("Only enter number from 1 to 10.")
          elif guess < secret_number :
              print("Too low, try little higher number")
          elif guess > secret_number :
              print("Too high, try little lower number")
          else :
              print(f"Congrsts, {name} you guessed the right number")
              break
     except ValueError :
         print("Invalid entery, enter only numbers.")
         continue
