print("## 택배를 보내기 위한 정보를 입력하세요. ##")

to_who = input("받는 사람: ")
address = input("주소: ")
weight = input("무게(g): ")

print(f"** 받는 사람 ==> {to_who}")
print(f"** 주소 ==> {address}")
print(f"** 배송비 ==> {int(weight) * 5}원")

