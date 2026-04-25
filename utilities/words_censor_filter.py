# List of words that should be censored in the file
words = ["donkey", "dog", "spam"]

# Try block to handle possible errors (like file not found)
try :

    # Open the file and read its contents
    with open("file.txt") as f :
        data = f.read()

        # Check if the file is empty
        if data == "":
            print("file is empty")

    # Convert the text to lowercase so the censoring works consistently
    data = data.lower()

    # Loop through each banned word in the list
    for word in words :

        # Replace the banned word with # symbols of the same length
        data = data.replace(word, "#" * len(word))

    # Open the same file again in write mode to save the censored text
    with open("file.txt", "w") as f :

        # Write the modified (censored) data back into the file
        f.write(data)

        # Print confirmation message
        print("Censoring complete.")

# If the file does not exist, this error will be handled
except FileNotFoundError :

    # Print an error message
    print("Error: The file was not found")