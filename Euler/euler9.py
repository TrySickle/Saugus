def findTriplets():
    triplets = []
    for x in range(1, 999):
        for y in range(1, 1000 - x):
            z = 1000 - x - y
            if x ** 2 + y ** 2 == z ** 2:
                triplets.append([x, y, z])
    return triplets

triplets = findTriplets()
print triplets[0][0] * triplets[0][1] * triplets[0][2]
