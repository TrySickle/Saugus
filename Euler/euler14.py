def collatz(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return 1 + collatz(n / 2)
        else:
            return 1 + collatz(3 * n + 1)

maxTerms = 0
maxI = 0
for i in range(1, 1000000):
    terms = collatz(i)
    if terms > maxTerms:
        maxTerms = terms
        maxI = i

print maxTerms
print maxI
