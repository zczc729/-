num = int(input("몇 단인가?"))

def pad_center_char(input_str, pad_char, total_length):
    padding_length = (total_length - len(input_str)) // 2
    padded_str = pad_char * padding_length + input_str + pad_char * padding_length

    if len(padded_str) < total_length:
        padded_str += pad_char
    return padded_str

input_str = "구  구  단"
pad_char = "#"
total_length = num*8

print(pad_center_char(input_str, pad_char, total_length))

for k in range(1, num+1):
    if k < num:
        print(f"{k}단", end="\t")
    else:
        print(f"{k}단")

for i in range(1,num+1):
    for j in range(1,num+1):
        if j % num == 0:
            print(i*j, end="\n")
        else:
            print(i*j,end="\t")