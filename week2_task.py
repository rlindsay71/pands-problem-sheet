# This program is for calculating a persons Body Mass Index (BMI)
# based on their weight in KG and height in meters.
# Author : Rachel Lindsay
# Resources:  
# https://www.calculator.net/bmi-calculator.html
# https://www.w3resource.com/python-exercises/python-basic-exercise-66.php
# https://docs.python.org/3/tutorial/inputoutput.html

 
 # The code below asks the user to input their height(M) and weight(KG) and assigns them to variables.

myWeight = float(input(" what is your weight in kilograms? "))
myHeight = float(input ("what is your height in meters? "))

# The code below calculates the BMI weight multiplied by height squared
# and rounds the result to two places.

myBMI = round(myWeight / (myHeight **2), 2)

# The following code prints out the persons BMI

print(f"Your BMI is {myBMI}")

# This code uses if and elif statements to decide what range their BMI belongs do and
# prints out the result.

if myBMI <= 18.4:
    print("You are underweight.")
elif myBMI <= 24.9:
    print("You are healthy.")
elif myBMI <= 29.9:
    print("You are over weight.")
elif myBMI <= 34.9:
    print("You are severely over weight.")
elif myBMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")








