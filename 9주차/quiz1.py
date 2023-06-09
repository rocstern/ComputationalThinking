# 점수가 문자열로 입력됩니다 (최대 5과목)
# 예시: 50 60 40 50 60
# 리스트에 넣고 하나씩 더해서 평균을 구하고 등급을 출력

total_scr = 0
scr_list = "60,80,80,90,100"

# str => list 됨
scr_list = scr_list.split(',')


# for scr in scr_list:
#     total_scr += int(scr)

# total_scr += int(scr_list[1])
# total_scr += int(scr_list[2])
# total_scr += int(scr_list[3])
# total_scr += int(scr_list[0])
# total_scr += int(scr_list[4])

len_list = len(scr_list)

if scr_list:
    total_scr += int(scr_list.pop())
if scr_list:
    total_scr += int(scr_list.pop())
if scr_list:
    total_scr += int(scr_list.pop())
if scr_list:
    total_scr += int(scr_list.pop())
if scr_list:
    total_scr += int(scr_list.pop())
if scr_list:
    total_scr += int(scr_list.pop())
if scr_list:
    total_scr += int(scr_list.pop())


# pop()은 꺼내옴과 함께 데이터를 삭제 함으로 pop()뒤에 len 쓰면 0 나온다
avg_scr = total_scr / len_list

print("총점: ", total_scr)
print("평균: ", avg_scr)