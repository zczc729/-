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
    








