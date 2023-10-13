# Build a histogram

# Import the course packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import the two datasets
gapminder = pd.read_csv("datasets/gapminder.csv")
brics = pd.read_csv("datasets/brics.csv")

# Create histogram of life_exp data
plt.hist(life_exp, )

# Display histogram
plt.show()

# Build a histogram of life_exp, with 5 bins. Can you tell which bin contains the most observations?
# Build histogram with 5 bins
plt.hist(life_exp, 5)

# Show and clean up plot
plt.show()
plt.clf()

# Build another histogram of life_exp, this time with 20 bins. Is this better?
# Build histogram with 20 bins
plt.hist(life_exp, 20)

# Show and clean up again
plt.show()
plt.clf()

# histogram compare
# Build a histogram of life_exp with 15 bins.
plt.hist(life_exp,15)

# Show and clear plot
plt.show()
plt.clf()

# Build a histogram of life_exp1950, also with 15 bins. Is there a big difference with the histogram for the 2007 data?
plt.hist(life_exp1950, 15)

# Show and clear plot again
plt.show()
plt.clf()



