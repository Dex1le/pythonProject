import time
s1 = time.time()

buk = 'metro'
buk1 = '123456789ab'
buk2 = '02468a'
k = 0
for a1 in buk:
    for a2 in buk:
        for a3 in buk:
            for a4 in buk:
                s = a1 + a2 + a3 + a4
                k += 1
print(k)

s2 = time.time()
print(s2 - s1)
