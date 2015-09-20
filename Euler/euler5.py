x = 19
while True:
    if x % 19 == 0 and x % 17 == 0 and x % 16 == 0 and x % 11 == 0 and x % 13 == 0 and x % 20 == 0 and x % 18 == 0 and x % 7 == 0:
        print x
        break
    x += 19
