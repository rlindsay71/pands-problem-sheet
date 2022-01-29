# This program is for calculating a person Body Mass Index (BMI)
# based on their weight in KG and height in meters.
# Author : Rachel Lindsay
# Week 2, weekly task, Programming & Scripting course

myWeight = float(input(" what is your weight in kilograms?"))
myHeight = float(input ("what is your height in meters?"))

# This code squares the height input

myHeightsquared = myHeight ** 2

# This code calculates the BMI

myBMI = myWeight // myHeightsquared

print(myBMI)



