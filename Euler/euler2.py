x = 1
y = 2
total = 0
while y < 4000000:
    if y % 2 == 0:
        total += y
    temp = x + y
    x = y
    y = temp
print total
