num = int(input("숫자 입력 : "))

for i in range(1, num + 1):
    ls = str(i)

    a = ls.count('3')
    b = ls.count('6')
    c = ls.count('9')

    if a + b + c != 0:
        print("짝!" * (a + b + c))
    else:
        print(i)

for i in range(1, 21):
    print(i)

result = 0

for i in range(1, 21):
    result += i

print(result)

result = 0

for i in range(1, 21):
    if i <= 10:
        result += i

print(result)

result = 0

for i in range(1, 21):
    if i <= 10:
        if i % 2 == 0:
            result += i

print(result)











