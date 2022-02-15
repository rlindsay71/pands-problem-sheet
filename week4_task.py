#  The following program asks the user to input any positive integer
#  and outputs the successive values of the following calculation.
#  At each step the program calculates the next value by taking the current value and,
#  if it is even, divides it by two,
#  but if it is odd, it multiplies the value by three and adds one.
#  The program ends if the value is one.
#  Author:  Rachel Lindsay
#  Resources:  www.w3schools.org
#              week 4 videos and labs

x = int(input("Please enter a positive integer number:\t"))
print(x)

while x > 1:
    if  x % 2 == 0:   
          x = x / 2
          print(int(x))
    else: 
          x = (x * 3 ) + 1
          print(int(x))







