# student marks analyzer

marks_list = []
# asking user to enter the marks of 5 students 

for i in range (5) :
    marks = int(input("Enter the marks: "))
# adding marks in a list 
    marks_list.append(marks)
# analyzing 
print(f"Highest marks: {max(marks_list)}") 
print(f"Lowest marks: {min(marks_list)}") 
print(f"Average marks: {sum(marks_list)/len(marks_list)}") 
print(f"Total marks: {sum(marks_list)}") 