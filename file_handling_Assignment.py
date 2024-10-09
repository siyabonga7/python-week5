#File Creation
try:
    with open("my_file.txt", 'w') as file:
        file.write("Hello, this is the first line.\n")
        file.write("The second line contains a number: 25.\n")
        file.write("Finally, here is the third line.\n")
    print("File 'my_file.txt' created and written successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error creating the file: {e}")
    

#File Reading and Display
try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\nContents of 'my_file.txt':")
        print(content)

except (FileNotFoundError, PermissionError) as e:
    print(f"Error reading the file: {e}")

#File Appending
try:
    with open("my_file.txt", 'a') as file:
        file.write("Appending a fourth line to the file.\n")
        file.write("Appending the fifth line: 100.\n")
        file.write("And here is the sixth line.\n")
    print("Additional lines appended to 'my_file.txt' successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error appending to the file: {e}")

#Error Handling
finally:
    print("\nFile handling tasks completed.")