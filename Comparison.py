# Write Python expressions, wrapped in a print() function, to check whether:
# x is greater than or equal to -10. x has already been defined for you.
# "test" is less than or equal to y. y has already been defined for you.
# True is greater than False.
  
# Comparison of integers
x = -3 * 6

# Comparison of strings
y = "test"

# Comparison of booleans
print(x >= -10)
print("test" <= y)
print(True > False)

# Compare Arrays
# Using comparison operators, generate boolean arrays that answer the following questions:

# Which areas in my_house are greater than or equal to 18?
# You can also compare two NumPy arrays element-wise. Which areas in my_house are smaller than the ones in your_house?
# Make sure to wrap both commands in a print() statement so that you can inspect the output!

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)
