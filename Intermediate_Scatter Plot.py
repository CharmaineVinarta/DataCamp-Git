# Import the course packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import the two datasets
gapminder = pd.read_csv("datasets/gapminder.csv")
brics = pd.read_csv("datasets/brics.csv")

# SCATTER PLOT
# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()

# Build a scatter plot, where pop is mapped on the horizontal axis, and life_exp is mapped on the vertical axis.
# Build Scatter plot
plt.scatter(pop,life_exp)

# Finish the script with plt.show() to actually display the plot. Do you see a correlation?
# Show plot
plt.show()
