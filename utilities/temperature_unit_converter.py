# for faharenheit to celsius 
def f_to_c(f) :
    return (f - 32) * 5 / 9

# for celsius to fahrenheit conversion 
def c_to_f(c) :
    return (c * (9 / 5) ) + 32

# asking the user to choose the operation 
while True :
    print("You can choose an option by entring the 1, 2 or 3.")
    print("1. Celsius to fahrenheit.")
    print("2. Fahrenheit to celsius.")
    print("3. Exit.")
    a = int(input("Choose one option: "))

    if a == 1 :
        c = int(input("Enter the temperature in celsius: "))
        s = c_to_f(c)
        print(f"{round(s, 2)}°F")

    elif a == 2 :
        f = int(input("Enter the temperature in fahrenheit: "))
        d = f_to_c(f)
        print(f"{round(d, 2)}°C")

    else :
        print("Thank you for using convertor.")
        break