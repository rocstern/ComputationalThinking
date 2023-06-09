
# 구구단 출력 2단

for dan in range(2, 10, 1):
    for num in range(1, 10, 1):
        print(f"{dan} x {num} = {dan*num}")
    print("\n")


# 학생 줄 세우기 경우의 수 구하기 // 팩토리얼

students = 5
outcome = 1

for num in range(1, students + 1, 1):
    outcome *= num

print("총 경우의 수: ", outcome)


# 단에 해당하는 구구단을 출력

dan = 3

for num in range(1, 11, 1):
    print(dan, "x", num, "=", dan*num)


for dan in range(2, 10, 1):
    for num in range(1, 10, 1):
        print(dan, "x", num, "=", dan * num)
