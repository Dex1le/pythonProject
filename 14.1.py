chek = []
for x in '0123456789ABC':
    for y in '0123456789ABC':
        a = int('8' + x + '78' + y, 13) + int('79' + x + y + '7', 18)
        if a % 9 == 0:
            chek.append(a)
            print(a // 9, x, y)