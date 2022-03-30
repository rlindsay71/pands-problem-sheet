#  The following program asks the user to input any positive integer
#  and outputs the successive values of the following calculation.
#  At each step the program calculates the next value by taking the current value and,
#  if it is even, divides it by two,
#  but if it is odd, it multiplies the value by three and adds one.
#  The program ends if the value is one.
#  Author:  Rachel Lindsay
#  Resources:  www.w3schools.org
#  https://realpython.com/python-append/
# https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
#              

x = int(input("Please enter a positive integer number:\t"))

numbercalc = [x]

# this code runs a while loop while x is bigger than 1, if the number is even, the code divides it by two,
#  but if it is odd, it multiplies the value by three and adds one.
#  If x is 1, the code exits the loop
#  through each interation of the loop, the value is appended to the numbercalc list variable.

while x > 1:
    if  x % 2 == 0:   
          x = x / 2
          numbercalc.append(int(x))

    else: 
          x = (x * 3 ) + 1
          numbercalc.append(int(x))
          
# the code below unpacks the contents of the list to print them all in one line, without the list brackets.

print(*numbercalc, sep=", ")









