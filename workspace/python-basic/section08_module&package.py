# 파이썬 모듈과 패키지
# 패키지 예제
# 상대경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1(클래스)
from package.fibonacci import Fibonacci

Fibonacci.fib(300)
print("ex1: ", Fibonacci.fib2(400))
print("ex1: ", Fibonacci().title)

# 사용2(클래스) 메모리를 많이 먹어서 비권장
from package.fibonacci import *

Fibonacci.fib(500)
print("ex1: ", Fibonacci.fib2(600))
print("ex1: ", Fibonacci().title)

# 사용3(클래스) Alias
from package.fibonacci import Fibonacci as fb

fb.fib(700)
print("ex1: ", fb.fib2(800))
print("ex1: ", fb().title)

# 사용4(함수)
import package.cacluations as c

print("ex4: ", c.add(10, 100))
print("ex4: ", c.mul(10, 100))

# 사용5(함수) 필요한 자원만 가져오는걸 권장
from package.cacluations import div as d

print("ex5: ", int(d(100 , 10)))

# 사용6
import package.prints as p
# import builtins 기본으로 불러온다
p.prt1()
p.prt2()