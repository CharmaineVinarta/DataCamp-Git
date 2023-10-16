import numpy as np
np.random.seed(123)
tails = [0] # create list tais contains 0, bcoz at start havent throw any tails 

for x in range(10): # run for loops 10x using range function
  coin = np.random.randint(0,2) #generate random numbers
  tails.append(tails[x] + coin) # if 1 is generated,the number of tailsshouldnt be incremenated

print(tails)

