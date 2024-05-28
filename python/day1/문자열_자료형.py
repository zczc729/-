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

# 1. 숫자 바로 대입

print("I eat %d apples." % 3)

print()

# 2. 문자열 바로 대입

print("I eat %s apples." % "five")

print()

# 3. 숫자 값을 나타내는 변수로 대입

number = 3
print("I eat %d apples." % number)

print()

# 4. 2개 이상의 값 넣기

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))

print()
#------------------------------------------------------------------------------------

# 포맷 코드와 숫자 함께 사용하기

# 1. 정렬과 공백

print("%10s" % "hi")
print("%-10sjane." % 'hi')

print()

# 2. 소수점 표현하기

print("%0.4f" % 3.42134234)
print("%10.4f" % 3.42134234)

print()
#------------------------------------------------------------------------------------

# format 함수를 사용한 포매팅

# 숫자 바로 대입하기

print("I eat {0} apples".format(3))

print()

# 문자열 바로 대입하기

print("I eat {0} apples".format("five"))

print()

# 숫자 값을 가진 변수로 대입하기

number = 3
print("I eat {0} apples".format(number))

print()

# 2개 이상의 값 넣기

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

print()

# 이름으로 넣기

print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))

print()

# 인덱스와 이름을 혼용해서 넣기

print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))

print()

# 왼쪽 정렬

print("{0:<10}".format("hi"))

print()

# 오른쪽 정렬

print("{0:>10}".format("hi"))

print()

# 가운데 정렬

print("{0:^10}".format("hi"))

print()

# 공백 채우기

print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

print()

# 소수점 표현하기

y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

print()

# { 또는 } 문자 표현하기

print("{{ and }}".format())

print()
#------------------------------------------------------------------------------------

# f 문자열 포매팅

name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

print()

# 표현식

age = 30
print(f'나는 내년이면 {age + 1}살이 된다.')

print()

# 딕셔너리

d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

print()

# 정렬

print(f'{"hi":<10}')  # 왼쪽 정렬
print(f'{"hi":>10}')  # 오른쪽 정렬
print(f'{"hi":^10}')  # 가운데 정렬

print()

# 공백 채우기

print(f'{"hi":=^10}')  # 가운데 정렬하고 '=' 문자로 공백 채우기
print(f'{"hi":!<10}')  # 왼쪽 정렬하고 '!' 문자로 공백 채우기

print()

#  소수점

y = 3.42134234
print(f'{y:0.4f}')  # 소수점 4자리까지만 표현
print(f'{y:10.4f}')  # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤

print(f'{{ and }}')

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

print()
#------------------------------------------------------------------------------------

# 과제 1

"""
"Life is too short" 문자열을 모두 대문자로 바꾸고, 다시 소문자로 바꾸고, 
공백을()을 컴마(,)로 바꾸고, 단어 단위로 문자열을 나누어라
단, 코딩은 한 줄로 하라
"""

a = "Life is too short"

print(a.upper().lower().replace(" ", ",").split(","))

# 과제 2

"""
가로가 4이고 세로가 2인 삼각형의 넓이 출력(문자열 대체로 출력)
"""

width = 4
height = 2
area = 4

print(f"가로가 {width}이고 세로가 {height}인 삼각형의 넓이는 {width} 입니다.")

# 과제3

"""
월급이 100원이다. 세금 10%를 제외한 연봉 출력
"""

month = 100

print(f"월급이 {month}이고 세금 10%를 제외한 연봉은 {(month - 10) * 12} 원이다.")

# 과제4

"""
100초를 1분 40초로 출력. (문자열 대체로 출력)
"""

print(f"100초는 {1}분 {40}초 입니다.")
print("100초는 %d분 %d초 입니다." %(1, 40))
print("100초는 {}분 {}초 입니다.".format(1, 40))

# 과제5

"""
800원에서 500원을 제외한 100원의 개수 출력(문자열 대체로 출력)
"""

print("100원의 개수는 %d 개 입니다." %3)
print("100원의 개수는 {} 개 입니다.".format(3))
print(f"100원의 개수는 {3} 개 입니다.")