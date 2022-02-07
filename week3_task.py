#This program lets the user input a string
#and returns every second letter of their sentence in reverse order
#resources : https://www.w3schools.com/python/python_howto_reverse_string.asp
# https://realpython.com/reverse-string-python/#reversing-strings-through-slicing


txt = input("please enter a sentence:\n") 

reversetxt = txt [-2::-2]

print(reversetxt)

 