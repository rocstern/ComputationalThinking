# 리스트 딕셔너리 투플

coin_wallet = [100, 500]
bill_wallet = ["오천원", "오만원", coin_wallet]
bag = ["도시락😊", "콜라", "라면", bill_wallet]

print(bag)
print(bag[0])
print(bag[1])
print(bag[2])
print(bag[3])
print(bag[3][0])  # 지갑
print(bag[3][1])
print(bag[3][2])
print(bag[3][2][0])  # 동전지갑
print(bag[3][2][1])


# 스트링은 배열이지만 각 글다가 하나의 데이터
prepare = "도시락, 콜라, 라면"
print(prepare)
print(prepare[0], prepare[1], prepare[2])

print(prepare[0:3])

wString = "가나다라마바사"
print(wString[0:3])
print(wString[2:5])
print(wString[4:7])


str_list = ["가", "나", "다", "라", "마", "바", "사"]
print(str_list[0:3])
print(str_list[2:5])
print(str_list[4:7])


wString = "트와이스"
print(wString[-1])
print(wString[-2])
print(wString[-3])
print(wString[-4])

# 위와 같음
print(wString[len(wString) - 1])
print(wString[len(wString) - 2])
print(wString[len(wString) - 3])
print(wString[len(wString) - 4])

# 이스
print(wString[2:4])
print(wString[2:len(wString)])
print(wString[2:])

# 트와
print(wString[0:2])
print(wString[:2])

# 트와이스
print(wString[0:4])
print(wString[0:len(wString)])
print(wString[:])


lunch_box = []
lunch_box.append("김밥")
lunch_box.append("과자")
lunch_box.append("음료수")
lunch_box.append("삼겹살")
lunch_box.append("맥주")
lunch_box.append("맥주")
lunch_box.append("맥주")
lunch_box.append("맥주")

print(lunch_box)

del(lunch_box[4])
# print(lunch_box.pop())
lunch_box.remove("맥주")

print(lunch_box)

print(f"맥주 {lunch_box.count('맥주')} 병 있어요")

idol = ["트", "와", "이", "스"]
idol.sort()
print(idol)

idol = ["트", "와", "이", "스"]
idol.reverse()
print(idol)
