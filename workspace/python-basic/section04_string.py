# Raw String
rs1 = r'C:\Programs\Test\Bin'
print(rs1) # C:\Programs\Test\Bin

# 멀티 라인
multi = \
"""
abc
def
123
"""
print(multi)

# 문자열 연산
st1 = "apple"
print('a' in st1) # 문자열 'a'가 st1에 포함되어 있는지? -> True
print('b' not in st1) # True

# 문자열 함수
a = 'niceman'
b = 'orange'

# 소문자 인지 판단
print(a.islower()) # True
# 'e'로 끝나는지 판단
print(b.endswith('e')) # True
# 첫글자를 대문자로 변환
print(a.capitalize()) # Niceman
# 특정 문자열 변경
print(a.replace('nice', 'good')) # goodman
# 리스트 형태로 반환
print(list(b)) # ['o', 'r', 'a', 'n', 'g', 'e']
print(list(reversed(b))) # ['e', 'g', 'n', 'a', 'r', 'o']

# 슬라이싱
a = 'niceman'
print(a[0:3])   # nic
print(a[:])     # niceman
print(a[0:4:2]) # nc
print(a[1:-2])  # icem
print(a[::-1])  # namecin