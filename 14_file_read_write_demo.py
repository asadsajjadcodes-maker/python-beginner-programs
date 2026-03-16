# Project 14 
# File read and write demo
# Auther: Asad Sajjad
# Description: Demonstrates how to write a file and read from it 

# writing in a file 
a = "Python is easy to read coding language."
f = open("demo_file.txt", "w") # opens the file in writing mode
f.write(a) # writes the data in the file 
f.close() # closes the file 


# reading data from the file 
f = open("demo_file.txt") # opens the file in read mode
data = f.read() # reads the file 
print(data) # prints data 
f.close() # closes the file 


