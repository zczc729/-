"""
ls = [[1, 0, 1], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]

a = 0

for i in ls:
    a += i.count(1)

print(a)
"""

"""



num1 = int(input("시작 번호를 입력하시오. : "))
num2 = int(input("끝 번호를 입력하시오 : "))

ls = []
for i in range(num1, num2+1, 1):
    ls.append([int(a) for a in str(i)])
print(ls)
x = 0
flag = True
while flag:
    sum = 0
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            if x == ls[i][j]:
                sum += 1
    print("{}:{}개".format(x, sum), end = ", ")
    x += 1
    if x == 10:
        flag = False
"""


num1 = int(input("시작 번호를 입력하시오. : "))
num2 = int(input("끝 번호를 입력하시오 : "))

count = {x:0 for x in range(0,10)}
for x in range(num1, num2):
    for i in str(x):
        count[int(i)]+=1
for i in count:
    # print("{}:{}개".format(i, count.get(i)), end = ", ")
    print(f"{i}:{count.get(i)}개", end = ", ")

