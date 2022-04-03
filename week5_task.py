# This program detects whether today is a weekday or not
# resource https://www.delftstack.com/howto/python/python-datetime-day-of-week/#:~:text=In%20Python%2C%20weekday()%20can,0%20and%20Sunday%20is%206.
# https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
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