# while
v1 = 1
while v1 < 11:
    print("v1 is ", v1) # 1 ~ 10
    v1 += 1

# range(시작값, 끝값, 증감값)
for v2 in range(10): # for(int i=0; i<10; i++)
    print("v2 is ", v2) # 0 ~ 9

for v3 in range(1, 11): # for(int i=1; i<11; i++)
    print("v3 is ", v3) # 1 ~ 10

# 1 ~ 100의 합
sum1 = 0
cnt1 = 1
while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1
print("1 ~ 100의 합: ", sum1) # 5050
print(sum(range(1, 101)))    # 5050
print(sum(range(1, 101, 2))) # 2500

# 시퀸스 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip
names = ["Kim", "Park", "Gwon", "Hong", "Yoo"]
for name in names:
    print("You are: ", name)

word = "dreams"
for s in word:
    print("Word: ", s)

info = {
    "name": "Gwon",
    "age": 22,
    "city": "Chuncheon"
}
for key in info: # 기본값 키
    print("info: ", key)
for key in info.values(): # 값
    print("info: ", key)
for key in info.items(): # 키, 값
    print("info: ", key)

name = "JaeHwan"
for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2]
for num in numbers:
    if num == 7:
        print("fount: 7")
        break
    else:
        print("not found")
else:
    print("not found 7 in numbers")

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]
for v in lt:
    if type(v) is float:
        continue
    print("타입: ", type(v))