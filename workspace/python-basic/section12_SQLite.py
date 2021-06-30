# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입
import sqlite3
import datetime

# 버전 확인
print(sqlite3.version)
print(sqlite3.sqlite_version)

# 삽입 날짜 생성
now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

# DB 생성 & Auto Commit
conn = sqlite3.connect('C:/dev/zero-base/workspace/resources/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print(type(c))

# 테이블 생성(Data Type: TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("create table if not exists users(\
           id INTEGER PRIMARY KEY, \
           username text, \
           email text, \
           phone text, \
           website text, \
           regdate text)")

# 데이터 삽입
# c.execute("insert into users values(1, 'Kwon', 'Kwon@gmail.com', '010-1234-5678', 'Kwon.com', nowDatetime)")
# c.execute("insert into users values(2, 'Joe', 'Joe@gmail.com', '010-8765-4321', 'Joe.com', nowDatetime)")

# 여러행 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', nowDatetime)
)
c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)

# 테이블 데이터 삭제
# print("users db deleted : ", conn.execute("delete from users").rowcount, "rows")

# 커밋 : isolation_level=None 일 경우 자동 반영(Auto Commit)
conn.commit()

# 롤백
# conn.rollback()

# 접속 해제
conn.close()