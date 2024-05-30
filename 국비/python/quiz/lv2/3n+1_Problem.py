"""
어떤 정수 n에서 시작해, n이 짝수면 2로 나누고, 홀수면 3을 곱한 다음 1을 더한다. 
이렇게 해서 새로 만들어진 숫자를 n으로 놓고, n=1 이 될때까지 같은 작업을 계속 반복한다. 
예를 들어, n=22이면 다음과 같은 수열이 만들어진다.

22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
n이라는 값이 입력되었을때 1이 나올때까지 만들어진 수의 개수(1을 포함)를 n의 사이클 길이라고 한다. 
\위에 있는 수열을 예로 들면 22의 사이클 길이는 16이다. 
i와 j라는 두개의 수가 주어졌을때, i와 j사이의 모든 수(i, j포함)에 대해 최대 사이클 길이를 구하라.

입력 예

1    10
100  200
201  210
900  1000
출력 예

1    10    20
100  200   125
201  210   89
900  1000  174
"""

i = int(input("첫 번 째 수 입력 : "))
j = int(input("두 번 째 수 입력 : "))
num = 0
num_dic = {}
results = []


def problem(n, results = None):
    if results is None:
        results = []
    if n == 1:
        return results
    elif n % 2 == 0:
        next_n = int(n / 2)
    elif n % 2 != 0:
        next_n = 3 * n + 1
    results.append(next_n)
    return problem(next_n, results)

for a in range(i, j):
    result = problem(a)
    results.append(result)
    for i in range(len(results)):
        if len(results[i]) > num:
            num_dic[a] = len(results[i])


k = [k for k,v in num_dic.items() if max(num_dic.values()) == v]

for i in k:
    print(f"{i} : {num_dic.get(i)}개")
