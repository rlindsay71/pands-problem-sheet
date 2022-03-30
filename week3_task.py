# This program lets the user input a string
# and returns every second letter of their sentence in reverse order
# resources : https://www.w3schools.com/python/python_howto_reverse_string.asp
# https://realpython.com/reverse-string-python/#reversing-strings-through-slicing

# the following code asks the user to imput a string
txt = input("please enter a sentence: ") 

# the following code creates a new variable from the original string entered which is reversed and outputs
# every second letter

reversetxt = txt [-1::-2]


print(reversetxt)

 