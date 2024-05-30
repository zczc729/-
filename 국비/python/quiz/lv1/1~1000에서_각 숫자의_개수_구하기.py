"""
예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자

10 = 1, 0
11 = 1, 1
12 = 1, 2
13 = 1, 3
14 = 1, 4
15 = 1, 5

그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개
"""

start_num = int(input("시작 숫자 입력 : "))
end_num = int(input("끝 숫자 입력 : "))
numList = []

for i in range(start_num, end_num + 1):
    for j in str(i):
        numList += j.split()

dic_num = {}

for i in range(0, 10):
    dic_num[i] = numList.count(str(i))
    if dic_num[i] != 0:
        print(f"{i} : {dic_num[i]} 개")