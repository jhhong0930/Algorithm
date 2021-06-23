# 데이터 타입 확인
print(type(1))    # <class 'int'>
print(type('a'))  # <class 'str'>
print(type(3.14)) # <class 'float'>

# 형변환
print(int(True))  # 1
print(complex(3)) # (3+0j)

# 수치 연산 함수
print(abs(-7)) # 7
a, b = divmod(100, 8)
print(a, b) # 12 4 a(몫), b(나머지)

import math
print(math.ceil(5.1)) # 6
print(math.floor(3.14)) # 3