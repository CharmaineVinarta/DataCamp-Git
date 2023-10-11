# As a data scientist, some notions of geometry never hurt. 

# For a fancy clustering algorithm, you want to find the circumference, , and area, , of a circle. 
# When the radius of the circle is r, you can calculate  and  as:
C = 2πr
A = πr2

# In Python, the symbol for exponentiation is **. This operator raises the number to its left to the power of the number to its right. 
# For example 3**4 is 3 to the power of 4 and will give 81.

# To use the constant pi, you'll need the math package. A variable r is already coded in the script. 
# Fill in the code to calculate C and A and see how the print() functions create some nice printouts.

# Import the math package. Now you can access the constant pi with math.pi.
# Calculate the circumference of the circle and store it in C.
# Calculate the area of the circle and store it in A.

# Import the math package
import math

# Definition of radius
r = 0.43

# Calculate C
C = 2 * math.pi * r
# Calculate A
A = math.pi * r **  2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))
