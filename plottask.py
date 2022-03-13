
# the following program displays a plot of the functions
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# resources: https://www.w3schools.com/python/matplotlib_plotting.asp
# https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
# Author:  Rachel Lindsay


import matplotlib.pyplot as plt
import numpy as np

# This code products a list of 0,1,2,3 as values to pass to the x coordinates
x = np.array(range(0,4))


# This code passes the values of x, x squared and x cubed to the following variables which will be our
# y coordinates for the 3 lines
F = x
G = x ** 2
H = x ** 3

# Here, the scale of the plot is set to 0 to 30 for both the x and y axises.

plt.xlim(0,30)
plt.ylim(0,30)

# A legend is set for the plot here,
plt.legend

# The three lines are now plotted on the axis set.

plt.plot(x,F,label = "X", color ="blue")
plt.plot(x,G,label = "Square of X", color ="red")
plt.plot(x,H,label = "Cube of X", color ="green")
plt.legend()

plt.show()

