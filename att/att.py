znamky = [0]
c = 0
b = 1
d = 0
while True:
    if b != 0 & b<6:
        b = int(input("zadaj znamku: "))
        znamky.append(int(b))
        c = c+1
    else:
        break

pocet = c-1
print("pocet: " + str(pocet))
for i in range(len(znamky)-1):
    d = d+znamky[i]
priemer = d/(len(znamky)-1)
print("priemer: " + str(priemer))