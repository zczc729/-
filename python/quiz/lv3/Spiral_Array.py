"""
문제는 다음과 같다:

6 6

0   1   2   3   4   5
19  20  21  22  23   6
18  31  32  33  24   7
17  30  35  34  25   8
16  29  28  27  26   9
15  14  13  12  11  10

00  01  02  03  04  05
10  11  12  13  14  15
20  21  22  23  24  25
30  31  32  33  34  35
40  41  42  43  44  45
50  51  52  53  54  55


0   1   2   3   4   5   6
23  24  25  26  27  28  7
22  39  40  41  42  29  8
21  38  47  48  43  30  9
20  37  46  45  44  31  10
19  36  35  34  33  32  11
18  17  16  15  14  13  12

00 01 02 03 04 05 06
10 11 12 13 14 15 16
20 21 22 23 24 25 26
30 31 32 33 34 35 36
40 41 42 43 44 45 46
50 51 52 53 54 55 56
60 61 62 63 64 65 66


위처럼 6 6이라는 입력을 주면 6 X 6 매트릭스에 나선형 회전을 한 값을 출력해야 한다.
"""

# 마지막 줄은 무조건 i + j


"""
0   1   2   3   4   5
19  20  21  22  23   6
18  31  32  33  24   7
17  30  35  34  25   8
16  29  28  27  26   9
15  14  13  12  11  10

00  01  02  03  04  05
10  11  12  13  14  15
20  21  22  23  24  25
30  31  32  33  34  35
40  41  42  43  44  45
50  51  52  53  54  55
"""


def generate_spiral_matrix(n):
    # n x n 매트릭스를 0으로 초기화
    matrix = [[0] * n for _ in range(n)]

    # 초기값 설정
    num = 1
    x, y = 0, 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽, 아래, 왼쪽, 위
    dir_index = 0  # 초기 방향은 오른쪽

    for _ in range(n * n):
        matrix[x][y] = str(num - 1)
        num += 1

        # 다음 위치 계산
        next_x = x + directions[dir_index][0]
        next_y = y + directions[dir_index][1]

        # 다음 위치가 매트릭스 범위를 벗어나거나 이미 숫자가 채워져 있는 경우 방향 전환
        if (0 <= next_x < n and 0 <= next_y < n and matrix[next_x][next_y] == 0):
            x, y = next_x, next_y
        else:
            dir_index = (dir_index + 1) % 4  # 방향 전환
            x += directions[dir_index][0]
            y += directions[dir_index][1]

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{num:2}" for num in row))


# 6x6 매트릭스를 생성하고 출력
n = int(input("매트릭스 크기 입력 : "))
spiral_matrix = generate_spiral_matrix(n)
print_matrix(spiral_matrix)
