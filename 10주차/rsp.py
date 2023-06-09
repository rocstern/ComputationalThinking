player = "가위"
com = "보"


# 중복될 수 있는 범위가 아니라
# 값이 명확한 경우 else 안쓰고 if문만 중첩해서 가능
if player == "가위":
    if com == "가위":
        print("비겼습니다.")
    if com == "바위":
        print("졌습니다.")
    if com == "보":
        print("이겼습니다")
        
elif player == "바위": 
    if com == "가위":
        print("이겼습니다.")
    if com == "바위":
        print("비겼습니다.")
    if com == "보":
        print("졌습니다")

elif player == "보":
    if com == "가위":
        print("졋습니다.")
    if com == "바위":
        print("이겼습니다.")
    if com == "보":
        print("비겼습니다")

if player == "가위" and com == "가위":
    print("비겼습니다.")
if player == "바위" and com == "바위":
    print("비겼습니다.")
if player == "보" and com == "보":
    print("비겼습니다.")

if player == "가위" and com == "보":
    print("이겼습니다.")
if player == "바위" and com == "가위":
    print("이겼습니다.")
if player == "보" and com == "바위":
    print("이겼습니다.")

if player == "가위" and com == "바위":
    print("졌습니다.")
if player == "바위" and com == "보":
    print("졌습니다.")
if player == "보" and com == "가위":
    print("졌습니다.")