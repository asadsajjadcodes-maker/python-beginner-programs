l = True
while l == True :
    a = int(input("Enter 1 to calculate \n Enter 2 to exit: "))
    if a == 1 :
        n1 = int(input("Enter first number: "))
        operator = input("Select operator ( + - * / ): ").strip()
        n2 = int(input("Enter second number: "))
# calculating results on the basis of operator seleceted
    
        if operator == "+" :
            print(f"Sum = {n1 + n2}")
        elif operator == "-" :
            print(f"Subtraction = {n1 - n2}")
        elif operator == "*" :
            print(f"Multiplication = {n1 * n2}")
        elif operator == "/" :
            print(f"Division = {n1 / n2}")
    elif a == 2 :
        print("\n Program finished, Thank you.")
        print("""

\t Author: Asad Sajjad
""")
        break
    else :
        print("\n Invalid choice, Please enter 1 or 2.")