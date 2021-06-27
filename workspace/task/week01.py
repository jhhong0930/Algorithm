# 1
count = 0
for i in range(1, 7):
    if i > 1 and i % 2 == 1:
        count += 2
    else:
        count += 1
    print('*' * count)

# 2
a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
a = list(map(str, map(lambda x: x + 1, map(int, a))))
print(a)

# 3
a = ['base ball', 'basket ball', 'soccer', 'base ball', 'soccer', 'soccer', 'basket ball', 'base ball', 'basket ball',
     'soccer', 'basket ball', 'basket ball', 'base ball', 'soccer', 'soccer', 'basket ball', 'basket ball', 'base ball', 'base ball']
b = dict()

for i in a:
    b[i] = 0
for i in a:
    if i in a:
        b[i] += 1
for k, v in b.items():
    print(k, v)

# 4
for i in range(-1, 11):
    if i < 9:
        print(int(2 ** i), end=" ")
    else:
        print(2 ** 8, end=" ")