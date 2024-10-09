import random
pole1 = [1,22,13,45,9,61,37,89,4,]
print(pole1)


prvni = pole1[0]
prostedni = pole1[len(pole1) // 2]
posledni = pole1[-1]

print("první hodnota:", prvni)
print("prostřední hodnota:", prostedni)
print("poslední hodnota:", posledni)

pole1[5]=34
print(pole1)

pole7 = pole1[7]
print( pole7)


print(len(pole1))

#minimální a maximální hodnota obou pole A
print(min(pole1))
print(max(pole1))

pole2 = [6,2,10,15,7,9,11,4,]
print(pole2)



#sečtení obou polí 
print(sum(pole1+pole2))


soucet = pole2[1] + pole2[5]
print(soucet)

pole_auto=list(range(1,9))
random.shuffle(pole_auto)
print(pole_auto)









