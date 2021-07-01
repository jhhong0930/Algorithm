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
# c.execute("insert into users values(1, 'Kwon', 'Kwon@gmail.com', '010-1234-5678', 'Kwon.com', ?)", (nowDatetime,))
# c.execute("insert into users values(2, 'Joe', 'Joe@gmail.com', '010-8765-4321', 'Joe.com', ?)", (nowDatetime,))
# c.execute("insert into users values(6, 'Test', 'Test@gmail.com', '010-0000-0000', 'Test.com', ?)", (nowDatetime,))

# 여러행 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', nowDatetime)
)
# c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)

# 테이블 데이터 삭제
# print("users db deleted : ", conn.execute("delete from users").rowcount, "rows")

# 커밋 : isolation_level=None 일 경우 자동 반영(Auto Commit)
# conn.commit()

# 롤백
# conn.rollback()

# 접속 해제
# conn.close()

# 전체 데이터 조회
c.execute("select * from users")

# 한 행 조회
# print(c.fetchone())

# 지정 개수 행 조회
# print(c.fetchmany(size=3))

# 전체 행 조회
# print(c.fetchall())

# 순회1
# rows = c.fetchall()
# for row in rows:
#     print(row)

# 순회2
# for row in c.fetchall():
#     print(row)

# 순회3
# for row in c.execute('select * from users order by id desc'):
#     print(row)

# 조건절1
param1 = (3,)
c.execute('select * from users where id = ?', param1)
print(c.fetchone())
print(c.fetchall()) # 한 행 조회 후 커서가 넘어갔으므로 데이터 조회 안됨

# 조건절2
param2 = 4
c.execute('select * from users where id = "%s"' % param2)
print(c.fetchone())
print(c.fetchall())

# 조건절3
c.execute('select * from users where id = :Id', {"Id": 5}) # 딕셔너리 이용
print(c.fetchone())
print(c.fetchall())

# 조건절4
param4 = (1, 2)
c.execute('select * from users where id in (?, ?)', param4)
print(c.fetchall())

# 조건절5
c.execute("SELECT * FROM users WHERE id In('%d','%d')" % (1, 2))
print('param5', c.fetchall())

# 조건절6
c.execute("SELECT * FROM users WHERE id= :id1 OR id= :id2", {"id1": 1, "id2": 2})
print('param6', c.fetchall())

# Dump 출력
with conn:
    with open('C:/dev/zero-base/workspace/resources/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')
# f.close(), conn.close() 실행됨 (With 때문에)

# 데이터 수정1
# c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman', 6))

# 데이터 수정2
# c.execute("UPDATE users SET username = :name WHERE id = :id", {"name": 'niceman', 'id': 6})

# 데이터 수정3
# c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('badboy', 6))
conn.commit()

for user in c.execute('select * from users'):
    print(user)

# 데이터 삭제1
c.execute("DELETE FROM users WHERE id = ?", (7,))

# 데이터 삭제2
c.execute("DELETE FROM users WHERE id = :id", {'id': 8})

# 데이터 삭제3
c.execute("DELETE FROM users WHERE id = '%s'" % 9)

# 테이블 전체 데이터 삭제
# print("users db deleted : ", conn.execute("delete from users").rowcount, "rows")