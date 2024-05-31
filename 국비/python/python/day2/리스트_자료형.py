# 리스트는 어떻게 만들고 사용할까 ?

odd = [1, 3, 5, 7, 9]

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

print()
#------------------------------------------------------------------------------------
# 리스트의 인덱싱과 슬라이싱

# 리스트의 인덱싱

a = [1, 2, 3]
print(a)

print(a[0])
print(a[0] + a[2])
print(a[-1])

print()

a = [1, 2, 3, ['a', 'b', 'c']]

print(a[0])
print(a[-1])
print(a[3])

print(a[-1][0])
print(a[-1][1])
print(a[-1][2])

print()

# 삼중 리스트에서 인덱싱 하기

a = [1, 2, ['a', 'b', ['Life', 'is']]]

print(a[2][2][0])

print()

# 리스트의 슬라이싱

a = [1, 2, 3, 4, 5]
print(a[0:2])

print()

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]

print(b)
print(c)

# 중척된 리스트에서 슬라이싱 하기

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]

print(a[2:5])
print(a[3][:2])

print()
#------------------------------------------------------------------------------------
# 리스트 연산하기

# 리스트 더하기(+)

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

print()

a = [1, 2, 3]
print(a * 3)

print()

# 리스트 길이 구하기

a = [1, 2, 3]
print(len(a))

print()
#------------------------------------------------------------------------------------
# 리스트의 수정과 삭제

# 리스트의 값 수정하기

a = [1, 2, 3]
a[2] = 4

print(a)

print()

# del 함수를 사용해 리스트 요소 삭제하기

a = [1, 2, 3]
del a[1]
print(a)

print()

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

print()
#------------------------------------------------------------------------------------
# 리스트 관련 함수

# 리스트에 요소 추가하기 - append

a = [1, 2, 3]
a.append(4)
print(a)

a.append([5, 6])
print(a)

print()

# 리스트 정렬 - sort

a = [1, 4, 3, 2]
a.sort()
print(a)

print()

a = ['a', 'c', 'b']
a.sort()
print(a)

print()

# 리스트 뒤집기 - reverse

a = ['a', 'c', 'b']
a.reverse()
print(a)

print()

# 인덱스 반환 - index

a = [1, 2, 3]
print(a.index(3))
print(a.index(1))

print()

# 리스트에 요소 삽입 - insert

a = [1, 2, 3]
a.insert(0, 4)
print(a)

a.insert(3, 5)
print(a)

print()

# 리스트 요소 제거 - remove

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

a.remove(3)
print(a)

print()

# 리스트 요소 끄집어 내기 - pop

a = [1, 2, 3]
a.pop()
print(a)

a = [1, 2, 3]
a.pop(1)
print(a)

print()

# 리스트에 포함된 요소 x의 개수 세기 - count

a = [1, 2, 3, 1]
print(a.count(1))

print()

# 리스트 확장 - extend

a = [1, 2, 3]
a.extend([4, 5])
print(a)

b = [6, 7]
a.extend(b)
print(a)

print()
#------------------------------------------------------------------------------------

# 과제1

"""
price 변수에는 날짜와 종가 정보가 저장돼 있다. 
날자 정보를 제외하고 가격 정보만을 출력하라
"""

price = ['20180728', 100, 130, 140, 150, 160, 170]

print(price[1:])

# 과제 2

"""
인덱스 + 슬라이싱을 사용해서 홀수만 출력하라.
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(nums[::2])











