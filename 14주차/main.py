num = 1
while num < 11:
    print(num)
    num += 1

# while문 밖에서 증가값이 얼마인지 아는게 중요하다
print("while 루프 밖: ", num)

for nums in range(1, 11, 1):
    print(nums)

print("for 루프 밖: ", nums)


# 1~10 중 짝수 홀수만 출력
for num in range(1, 11, 2):
    print(num)

num = 2
while num < 11:
    print(num)
    num += 2

print(list(range(2, 11, 2)))

for num in range(1, 11, 1):
    if num % 2 == 0:
        print(f"짝 {num}")
    else:
        print(f"홀 {num}")


# 줄 바꿈 칸에 매우 주의해야 한다
num = 1
while num < 11:
    if num % 2 == 0:
        print(f"even nmber: {num}")
    else:
        print(f"odd number: {num}")
    num += 1

# 들여쓰기 잘못하면 결과가 완전히 다르다
# num = 1
# while num < 11:
#     if num % 2 == 0:
#         print(f"even nmber: {num}")
#     else:
#         print(f"odd number: {num}")
# num += 1          얘는 while문 밖에 num 증가식이 있어서 1에서 무한 반복된다
#         num += 1  # 얘는 홀수일때만 증가식이 있어서 2에서 무한 반복된다

scores = [100,90,80,90]

sum = 0
for score in scores:
    sum += int(score)
    
print(f"총합은 {sum} 입니다")


sum = 0
for num in range(0, len(scores), 1):
    sum += scores[num]

print(f"이렇게 해도 총합: {sum}")

num = 0
hap = 0
while num < len(scores):
    hap += scores[num]
    num += 1

print(f"hap: {hap}")

scrs = [100, 90, 80, 90]
bonus = [1, 2, 3, 4]

idx = 0
while idx < len(scrs):
    hap = scrs[idx] + bonus[idx]
    print(f"hap: {hap}, scr: {scrs[idx]}, bonus: {bonus[idx]}")
    scrs[idx] += bonus[idx]
    idx += 1

print("asd")
print(f"보너스 적용 후 점수: {scrs}")


scrs = [100, 90, 80, 90]
bonus = [1, 2, 3, 4]

print("\nfor문 합계")
for idx in range(len(scrs)):
    hap = scrs[idx] + bonus[idx]
    print(f"hap: {hap}, scr: {scrs[idx]}, bonus: {bonus[idx]}")
    scrs[idx] += bonus[idx]


std1 = [90, 60, 80]
std2 = [100, 10, 50]
std3 = [50, 90, 100]

students = [std1, std2, std3]

# 전체 학생들의 점수를 출력 합 출력

for i in range(len(students)):
    hap = 0
    for j in range(0, 3, 1):
        print(f"{i+1}번째 학생 점수: {students[i][j]}")
        hap += students[i][j]

    print(f"{i+1}번째 학생 점수 총합: {hap}")


# 아니면 이렇게 해도 된다
for std in students:
    for scr in std:
        print(scr)


std_num = 0
while std_num < len(students):
    scr_num = 0
    while scr_num < len(students[std_num]):
        print(students[std_num][scr_num])
        scr_num += 1
    std_num += 1








