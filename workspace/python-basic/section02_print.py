# print 구문의 이해
# 기본출력
print('hello world')
print("hello world")
print('''hello world''')
print("""hello world""")

# Separator 옵션 사용
print('T', 'E', 'S', 'T', sep='')  # TEST
print('2019', '02', '19', sep='-') # 2019-02-19
print('kwh', 'google.com', sep='@') # kwh@google.com

# end 옵션 사용
print('Welcome To', end=' ') # Welcome To The Jungle 줄바꿈 X
print('The Jungle', end=' ')
print()

# format 사용 [], {}, ()
print('{} and {}'.format('you', 'me')) # you and me
print('{0} and {1} and {0}'.format('you', 'me')) # you and me and you
print('{a} != {b}'.format(a='3', b='5'))
# %s: 문자 %d: 정수 %f: 실수
print("%s's favortie number is %d" % ('Joe', 3)) # Joe's favortie number is 3

print("Test1: %5d, Price: %4.2f" % (776, 6534.123)) # Test1:   776, Price: 6534.12
print("Test1: {0: 5d}, price: {1:4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, price: {b:4.2f}".format(a=776, b=6534.123))