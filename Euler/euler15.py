import math

counter = 0
def getLattice(dimension, x, y):
    if x == dimension and y == dimension:
        global counter
        counter += 1
        #print counter
    else:
        if x < dimension:
            getLattice(dimension, x + 1, y)
        if y < dimension:
            getLattice(dimension, x, y + 1)

#getLattice(14, 0, 0)
#print counter

#well it's pascal's triangle, fuck me, apparently it's 2n C n

print math.factorial(2 * 20) / (math.factorial(20) * math.factorial(20))


