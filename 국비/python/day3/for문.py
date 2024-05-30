# for 문의 기본 구조

"""
for 변수 in 리스트(또는 튜플, 문자열):
    수행할_문장1
    수행할_문장2
    ...
"""

print()
#------------------------------------------------------------------------------------
# 예제를 통해 for 문 이해하기

# 1. 전형적인 for 문
test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print(i)

print()

# 2. 다양한 for 문의 사용

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

print()

# 3. for 문의 응용

# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다. 합격인지, 불합격인지 결과를 보여 주시오.

marks = [90, 25, 67, 45, 80]   # 학생들의 시험 점수 리스트

number = 0   # 학생에게 붙여 줄 번호
for mark in marks:   # 90, 25, 67, 45, 80을 순서대로 mark에 대입
    number = number +1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)

print()
#------------------------------------------------------------------------------------
# for 문과 continue 문

marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)

print()
#------------------------------------------------------------------------------------
# for 문과 함께 자주 사용하는 range 함수

a = range(10)
print(a)

print()

a = range(1, 11)
print(a)

print()

# range 함수의 예시 살펴보기

add = 0 
for i in range(1, 11): 
    add = add + i 
print(add)

print()

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: 
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

print()

# for와 range를 이용한 구구단

for i in range(2,10):        # 1번 for문
    for j in range(1, 10):   # 2번 for문
        print(i*j, end=" ") 
    print('') 

print()
#------------------------------------------------------------------------------------
# 리스트 컴프리헨션 사용하기

a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)

print()

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)








