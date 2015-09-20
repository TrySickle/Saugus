import math
def isPrime(x):
    if x == 2 or x == 3:
        return False
    for y in range(5, int(math.sqrt(x))):
         if x % y == 0:
             return False
    return True

def getFactors(x):
    factorList = []
    for y in range (2, int(math.sqrt(x))):
        if x % y == 0:
            if isPrime(y):
                factorList.append(y)
                #print (y)
            if isPrime(int(x / y)):
                factorList.append(int(x / y))
                #print(int(x / y))
            #print(y)
    return factorList

myList = getFactors(600851475143)
z = myList[0]
for w in myList:
    if (w > z):
        z = w
print z
