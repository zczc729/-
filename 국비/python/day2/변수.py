# 변수는 어떻게 만들까?

a = 1
b = "python"
c = [1, 2, 3]

print()
#------------------------------------------------------------------------------------
# 변수란?

a = [1, 2, 3]
print(id(a))

print()
#------------------------------------------------------------------------------------
# 리스트를 복사하고자 할 때

a = [1, 2, 3]
b = a

print(id(a))
print(id(b))

print(a is b)

print()

a[1] = 4
print(a)
print(b)

print()

# 1. [:] 이용하기

a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

print()

# 2. copy 모듈 이용하기

from copy import copy
a = [1, 2, 3]
b = copy(a)

print(b is a)

print()
#------------------------------------------------------------------------------------
# 변수를 만드는 여러 가지 방법

a, b = ('python', 'life')
(a, b) = 'python', 'life'
[a, b] = ['python', 'life']
a = 3
b = 5
a, b = b, a

print(a)
print(b)













