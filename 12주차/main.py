

# in range(시작, 끝+1, 증가값)

# for i in [0, 1, 2]:
#     print(i, " 출력")

# for num in range(10):
#     print(num)
#
# for num in range(0, 10, 1):
#     print(num)


# 1 ~10 숫자 중 짝수 출력

for num in range(2, 11, 2):
    print(num)

# or
for num in range(1, 11, 1):
    if num % 2 == 0:
        print(num)


print(list(range(1, 11, 2)))

for num in [1, 3, 5, 7, 9]:
    print(num)

for char in "String":
    print(char)


score = "100 90 98 80 100"
scores = score.split(' ')
scr_sum = 0

for scr in scores:
    scr_sum += int(scr)

# 총점
print("총점: ", scr_sum)

# 평균
print("평균: ", scr_sum / len(scores))


# 평균보다 높은 과목 총점과 평균

abv_scores = []
abv_sum = 0

for scr in scores:
    if int(scr) > scr_sum / len(scores):
        abv_scores.append(scr)
        abv_sum += int(scr)

print(abv_scores)
print(abv_sum)


# 평균보다 낮은 점수들 총점과 평균 구하기
bel_scores = []
bel_sum = 0

for scr in scores:
    if int(scr) < scr_sum / len(scores):
        bel_scores.append(scr)
        bel_sum += int(scr)

print("평균보다 낮은 점수들 총점: ", bel_sum)
print("평균보다 낮은 점수들 평균: ", bel_sum / len(bel_scores))





























