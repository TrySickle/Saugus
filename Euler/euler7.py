import math
def isPrime(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0:
        return False
    for y in range(3, x / 2, 2):
         if x % y == 0:
             return False
    return True

counter = 2
check = 6
while True:
    if isPrime(check - 1):
        counter += 1
        if counter == 10001:
            print check - 1
            break
    if isPrime(check + 1):
        counter += 1
        if counter == 10001:
            print check + 1
            break
    check += 6
