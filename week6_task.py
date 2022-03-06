# The following program asks the user to input a number and returns its square root.
# Resource:  https://www.goeduhub.com
# Author Rachel Lindsay


def findnumberroot(number, rootcalc = 100):

    a = float(number) 

    for i in range(rootcalc): 

# The following code calculates the square root using newtons method

        number = 0.5 * (number + a / number) 

    return number


a=int(input("Please enter a positive number "))

print("The square root of", a ,  "is",findnumberroot(a))


