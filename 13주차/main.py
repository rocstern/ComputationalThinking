print("for문 피라미드")
for floor in range(1, 11):
    for empty in range(10, floor, -1):
        print("⬛", end="")

    for width in range(1, floor*2):
        print("⬜", end="")

    for empty in range(floor-1, 9):
        print("⬛", end="")

    print("")

print("")
print("")
print("")
print("")


floor = 0
height = 10

print("while문 피라미드")
for floor in range(floor, height):
    # 공백 계산
    empty = height - floor -1
    while empty > 0:
        print("⬛", end="")
        empty -= 1

    # 너비
    width = 0
    while  width < 1+floor*2:
        print("⬜", end="")
        width += 1

    # 반대 공백
    empty = height - floor - 1
    while empty > 0:
        print("⬛", end="")
        empty -= 1

    floor += 1
    print("")

print("")
print("")
print("")




num = 1

while num < 10:
	dan = 2
	while dan < 10:
		print(f"{dan} x {num} = {dan*num}", end="\t")
		dan += 1

	num += 1
	print("")



