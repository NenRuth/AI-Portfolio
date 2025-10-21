# Concept          | Meaning (Simple)                                     | Example                        |
# | ---------------- | ---------------------------------------------------- | ------------------------------ |
# | **File**         | A place to store data your program can read or write | `notes.txt`                    |
# | **Read**         | Look at the contents of a file                       | `open("file.txt", "r")`        |
# | **Write**        | Save information into a file                         | `open("file.txt", "w")`        |
# | **Exception**    | An error that happens during program execution       | File not found, divide by zero |
# | **try / except** | A way to handle errors so your program doesn’t crash | `try: ... except: ...`         |

# The with keyword makes sure Python closes the file automatically when done.

# # Writing to a file
# opens this file, reads it, and prints the contents of the file to the screen: 

# with open('pi_digits.txt') as file_object:
# contents = file_object.read()
# print(contents)

# with open("notes.txt", "w") as file:
#     file.write("Hello! This is my first note.")

# # Reading from a file
# with open("notes.txt", "r") as file:
#     content = file.read()
#     print(content)

# Exceptions
# try:
#     file = open("notes.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("Oops! The file was not found.")
# finally:
#     print("Done trying to read the file.")

#     Explanation:

# try: → "Hey, Python, try to do this..."

# except: → "...but if it fails, do this instead."

# finally: → "...no matter what happens, do this at the end." 

# To get Python to open files from a directory other
# than the one where your program file is stored, you need to provide a file
# path, which tells Python to look in a specific location on your system.
# On Windows systems, you use with open('text_files\filename.txt') as file_object:

# You can also tell Python exactly where the file is on your computer
# regardless of where the program that’s being executed is stored.
# on Windows they look like this:
# file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
# with open(file_path) as file_object:


# with open('pi_digits.txt') as file_object:
# 	contents = file_object.read()
# 	print(contents)

#Reading Line by Line
#You can use a for loop on the file object to examine each line from a file one at a time:
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
# 	for line in file_object:
# 		print(line)

## print(line.rstrip()): this will remove the blank spaces on each line. 

# #Making a List of Lines from a File
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
# 	lines = file_object.readlines()
# 	for line in lines:
# 		print(line.rstrip())


#Working with a File’s Contents
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
# 	lines = file_object.readlines()
# pi_string = ''
# for line in lines:
# 	pi_string += line.rstrip()
# print(pi_string)
# print(len(pi_string))


#Writing to an Empty File
# filename = 'programming.txt'
# message.py
# with open(filename, 'w') as file_object:  #this line has 2 arguments, 1st open() the file, 2nd tells py that we want to open the file in write mode.
# 	file_object.write("I love programming.")

#You can open a file in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows
# you to read and write to the file ('r+').

# Note Python can only write strings to a text file. If you want to store numerical data in a text file, 
# you’ll have to convert the data to string format first using the str() function.