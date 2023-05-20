'''Even if you haven't studied physics (recently or ever!), you might have heard that , wherein 
 represents energy (measured in Joules), represents mass (measured in kilograms), and 
 represents the speed of light (measured approximately as 300000000 meters per second), per 
 Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent. '''

# Get a mass, in kilograms, from the user and cast it to its integer value.
mass = int(input("Mass: ").strip())

# E = mc²
constant = 300000000
energy = (mass * constant**2)

# Print the result, in joules, to the console.
print(energy)