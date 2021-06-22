# 몸풀기 코딩

import sys

# 파이썬의 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('Joe')

# 변수 선언
name = "Joe"

# 조건문
if name == "Joe":
    print("Hi", name)

# 반복문
# for i in range(1, 10):
#     for j in range(1, 10):
#         print("%d X %d = " % (i, j), i * j)

# 함수 선언
def greeting():
    print('hello!')
greeting()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))