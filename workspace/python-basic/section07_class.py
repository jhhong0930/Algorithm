# 네임스페이스: 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수: 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수: 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 예제1
class UserInfo:
    # pass
    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("Name: ", self.name)

user1 = UserInfo("Joe")
user1.user_info_p()
user2 = UserInfo("Kwon")
user2.user_info_p()

print(user1.__dict__)
print(user2.__dict__)

# 예제2
# self의 이해
class SelfTest:
    def function1():
        print('function1 called')
    def function2(self):
        print(id(self))
        print('function2 called')
self_test = SelfTest()
# self_test.function1()
SelfTest.function1() # self가 없으면 클래스에서 직접 호출
self_test.function2()

print(id(self_test))

# 예제3
# 클래스 변수, 인스턴스 변수
class WareHouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Joe')
user2 = WareHouse('Kwon')
print(user1.__dict__)
print(user2.__dict__)
print(WareHouse.__dict__)

print(user1.stock_num)
print(user2.stock_num)