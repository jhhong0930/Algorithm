# 파일 읽기, 쓰기
# 읽기 모드: r
# 쓰기 모드(덮어 쓰기, 기존 파일 삭제): w
# 추가 모드(이어 쓰기, 파일 생성 또는 추가): a
# 기타 : https://docs.python.org/3.7/library/functions.html#open
# .. : 상대경로
# .  : 절대경로

# 파일 읽기
# 예제1
f = open('../resources/review.txt', 'r')
content = f.read()
print(content)
f.close() # 자원 반납

print("----------------------------------")

# 예제2
# with는 자동으로 자원을 반납한다
with open('../resources/review.txt', 'r') as f:
    c = f.read()
    print(c)

print("----------------------------------")

# 예제3
with open('../resources/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

print("----------------------------------")

# 예제4
with open('../resources/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read() # 내용 없음
    print(">", content)

print("----------------------------------")

# 예제5
with open('../resources/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end='####')
        line = f.readline()

print("----------------------------------")

# 예제6
with open('../resources/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end=' *****')
print()

# 예제7
score = []
with open('../resources/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print('Average: {:6.3}'.format(sum(score) / len(score)))

# 파일 쓰기
# 예제1
with open('../resources/test1.txt', 'w') as f:
    f.write('Hello!\n')

# 예제2
with open('../resources/test1.txt', 'a') as f:
    f.write('Python!\n')

# 예제3
from random import randint

with open('../resources/test2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(0, 50)))
        f.write('\n')

# 예제4
# writelines: 리스트 -> 파일로 저장
with open('../resources/test3.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Lee\n']
    f.writelines(list)

# 예제5
with open('../resources/test4.txt', 'w') as f:
    print('Test Contents!', file=f)
    print('Test Contents!!', file=f)