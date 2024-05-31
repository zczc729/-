n = int(input("숫자 입력 : "))
result = 1
ls = []
ans = [0]

for i in range(n - 1):
    ls.append(result)
    result += ls[i - 1]

for i in ls:
    if i < n:
        ans.append(i)

print(ans)


