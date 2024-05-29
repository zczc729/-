"""
A씨는 게시판 프로그램을 작성하고 있다.

A씨는 게시물의 총 건수와 한 페이지에 보여줄 게시물수를 입력으로 주었을 때 총 페이지수를 리턴하는 프로그램이 필요하다고 한다.

입력 : 총건수(m), 한페이지에 보여줄 게시물수(n) (단 n은 1보다 크거나 같다. n >= 1)
출력 : 총페이지수
A씨가 필요한 프로그램을 작성하시오.
"""


post = int(input("총 건수 : "))
while True:
    page_post = int(input("한 페이지에 보여줄 게시물 수 : "))

    if page_post >= 1:
        break
    else:
        print("한 페이지에 보여줄 게시물 수는 1이상 이어야 합니다.")

page_num = divmod(post, page_post)

print("m\tn\t출력")

if page_num[0] == 0:
    page_num = 1
    print(f"{post}\t{page_post}\t{page_num}")
else:
    print(f"{post}\t{page_post}\t{page_num[0] + page_num[1]}")



