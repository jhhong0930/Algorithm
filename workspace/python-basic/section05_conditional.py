# 참, 거짓 종류(True, False)
# 참: "내용", [내용], (내용), {내용}, 1, True
# 거짓: "", [], (), {}, 0, False
city = ""
if city:          # FALSE
    print("TRUE")
else:
    print("FALSE")

# 논리 연산자
# and, or, not
a = 100
b = 60
c = 15
print(a > b and b > c) # True
print(a > b or c > b)  # True
print(not a > b)       # Flase

# 다중 조건문 if ~ elif ~ else
num = 90
if(num >= 90):
    print("A")
elif(num >= 80):
    print("B")
elif(num >= 70):
    print("C")
else:
    print("D")

