"""
1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오. (단 점들의 배열은 모두 정렬되어있다고 가정한다.)

예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.
"""

from random import randint

s = []

for i in range(7):
    s.append(randint(1, 20))

s.sort()

print(s)

dif = 0
dif_num = 0
min = []

for i in range(1, len(s)):
    min.append(s[i] - s[i - 1])

print(min)

for i in range(len(min)):
    if i == 0:
        dif = min[i]
    else:
        if dif > min[i]:
            dif = min[i]
            dif_num = i

print(s[dif_num], s[dif_num + 1])

