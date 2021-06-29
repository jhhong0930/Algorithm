# 파이썬 예외처리의 이해
# 예외 처리 기본
# try               에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1:    여러 개 가능(에러 처리)
# except 에러명2:
# else:             try 블록의 에러가 없을 경우 실행
# finally:          항상 실행

# 예제1
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'  # 'Cho' 예외 발생
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('ok! else!')

print()

# 예제2
try:
    z = 'Kim'  # 'Cho' 예외 발생
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except:  # 모든 에러를 처리(Exception)
    print('Not found it! - Occurred ValueError!')
else:
    print('ok! else!')

print()

# 예제3
try:
    z = 'Kim'  # 'Cho' 예외 발생
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except Exception as e:
    print(e)  # 에러 내용 출력
    # pass # 임시로 에러 해결 시 예외 처리
else:
    print('ok! else!')
finally:
    print('ok! finally!')  # 무조건 수행 됨

print()

# 예제4
# 예외처리는 하지 않지만, 무조건 수행 되는 코딩 패턴
try:
    print('try')
finally:
    print('finally')

print()

# 예제5
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생
try:
    a = 'Park'
    if a == 'Kim':
        print('Ok! pass')
    else:
        raise ValueError
except ValueError:
    print('Raise! Occurred ValueError')
except Exception:
    print('Occurred Exception')
else:
    print('ok! else!')