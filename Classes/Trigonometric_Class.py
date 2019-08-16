import numpy as np
import matplotlib.pyplot as plot  # Importing 'matplotlib.pyplot' to draw trigonometric functions.
import math  # Importing {math} module to calculate the values of trigonometric functions.


class Trigonometric:
    def __init__(self):  # Class Constructor
        pass

    def Sin_value(self, angle):  # Method {Sin_value} to calculate the value of Sin for the angle in the parameter.
        return math.sin(angle)   # Calculating the value of sin for the angle in the prameter using {sin()} function from {math} module.

    def Cos_value(self, angle):  # Method {Cos_value} to calculate the value of Cos for the angle in the parameter.
        return math.cos(angle)   # Calculating the value of cos for the angle in the prameter using {cos()} function from {math} module.

    def Tan_value(self, angle):  # Method {Tan_value} to calculate the value of Tan for the angle in the parameter.
        return math.tan(angle)   # Calculating the value of tan for the angle in the prameter using {tan()} function from {math} module.


class Graphs:
    def __init__(self):  # Class Constructor
        pass

    def Sine_Graph(self, angle, angle_str):  # Method {Sine_Graph} to draw the graph of sine function.
        x = np.arange(0, angle, 0.1)  # Defining the bounds of the graph using {arrange()} function from {numpy} module.
        plot.plot(x, np.sin(x), color='black')  # Designing the graph using {plot()} function from {matplotlib.pyplot} module.
        plot.title("Sine ("+angle_str+") graph", color="blue")  # Creating the title of the graph using {title()} function from {matplotlib.pyplot} module.
        plot.show()  # Displaying the graph using {show()} function from {matplotlib.pyplot} module.

    def Cosine_Graph(self, angle, angle_str):  # Method {Cosine_Graph} to draw the graph of cosine function.
        x = np.arange(0, angle, 0.1)  # Defining the bounds of the graph using {arrange()} function from {numpy} module.
        plot.plot(x, np.cos(x), color='black')  # Designing the graph using {plot()} function from {matplotlib.pyplot} module.
        plot.title("Cosine ("+angle_str+") graph", color="blue")  # Creating the title of the graph using {title()} function from {matplotlib.pyplot} module.
        plot.show()  # Displaying the graph using {show()} function from {matplotlib.pyplot} module.

    def Tan_Graph(self):  # Method {Tan_Graph} to draw the graph of Tan function.
        x = np.linspace(np.pi * -2, np.pi * 2, 1000)  # Defining the bounds of the graph using {linspace()} function from {numpy} module.
        plot.plot(x, np.tan(x), color='black')  # Designing the graph using {plot()} function from {matplotlib.pyplot} module.
        plot.ylim(-5, 5)  # Defining the limits of the 'y' axis using {ylim()} function from {matplotlib.pyplot} module.
        plot.title("Tan () graph", color="blue")  # Creating the title of the graph using {title()} function from {matplotlib.pyplot} module.
        plot.show()  # Displaying the graph using {show()} function from {matplotlib.pyplot} module.

