# 리스트(순서o, 중복o, 수정o, 삭제o)
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'pen', 'banana', 'orange']
e = [10, 100, ['pen', 'banana', 'orange']]

# 인덱싱
print(d[3]) # banana
print(d[-1]) # orange
print(d[0] + d[1]) # 110
print(e[-1]) # ['pen', 'banana', 'orange']

# 슬라이싱
print(d[0:2]) # [10, 100]
print(e[2][1:3]) # ['banana', 'orange']

# 리스트 수정, 삭제
c[0] = 77
c[1:2] = [100, 1000, 10000]
print(c) # [77, 100, 1000, 10000, 3, 4]
c[1] = ['a', 'b', 'c']
print(c) # [77, ['a', 'b', 'c'], 1000, 10000, 3, 4]

del c[1]
print(c) # [77, 1000, 10000, 3, 4]
del c[-1]
print(c) # [77, 1000, 10000, 3]

# 리스트 함수
y = [5, 2, 3, 1, 4]
y.append(6)
print(y) # [5, 2, 3, 1, 4, 6]
y.sort()
print(y) # [1, 2, 3, 4, 5, 6]
y.reverse()
print(y) # [6, 5, 4, 3, 2, 1]
y.insert(2, 7)
print(y) # [6, 5, 7, 4, 3, 2, 1]
y.remove(2)
print(y) # [6, 5, 7, 4, 3, 1]

# 튜플(순서o, 중복o, 수정x, 삭제x)
ta = ()
tb = (1,)
tc = (1, 2, 3, 4)

# 튜플 함수
z = (5, 2, 1, 3, 4)
print(3 in z) # True
print(z.index(5)) # 0
print(z.count(1)) # 1