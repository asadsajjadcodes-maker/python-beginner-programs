# function for checking the greatest number in three numbers entered by the user 
def gn(a, b, c) :
    if a > b and a > c :
        print(f"{a} is the greatest number.")
        return a
    elif b > a and b > c :
        print(f"{b} is the greatest number.")
        return b
    else :
        print(f"{c} is the greatest number.")
        return c

h = int(input("Enter the number: "))
k = int(input("Enter the number: "))
r = int(input("Enter the number: "))

# calling the function 

g = gn(h, k, r)
print(g)