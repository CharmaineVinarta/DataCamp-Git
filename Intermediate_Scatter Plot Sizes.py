# A list pop savesd in workspace, contains population numbers for each country expressed in millions.
# Import the course packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import the two datasets
gapminder = pd.read_csv("datasets/gapminder.csv")
brics = pd.read_csv("datasets/brics.csv")


# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop * 2


# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()
