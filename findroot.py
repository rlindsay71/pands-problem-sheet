# The following program asks the user to input a number and returns its square root.
# Resource:  https://www.goeduhub.com
# Author Rachel Lindsay


def findnumberroot(number):
    a = float(number) 

# The following code calculates the square root using newtons method

    number = 0.5 * (number + a / number) 

    return number


a=int(input("Please enter a number "))

print("The square root of this number is: ",findnumberroot(a))

