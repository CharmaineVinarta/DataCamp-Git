# Import the course packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import the two datasets
gapminder = pd.read_csv("datasets/gapminder.csv")
brics = pd.read_csv("datasets/brics.csv") 

# Explore Datasets

# Instructions 
# print() the last item from both the year and the pop list to see what the predicted population for the year 2100 is. Use two print() functions.
# Before you can start, you should import matplotlib.pyplot as plt. pyplot is a sub-package of matplotlib, hence the dot.
# Use plt.plot() to build a line plot. year should be mapped on the horizontal axis, pop on the vertical axis. 
# Don't forget to finish off with the plt.show() function to actually display the plot.

# Print the last item from year and pop
print(year)
print(pop)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
plt.show()

# Bubble Chart
# life_exp which contains the life expectancy for each country and
# gdp_cap, which contains the GDP per capita (i.e. per person) for each country expressed in US Dollars.

# Print the last item from both the list gdp_cap, and the list life_exp; it is information about Zimbabwe.
# Build a line chart, with gdp_cap on the x-axis, and life_exp on the y-axis. Does it make sense to plot this data on a line plot?
# Don't forget to finish off with a plt.show() command, to actually display the plot.

# Print the last item of gdp_cap and life_exp
print(gdp_cap)
print(life_exp)

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap,life_exp)

# Display the plot
plt.show()
