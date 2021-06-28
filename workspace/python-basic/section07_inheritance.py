# 상속, 다중상속

# 예제1
class Car:
    """Parent Class"""
    def __init__(self, type, color):
        self.type = type
        self.color = color
    def show(self):
        return 'Car Class "Show Method"'

class Bmw(Car):
    """Sub Class"""
    def __init__(self, car_name, type, color):
        super().__init__(type, color)
        self.car_name = car_name
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

class Benz(Car):
    """Sub Class"""
    def __init__(self, car_name, type, color):
        super().__init__(type, color)
        self.car_name = car_name
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    def show(self):
        print(super().show())
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)

# 일반 사용
model1 = Bmw('520d', 'sedan', 'red')
print(model1.type) # Super
print(model1.color) # Super
print(model1.car_name) # Sub
print(model1.show()) # Super
print(model1.show_model()) # Sub
print(model1.__dict__)

# Method Overriding
model2 = Benz('S550', 'sedan', 'black')
print(model2.show())

# Parent Method Call
model3 = Benz('S580', 'sedan', 'white')
print(model3.show())

# Inheritance Info
print(Bmw.mro())
print(Benz.mro())

# 예제2
# 다중 상속
class X():
    pass
class Y():
    pass
class Z():
    pass

class A(X, Y):
    pass
class B(Y, Z):
    pass
class M(B, A, Z):
    pass

print(M.mro())
print(A.mro())