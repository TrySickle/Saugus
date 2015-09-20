import math

def eratosthenes(n):
    numbers = []
    for i in range(2, n):
        numbers.append([i, True])

    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if numbers[i - 2][1]:
            #print numbers[i - 2][0]
            for j in range(i ** 2, n, i):
                numbers[j - 2][1] = False

    return numbers

n = 2000000

total = 0
primes = eratosthenes(n)
for i in primes:
    if i[1] == True:
        total += i[0]

print total
        
