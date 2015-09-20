def isPalindrome(x):
    numStr = str(x)
    length = len(numStr)
    firstHalf = numStr[0:int(length / 2)]
    secondHalf = numStr[-int(length / 2):]
    rev = ""
    for i in range(len(secondHalf) - 1, -1, -1):
        rev += secondHalf[i]
    if firstHalf == rev:
        return True
    else:
        return False

possible = []
for x in range(100,1000):
    for y in range(100,1000):
        possible.append(x * y)

possible.sort()
for z in range(len(possible) - 1, 0, -1):
    if isPalindrome(possible[z]):
        print possible[z]
        break
