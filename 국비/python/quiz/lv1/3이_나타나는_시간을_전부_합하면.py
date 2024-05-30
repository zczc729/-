"""
디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초(second) 일까요?

디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됩니다.

00:00 (60초간 표시됨)
00:01 
00:02 
...
23:59
"""
ls = {}

# for i in range(25):
#     ls[str(i)] = []


# for i in range(25):
#     if str(i) in "3":
#         # ls = {str(i) : list(str(j))}
#         ls[str(i)].append(str(j))
#     for j in range(0, 60):
#         for k in str(j):
#             if k in '3':
#                 # ls = {str(i) + str(j)}
#                 ls[str(i)].append(str(j))




# print(ls)

result = 0

for i in ls:
    result += int(i) * 60 * 60
    for j in ls[i]:
        result += int(j) * 60

print(result)

# print(ls)



sum = 0

for h in range(24):
    for m in range(60):
        if '3' in str(h) or '3' in str(m):
            sum += 60

print(sum)
