# Make a colorful Plot
# It's a list with a color for each corresponding country, depending on the continent the country is part of.
# The Gapminder data contains a list continent with the continent each country belongs to. A dictionary is constructed that maps continents onto colors:

# Import the course packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import the two datasets
gapminder = pd.read_csv("datasets/gapminder.csv")
brics = pd.read_csv("datasets/brics.csv") 

dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}

# Specify c and alpha inside plt.scatter()
# Change the opacity of the bubbles by setting the alpha argument to 0.8 inside plt.scatter()
# Col function to put a color
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c =col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations, adding a name to the map locations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()
