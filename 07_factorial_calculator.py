# calculating the factorial of a number entered by the user 
n = int(input("Enter the number: "))
result = 1 
for i in range (1, n+1) :
    result *= i
print(f"the factorial of {n} is = {result}")