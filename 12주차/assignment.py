
for num in range(1, 10, 1):
    for dan in range(2, 10, 1):
        print(dan, "x", num, "=", dan*num, end="\t")
    print()


std1 = [100,90,80]
std2 = [90,90,80]
std3 = [100,90,70]

std_list = [std1, std2, std3]

for std in std_list:
    for scr in std:
        print(scr)