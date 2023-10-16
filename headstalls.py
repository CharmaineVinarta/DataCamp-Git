import numpy as np
np.random.seed(123)

outcomes=[] #empty list

for x in range(10):
  coin = np.random.randint(0,2) # random integer coin either 0(heads) or 1(tails)
  
  if coin == 0: #if coins is0,append heads to the lists
    outcomes.append("heads")
  else: #else, append tails 
    outcomes.append("tails")

# 10 iteration 
print(outcomes) 
# list with 10 strings
