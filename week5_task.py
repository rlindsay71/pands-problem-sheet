# This program detects whether today is a weekday or not
# resource delftstack.com
# author:  Rachel Lindsay

# The following code imports the datetime module

from datetime import datetime

#  this code returns the current day of the week as an integer
#  e.g monday is equal to 1, tuesday is 2, etc

whichday = datetime.today().isoweekday()

if whichday < 6:
     print(" Yes, sadly its a weekday and you don't get a lie on")
else:
     print("Yahoo!  its the weekend and I get to lie on")

    

#print(datetime.today().isoweekday())