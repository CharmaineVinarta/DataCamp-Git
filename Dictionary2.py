# Dictionary Manipulation (1)
# Adding a new key-value pair 
# Add the key 'italy' with the value 'rome' to europe.
# To assert that 'italy' is now a key in europe, print out 'italy' in europe.
# Add another key:value pair to europe: 'poland' is the key, 'warsaw' is the corresponding value.
# Print out europe.

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)
# this return a True value

# Add poland to europe
europe['poland']= 'warsaw'

# Print europe
print(europe)


# Dictionary Manipulation (2)
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'
print(europe)

# Remove australia
del(europe['australia'])

# Print europe
print(europe)

# Dictionariception

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital':'rome','population':59.83}

# Add data to europe under key 'italy'
europe['italy']= {'capital':'rome','population':59.83}

# Print europe
print(europe)
