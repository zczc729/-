from random import randint

numList = []

ranNum = randint(1, 20)
numList.append(ranNum)

for i in range(2):
    while True:
        ranNum = randint(1, 20)
        if numList[i] != ranNum:
            numList.append(ranNum)
            break

print(numList)

chance = int(input("기회 입력 : "))
anw_count = chance

for i in range(chance):
    user_in = input("숫자 입력 : ")
    ls = user_in.split()
    anw_list = []
    for a in ls:
        anw_list.append(int(a))


    anw_in_cnt = 0
    for j in anw_list:
        if j in numList:
            anw_in_cnt += 1
    anw_count -= 1
            
    
    if anw_in_cnt == 3:
        print("축하드립니다! 정답입니다!")
        break
    else:
        print(f"입력하신 숫자들 중 정답은 {anw_in_cnt}개 입니다.")
        print(f"남은 기회는 {anw_count}번 입니다.")

    

    