# if 문의 기본 구조

"""
if 조건문:
    수행할_문장1
    수행할_문장2
    ...
else:
    수행할_문장A
    수행할_문장B
    ...
"""

# 들여쓰기 방법 알아보기

"""
if 조건문:
    수행할_문장1
    수행할_문장2
    수행할_문장3

if 조건문:
    수행할_문장1
수행할_문장2
    수행할_문장3

money = True
if money:
    print("택시를")
print("타고")
    print("가라")
"""

print()
#------------------------------------------------------------------------------------
# 조건문이란 무엇인가?

money = True
if money:
    pass

# 비교 연산자

x = 3
y = 2
print(x > y)
print(x < y)
print(x == y)
print(x != y)

print()

# 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 가고, 그렇지 않으면 걸어가라.

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

print()

# and, or, not

# 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않으면 걸어가라.

money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

print()

# in, not in

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

print('a' in ('a', 'b', 'c'))
print('j' not in 'python')

print()

# 만약 주머니에 돈이 있으면 택시를 타고 가고, 없으면 걸어가라.

pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

print()
#------------------------------------------------------------------------------------
# 다양한 조건을 판단하는 elif

# 주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라.

# pocket = ['paper', 'cellphone']
# card = True

# if 'money' in pocket:
#     print("택시를 타고가라")
# else:
#     if card:
#         print("택시를 타고가라")
#     else:
#         print("걸어가라")

pocket = ['paper', 'cellphone']
card = True

if 'money' in pocket:
    print("택시를 타고가라")
elif card: 
    print("택시를 타고가라")
else:
    print("걸어가라")

"""
if 조건문:
    수행할_문장1 
    수행할_문장2
    ...
elif 조건문:
    수행할_문장1
    수행할_문장2
    ...
elif 조건문:
    수행할_문장1
    수행할_문장2
    ...
...
else:
   수행할_문장1
   수행할_문장2
   ... 
"""

print()
#------------------------------------------------------------------------------------
# 조건부 표현식

score = 0

if score >= 60:
    message = "success"
else:
    message = "failure"















