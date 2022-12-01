vs = []
for a in range(200):
    flag = True
    for x in range(200):
        for y in range(200):
            f = ((x < 6) <= (x**2 < a)) and ((y**2 <= a) <= (y <= 6))
            if f == 0:
                flag = False
                break
    if flag:
        vs.append(a)
print(len(vs))
