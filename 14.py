a = 9**8 + 3**5 - 9
n = 3

res = ''
buk = '0123456789ABCDEF'
while a != 0:
    res = str(a % n) + res
    a = a // n
print(res.count('2'))

for i in '0123456':
    print(res.count(i), i)
print(res)