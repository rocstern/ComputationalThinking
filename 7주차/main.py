bool1 = 1 > 2
print(bool1)

bool2 = 1 < 2
print(bool2)

if bool2:
    print("조건이 참이에요")
else:
    print("조건이 거짓이에요")

if 1 > 2:
    print("조건이 참이에요")
else:
    print("조건이 거짓이에요")

if bool2 == True:
    print("조건이 참이에요")
else:
    print("조건이 거짓이에요")

# 8시에 일어나야 해요 늦으면 택시 타요. 아니면 걸어가요

wake_time = 5 #int(input("몇시 기상:"))

if wake_time <= 8:
    print("8시 이전에 일어나서 걸어갈 수 있어요.")
else:
    print("8시 이후에 일어나서 택시를 타야해요.")


# 메뉴를 선택 돈 부족하면 못 먹어요
# 커피 1000

coffee = 1000
money = 1500 #int(input("가진 돈을 입력하세요:"))

if money >= coffee:
    print("커피를 마셔요")
else:
    print("커피를 못 먹어요")


cut = 60
scr = 64

if cut <= scr:
    print("합격입니다.")
    print("기분이 좋아요.")
else:
    print("불합격입니다.")
    print("슬퍼요")



bool3 = 'A' > 'B'
if bool3:
    print("조건이 참이에요")
else:
    print("조건이 거짓이에요")

print("\n")

if [1, 2, 3]: # 0: 값이 비어있거나 초가화되어 있는 경우 모두 거짓!!
    print("조건이 참이에요")
else:
    print("조건이 거짓이에요")

print()

bag = ["라면", "콜라", "고기"]

if bag:
    print(bag.pop())

if bag:
    print(bag.pop())

if bag:
    print(bag.pop())

if bag:
    print(bag.pop())





# x not in list
# 준비물 검사 프로그램

needs = ["연필", "색종이", "그림책"]

if "연필" in needs:
    print("연필 있어요.")
else:
    print("연필 없어요.")

if "색종이" in needs:
    print("색종이 있어요.")

if "그림책" not in needs:
    print("그림책 없어요.")
else:
    print("그림책 있어요.")
    
alp_str = "abcdefghi"

if 'a' in alp_str:
    print("a 있어요")
else:
    print("없어요")

# 리스트가 아닌 문자열 일때는 조심해야 한다.
string = "연필, 색종이, 그림책"
if "종이" in string:
    print("종이 있어요.")










































