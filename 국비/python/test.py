num = 2

print("\t\t\t\t\t\t구구단\n")
print("   2단\t\t   3단\t\t   4단\t\t   5단\t\t   6단\t\t   7단\t\t   8단\t\t   9단")

for i in range(1, 10):
    while num <= 9:
        print(f"|{num} * {i} = {num * i}|", end="\t")
        num += 1
    num = 2
    print()







