#  The following Program reads a specified file and will return the count of a given letter.
#  resource: www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
#  www.w3schools.com/python/python_file_open.asp
#  pythonexamples.org/python-count-occurrences-of-word-in-text-file/
#  stackoverflow.com/questions/8280250/how-to-open-files-given-as-command-line-arguments-in-python
#  Author: Rachel Lindsay

# the following imports the sys library which allows the user to input the filename to be read
# from the commandline

import sys

# this code takes in the file name as a command line arguement.
file_name = sys.argv[1]
# the file is opened here to be read
f = open(file_name, 'r')
# here, the file is stored in a variable
data = f.read()
# The count function is used to count the frequency of e 
lettercounter = data.count('e')

print("The number of instances of the letter e is: ", lettercounter)





