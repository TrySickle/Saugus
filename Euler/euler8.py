line1 = "73167176531330624919225119674426574742355349194934"
line2 = "96983520312774506326239578318016984801869478851843"
line3 = "85861560789112949495459501737958331952853208805511"
line4 = "12540698747158523863050715693290963295227443043557"
line5 = "66896648950445244523161731856403098711121722383113"
line6 = "62229893423380308135336276614282806444486645238749"
line7 = "30358907296290491560440772390713810515859307960866"
line8 = "70172427121883998797908792274921901699720888093776"
line9 = "65727333001053367881220235421809751254540594752243"
line10 = "52584907711670556013604839586446706324415722155397"
line11 = "53697817977846174064955149290862569321978468622482"
line12 = "83972241375657056057490261407972968652414535100474"
line13 = "82166370484403199890008895243450658541227588666881"
line14 = "16427171479924442928230863465674813919123162824586"
line15 = "17866458359124566529476545682848912883142607690042"
line16 = "24219022671055626321111109370544217506941658960408"
line17 = "07198403850962455444362981230987879927244284909188"
line18 = "84580156166097919133875499200524063689912560717606"
line19 = "05886116467109405077541002256983155200055935729725"
line20 = "71636269561882670428252483600823257530420752963450"

twoD = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10,
      line11, line12, line13, line14, line15, line16, line17, line18, line19, line20]

megaStr = ""
for x in range(0, 20):
    megaStr += twoD[x]

def findProduct(s):
    total = 1
    for n in s:
        total *= int(n)
    return total

testStr = ""
x = 0
maxProduct = 0
while x < 987:
    testStr = megaStr[x : x + 13]
    if findProduct(testStr) > maxProduct:
        maxProduct = findProduct(testStr)
    x += 1

print maxProduct
  
            
