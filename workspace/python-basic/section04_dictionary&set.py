# 딕셔너리(순서x 중복x 수정o 삭제o)
# Key, Value
a = {'name': 'kwh', 'birth': '000112'}
b = {0: 'hello', 1: 'python'}
c = {'arr': [1, 2, 3, 4, 5]}

# 출력
print(a['name']) # kwh 해당 키값이 없으면 KeyError
print(a.get('name')) # kwh 해당 키값이 없으면 None 반환
print(c['arr'][1:3]) # [2, 3]

# 딕셔너리 추가
a['address'] = 'Seoul'
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3)
print(a) # {'name': 'kwh', 'birth': '000112', 'address': 'Seoul', 'rank': [1, 3, 4], 'rank2': (1, 2, 3)}

# keys, values, items
print(a.keys()) # dict_keys(['name', 'birth', 'address', 'rank', 'rank2'])
print(list(a.keys())) # ['name', 'birth', 'address', 'rank', 'rank2']

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))

print(2 in b) # False
print('name2' not in a) # True

# 집합(순서x, 중복x)
d = set()
e = set([1, 2, 3, 4])
f = set([1, 4, 5, 6, 6])

print(type(d)) # <class 'set'>
print(f) # {1, 4, 5, 6}

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2)) # {4, 5, 6}
print(s1 & s2) # == intersection

print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1 | s2) # == union

print(s1.difference(s2)) # {1, 2, 3}
print(s1 - s2) # == difference

# 추가, 제거
s3 = set([7, 8, 10, 15])
s3.add(18)
s3.remove(15)
print(s3) # {7, 8, 10, 18}