"""
Project 14: File Read & Write Demo
Author: Asad Sajjad
Description:
This program demonstrates how to:
1. Write text to a file
2. Append new text to the file
3. Read file contents
4. Check if a specific word exists in the file
"""

a = """Python is a versatile, high-level programming language first 
released in 1991 by \"Guido van Rossum\", who named it after the British comedy troupe 
Monty Python. It is celebrated for its clean, English-like syntax and its use of 
significant indentation, which makes the code highly readable and reduces maintenance 
costs. As a general-purpose language, Python is used extensively across diverse 
fields such as web development, data science, artificial intelligence, and automation. 
Major companies like Google, Netflix, and Instagram rely on its powerful libraries 
and frameworks to build everything from recommendation algorithms to complex 
scientific models. Because it is open-source and beginner-friendly, Python 
continues to be one of the fastest-growing and most popular languages in the 
global developer community."""

# write file 
with open("python_introduction.txt", "w") as f :
    f.write(a)
    print("File saved sucessfully")




b = """\nPython is a powerhouse in modern technology, used extensively 
for data science and machine learning to analyze complex datasets and build 
predictive models. In web development, frameworks like Django and Flask allow 
developers to build scalable back-end systems quickly. Beyond the web, Python 
is the go-to language for automation and scripting, helping users streamline 
repetitive tasks like file management or web scraping. It also plays a vital 
role in scientific computing, software testing, and even game development, 
making it one of the most versatile tools in a programmer's toolkit."""
# append file 
with open("python_introduction.txt", "a") as f :
    f.write(b)
    print("New data added sucessfully")

# read file
with open("python_introduction.txt") as f :
    data = f.read()

# cheacking if the "python" word is in the file
    
    if "python" in data.lower() :
        print("Yes the word python is present in the file.")
    else :
        print("The word python is not present in the file.")
# printing the file with new added data

    print("\n", data)
