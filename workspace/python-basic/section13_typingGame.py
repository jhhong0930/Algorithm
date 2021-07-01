import random
import time

import winsound
import sqlite3
import datetime

conn = sqlite3.connect('C:/dev/zero-base/workspace/resources/records.db', isolation_level=None)
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT,  cor_cnt INTEGER, record text, regdate text)"
)

words = []   # 단어 리스트
n = 1        # 게임 시도 횟수
que_cnt = 5  # 문제 개수
cor_cnt = 0  # 정답 개수

with open('../resources/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())
# print(words) # 단거 리스트 확인

input("Ready? Press Enter To Start!")

start = time.time()

while n <= que_cnt:
    random.shuffle(words)
    q = random.choice(words)

    print()

    print('*Question # {}'.format(n))
    print(q)    # 문제 출력

    x = input() # 타이핑 입력

    print()

    if str(q).strip() == str(x).strip(): # 입력 확인(공백 제거)
        print("Correct!")
        # 정답 소리 재생
        # winsound.PlaySound('../resources/good.wav', winsound.SND_FILENAME)
        cor_cnt += 1
    else:
        print("Wrong!")
        # 오답 소리 재생
        # winsound.PlaySound('../resources/bad.wav', winsound.SND_FILENAME)

    n += 1

end = time.time() # end time
et = end - start  # 총 게임시간
et = format(et, '.3f')

print('-------------------')

if cor_cnt == que_cnt:
    print('Excellent!')
elif cor_cnt >= que_cnt // 2:
    print('Not bad!')
else:
    print('You need more practice, never give it up!')

# 기록 DB 삽입
cursor.execute(
    "INSERT INTO records('cor_cnt', 'record', 'regdate') VALUES (?, ?, ?)",
    (
        cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    )
)

# 접속 해제
conn.close()

# 수행 시간 출력
print('playtime: ', et, 'correct: {}'.format(cor_cnt))

# 시작 지점
if __name__ == '__main__':
    pass