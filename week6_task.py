# The following program asks the user to input a postive number and returns its square root.
# Resource:  https://www.goeduhub.com
# https://thirumalai2024.medium.com/python-program-to-find-square-root-of-the-number-using-newtons-method-937c0e732756
# Author Rachel Lindsay



def numberSqrRoot(a):

    # the folowing code uses a while loop to iterate through an approximate
    # result and a result from newtons formula, until both results have reached the closed level of precision
    # i.e are equal so the code knows it has reached the correct square root result.
    # when this stage is reached, the number that the user inputs divided by 2 (approxnbr) will be equal 
    # to the result from newtons formula (betternbr) and the loop is finished and returns the correct result

    approxnbr = 0.5 * a
    betternbr = 0.5 * (approxnbr + a / approxnbr)
    
    while betternbr != approxnbr:
        approxnbr = betternbr

        betternbr =0.5*(approxnbr + a  / approxnbr)
    return approxnbr

a = int(input("Please enter a positive number "))

print("The square root of", a ,  "is",numberSqrRoot(a))

