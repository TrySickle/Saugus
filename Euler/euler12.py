import math
def getFactors(x):
    factorList = []
    factorList.append(1)
    factorList.append(x)
    for y in range (2, int(math.sqrt(x))):
        if x % y == 0:
            factorList.append(y)
    
            factorList.append(int(x / y))
    return factorList

factors = 0
counter = 1
while factors < 500:
    triangle = 0
    for i in range(1, counter + 1):
        triangle += i
    factors = len(getFactors(triangle))
    counter += 1

answer = 0
for i in range(1, counter):
    answer += i

print answer

