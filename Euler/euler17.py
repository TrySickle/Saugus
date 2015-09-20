# Number letter counts
# one two three four five six seven eight nine ten
# ten eleven 6 twelve 6 thirteen 8 fourteen 8 fifteen 7 sixteen 7 seventeen 9 eighteen 8 nineteen 8
# twenty 6 thirty 6 forty 5 fifty 5 sixty 5 seventy 7 eighty 6 ninety 6 
# first approach was converting numbers mostly
"""def getCount(s):
    total = 0
    strS = str(s)

    if len(strS) == 1:
        total += onesPlace(strS)
    elif len(strS) == 2:

    elif len(strS) == 3:

    else:
        total += 3 + 8

    return total

def onesPlace(s):
    if s == "1" or s == "2" or s == "6":
        return 3
    elif s == "4" or s == "5":
        return """

# second approach, convert numbers to words, use len
def getWord(n):
    strN = str(n)
    word = ""
    
    if len(strN) > 3:
        word += "onethousand"
        strN = ""
    if len(strN) > 2:
        if strN[0] == "1":
            word += "one"
        elif strN[0] == "2":
            word += "two"
        elif strN[0] == "3":
            word += "three"
        elif strN[0] == "4":
            word += "four"
        elif strN[0] == "5":
            word += "five"
        elif strN[0] == "6":
            word += "six"
        elif strN[0] == "7":
            word += "seven"
        elif strN[0] == "8":
            word += "eight"
        elif strN[0] == "9":
            word += "nine"
        word += "hundred"
        strN = strN[1:]
    if len(strN) > 1:
        if (strN[0] != "0" or strN[1] != "0") and n > 99:
            word += "and"
        if strN[0] == "1":
            if strN[1] == "0":
                word += "ten"
            elif strN[1] == "1" or strN[1] == "2":
                word += "eleven"
            elif strN[1] == "5" or strN[1] == "6":
                word += "fifteen"
            elif strN[1] == "3" or strN[1] == "4" or strN[1] == "8" or strN[1] == "9":
                word += "thirteen"
            elif strN[1] == "7":
                word += "seventeen"
            strN = strN[0]
        if strN[0] == "4" or strN[0] == "5" or strN[0] == "6":
            word += "forty"
        elif strN[0] == "2" or strN[0] == "3" or strN[0] == "8" or strN[0] == "9":
            word += "twenty"
        elif strN[0] == "7":
            word += "seventy"
        strN = strN[1:]
    if len(strN) > 0:
        if strN[0] == "1":
            word += "one"
        elif strN[0] == "2":
            word += "two"
        elif strN[0] == "3":
            word += "three"
        elif strN[0] == "4":
            word += "four"
        elif strN[0] == "5":
            word += "five"
        elif strN[0] == "6":
            word += "six"
        elif strN[0] == "7":
            word += "seven"
        elif strN[0] == "8":
            word += "eight"
        elif strN[0] == "9":
            word += "nine"

    return word

total = 0
for i in range(1, 1001):
    print getWord(i)
    total += len(getWord(i))

print total
