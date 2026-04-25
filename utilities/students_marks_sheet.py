# marks sheet 
subject_marks = 200
pass_marks_percentage = 33
total_marks = 800
total_pass_marks_percentage = 40

biology = int(input("Enter the marks obtained in Biology from 200: "))
physics = int(input("Enter the marks obtained in Physics from 200: "))
chemistry = int(input("Enter the marks obtained in Chemistry from 200: "))
math = int(input("Enter the marks obtained in Math from 200: "))

# total percentage method

total_percentage = ((biology + physics + chemistry + math) * (100)) / total_marks

# percentage of marks by subject

biology_marks_percentage = (biology * 100) / subject_marks
physics_marks_percentage = (physics * 100) / subject_marks
chemistry_marks_percentage = (chemistry * 100) / subject_marks
math_marks_percentage = (math * 100) / subject_marks

# printing results and making decision of pass or fail
# biology

if biology_marks_percentage >= pass_marks_percentage :
    print("Percentage in Biology: ",biology_marks_percentage,"% pass")
else:
    print("Percentage in Biology: ",biology_marks_percentage,"% fail")

# physics 

if physics_marks_percentage >= pass_marks_percentage :
    print("Percentage in Physics: ",physics_marks_percentage,"% pass")
else:
    print("Percentage in Physics: ",physics_marks_percentage,"% fail")

# chemistry 

if chemistry_marks_percentage >= pass_marks_percentage :
    print("Percentage in Chemistry: ",chemistry_marks_percentage,"% pass")
else:
    print("Percentage in Chemistry: ",chemistry_marks_percentage,"% fail")

# math 

if math_marks_percentage >= pass_marks_percentage :
    print("Percentage in Math: ",math_marks_percentage,"% pass")
else:
    print("Percentage in Math: ",math_marks_percentage,"% fail")

# total percentage if less than 40 % 

print("Total percentage",total_percentage,"%")
if total_percentage < total_pass_marks_percentage :
    print("Because total percentage is less than 40 %")

if total_percentage >= total_pass_marks_percentage and biology_marks_percentage >= pass_marks_percentage and physics_marks_percentage >= pass_marks_percentage and chemistry_marks_percentage >=pass_marks_percentage and math_marks_percentage >=pass_marks_percentage :
    print("You are passed.")
else:
    print("Because your marks in subject are less than 33 %")
    print("You are failed.")
# program finished