# Multiplication table generator
# This program prints the multiplication table for any number,
# entered by the user 
print("Hi! I can generate a multiplication table for any number you enter.")
while True :
# ask user to enter a number
    n = int(input("Enter your number: "))
# check if user entered the number 0
    if n == 0 :
        print("Number should be bigger than 0 , Multiplication with 0 always 0")
        continue
# using loop to multiply the entered number with 1 to 10
    a = 1
    while a < 11 :
        print(f"{n} * {a} = {n * a}")
        a += 1
    else :
        print("Task is completed")
    break    