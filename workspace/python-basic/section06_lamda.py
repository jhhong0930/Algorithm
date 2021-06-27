# 파이썬 함수식 및 람다
# 함수 정의 방법
# def 함수명(parameter):
#     code
# 예제1
def hello(world):
    print("Hello ", world)
hello("python")

# 예제2
def hello_return(world):
    val = "Hello " + str(world)
    return val
str = hello_return("Python!!!!!")
print(str)

# 예제3
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3
val1, val2, val3 = func_mul(100)
print(val1, val2, val3)

# 예제4
# *args, *kwargs 가변 파라미터
# *튜블 **딕셔너리
def args_func(*args):  # 매개변수명 자유롭게 변경 가능
    for i, v in enumerate(args):
        print('{}'.format(i), v, end=' ')
args_func('Kim')
args_func('Kim', 'Park')
args_func('Kim', 'Park', 'Lee')

def kwargs_func(**kwargs):  # 매개변수명 자유롭게 변경 가능
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v], end=' ')
kwargs_func(name1='Kim')
kwargs_func(name1='Kim', name2='Park')
kwargs_func(name1='Kim', name2='Park', name3='Lee')

# 전체 혼합
def example(arg_1, arg_2, *args, **kwargs):
    print(arg_1, arg_2, args, kwargs)
example(10, 20, 'park', 'kim', 'lee', age1=33, age2=34, age3=44)

# 예제5
# 중첩함수
def nested_func(num):
    def func_in_func(num):
        print(num)

    print("In func")
    func_in_func(num + 100)

nested_func(1)

#  예제6
def func_mul6(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]
print(func_mul6(5))

# 람다식: 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화
# 일반적 함수 -> 변수 할당
def mul_10(num):
    return num * 10
mul_func = mul_10

print(mul_func(5))
print(mul_func(6))

# 람다 함수 -> 할당
lambda_mul_func = lambda x: x * 10
def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul_func)