def sumSquare(n):
    total = 0
    while n > 0:
        total += n * n
        n -= 1
    return total

def squareSum(n):
    total = 0
    while n > 0:
        total += n
        n -= 1
    total *= total
    return total

print squareSum(100) - sumSquare(100)

