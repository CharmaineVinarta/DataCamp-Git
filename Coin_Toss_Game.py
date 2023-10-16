import numpy as np
np.random.seed(123)
coin=np.random.ranint(0,2) #randomly generate 0 or 1
print(coin) # we will get 0

# usethe coin to play thegame
if coin == 0:
  print("heads")
else:
  print("tails")


# Use randint() with the appropriate arguments to randomly generate the integer 1, 2, 3, 4, 5 or 6. This simulates a dice. Print it out.
# Repeat the outcome to see if the second throw is different. Again, print out the result.
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
np.random.randint(1,7)
print("heads")

# Use randint() again
np.random.randint(1,7)
print(3)


# determining the nexr move
# NumPy is imported, seed is set
import numpy as np
np.random.seed(123)

# Starting step
step = 48
dice = np.random.randint(1,7)

# Roll the dice
np.random.randint(1,51)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)
