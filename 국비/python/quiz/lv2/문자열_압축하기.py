"""
문자열을 입력받아서, 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시하여 문자열을 압축하기.

입력 예시: aaabbcccccca

출력 예시: a4b2c6
"""

s = input("입력 : ")
s1 = sorted(set(s))
num_ls = {}
num_cnt = 0

for i in s1:
    num_ls[i] = 0

for i in s:
    for j in s1:
        if j == i:
            num_ls[j] += 1

print(num_ls)



