# 1
import csv

with open('a.csv', 'r') as f:
    content = csv.reader(f)

    for c in content:
        l = sum(list(map(int, c)))
    print(l)

# 2
class Median:
    def __init__(self):
        self.a = list()

    def get_item(self, item):
        self.item = item
        self.a.append(self.item)

    def clear(self):
        self.a = list()

    def show_result(self):
        self.a.sort()
        centerIndex = len(self.a) // 2
        if len(self.a) % 2 == 1:
            print(self.a[centerIndex])
        else: print(((self.a[centerIndex - 1] + self.a[centerIndex]) / 2))

median = Median()
for x in range(10):
    median.get_item(x)
median.show_result()

median.clear()
for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
    median.get_item(x)
median.show_result()

# 3
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' cannot speak.')

    def move(self):
        print(self.name + ' cannot move.')

class Dog(Animal):
    pass

class Retriever(Dog):
    pass

dog = Dog('Nancy')
dog.speak()
dog.move()

super_dog = Retriever('Michael')
super_dog.speak()
super_dog.move()

median.clear()
for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
    median.get_item(x)
median.show_result()

# 4
class Foo:
    bar = 'A'
    def __init__(self, bar = 'B'):
        self.bar = bar

    class Bar:
        bar = 'C'
        def __init__(self, bar = 'D'):
            self.bar = bar

print(Foo.bar)
print(Foo().bar)
print(Foo.Bar.bar)
print(Foo.Bar().bar)