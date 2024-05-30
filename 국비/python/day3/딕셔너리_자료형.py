# 딕셔너리는 어떻게 만들까?

# {Key1: Value1, Key2: Value2, Key3: Value3, ...}

dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

a = {1: 'hi'}
a = {'a': [1, 2, 3]}

print()
#------------------------------------------------------------------------------------
# 딕셔너리 쌍 추가, 삭제하기

# 딕셔너리 쌍 추가하기

a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1, 2, 3]
print(a)

print()

# 딕셔너리 요소 삭제하기

del a[1]
print(a)

print()

# 딕셔너리를 사용하는 방법

# {"김연아": "피겨스케이팅", "류현진": "야구", "손흥민": "축구", "귀도": "파이썬"}

# 딕셔너리에서 Key를 사용해 Value 얻기

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

print()

a = {1:'a', 2:'b'}
print(a[1])
print(a[2])

a = {'a': 1, 'b': 2}
print(a['a'])
print(a['b'])

print()

dic = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

print()

# 딕셔너리 만들 때 주의할 사항

a = {1:'a', 1:'b'}
print(a)

# >>> a = {[1,2] : 'hi'}
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'

print()
#------------------------------------------------------------------------------------
# 딕셔너리 관련 함수

# Key 리스트 만들기 - keys

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())

print()

# Value 리스트 만들기 - values

print(a.values())

print()

# Key, Value 쌍 얻기 - items

print(a.items())

print()

# Key: Value 쌍 모두 지우기 - clear

a.clear()
print(a)

print()

# Key로 Value 얻기 - get

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))

print()

a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print(a.get('nokey'))
# print(a['nokey’])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'nokey'

print()

# 해당 Key가 딕셔너리 안에 있는지 조사하기 - in

a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print('name' in a)
print('email' in a)











