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