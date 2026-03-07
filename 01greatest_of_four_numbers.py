n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))
n3 = int(input("Enter your third number: "))
n4 = int(input("Enter your fourth number: "))

# if-else ladder to find the greatest number

if n1 >= n2 and n1 >= n3 and n1 >= n4:
    print(f"{n1} is the greatest number.")
elif n2 >= n1 and n2 >= n3 and n2 >= n4:
    print(f"{n2} is the greatest number.")
elif n3 >= n1 and n3 >= n2 and n3 >= n4:
    print(f"{n3} is the greatest number.")
else:
    print(f"{n4} is the greatest number.")
print("End program")
