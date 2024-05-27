"Life is too short, You need Python"
"a"
"123"

#------------------------------------------------------------------------------------

"Hello World"
'Python is fun'
"""Life is too short, You need python"""
'''Life is too short, You need python'''

#------------------------------------------------------------------------------------
# 문자열에 작은 따옴표 포함하기

food = "Python's favorite food is perl"
print(food)

# food
# "Python's favorite food is perl"
# print(food)

print()
#------------------------------------------------------------------------------------
# 문자열에 큰 따옴표 포함하기

say = '"Python is very easy." he says.'
print(say)

print()
#------------------------------------------------------------------------------------
# 역슬래시를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함하기

food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

print(food)
print(say)

print()
#------------------------------------------------------------------------------------
# 여러 줄인 문자열을 변수에 대입하고 싶을 때

# 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기

multiline = "Life is too short\nYou need python"
print(multiline)

# 연속된 작은따옴표 3개 또는 큰따옴표 3개 사용하기

multiline = '''
Life is too short
You need python
'''

print(multiline)

print()
#------------------------------------------------------------------------------------
# 문자열 연산하기

# 문자열 더해서 연결하기

head = "Python"
tail = " is fun!"
print(head + tail)

# 문자열 곱하기

a = "python"
print(a * 2)

# 문자열 곱하기를 응용하기

print("=" * 50)
print("My Program")
print("=" * 50)

print()
#------------------------------------------------------------------------------------
# 문자열 길이 구하기

a = "Life is too short"
print(len(a))

print()
#------------------------------------------------------------------------------------
# 문자열 인덱싱과 슬라이싱

# 문자열 인덱싱

a = "Life is too short, You need Python"
print(a[3])
print(a[0])
print(a[12])
print(a[-1])
print(a[-0])
print(a[-2])
print(a[-5])

print()
# 문자열 슬라이싱

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:4])
print(a[0:3])
print(a[0:5])
print(a[0:2])
print(a[5:7])
print(a[12:17])
print(a[19:])
print(a[:17])
print(a[:])
print(a[19:-7])

print()
# 슬라이싱으로 문자열 나누기

a = "20230331Rainy"
date = a[:8]
weather = a[8:]

print(date)
print(weather)

year = a[:4]
month = a[4:6]
day = a[6:8]
weather = a[8:]

print(year)
print(month)
print(day)
print(weather)

print()
# Pithon 문자열을 Python으로 바꾸려면?

# a = "pithon"
# a[1] = 'y'
# print(a)

a = "Pithon"

print(a[:1])
print(a[2:])

print(a[:1] + 'y' + a[2:])

print()
#------------------------------------------------------------------------------------
# 문자열 포매팅이란?


print()
#------------------------------------------------------------------------------------
# 문자열 관련 함수들

# 문자열 개수 세기 - count

a = "hobby"
print(a.count('b'))

print()
# 위치 알려 주기 1 - find

a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))

print()
# 위치 알려 주기 1 - index

a = "Life is too short"
print(a.index('t'))

# print(a.index('k'))

print()
# 문자열 삽입 - join

print(",".join('abcd'))
print(",".join(['a', 'b', 'c', 'd']))

print()

# 소문자를 대문자로 바꾸기 - upper

a = "hi"
print(a.upper())

print()
# 대문자를 소문자로 바꾸기 - lower

a = "HI"
print(a.lower())

print()
# 왼쪽 공백 지우기 - lstrip

a = " hi "
print(a.lstrip())

# 오른쪽 공백 지우기 - rstrip

a = " hi "
print(a.rstrip())

# 양쪽 공백 지우기 - strip

a = " hi "
print(a.strip())

print()
# 문자열 바꾸기 - replace

a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 문자열 나누기 - split

a = "Life is too short"
print(a.split())

b = "a:b:c:d"
print(b.split(':'))






