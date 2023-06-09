# 리스트와 비슷하나 데이터 수정이 안된다
# 소괄호를 사용함

idol = {"이름": "트와이스", "구성원수": 9, "데뷔": "서바이벌 식스틴", "대표곡": "cry or me", "이름": "스위왕트", 0: "0을 키로 사용하겠다"}

print(idol)

print(idol["이름"])
idol["이름"] = "트와이스"
idol["별명"] = "스와이트"
print(idol[0])

print(list(idol.keys()))

print(idol.values())