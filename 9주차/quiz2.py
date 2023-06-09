# 반환되는 동전 수를 출력하라

money = 3563


if money >= 500:
    print("오백원 ", money // 500, "개")
    money -= 500 * (money // 500)
    
if money >= 100:
    print("백원 ", money // 100, "개")
    money -= 100 * (money // 100)
    
if money >= 50:
    print("오십원 ", money // 50, "개" )
    money -= 50 * (money // 50)
    
if money >= 10:
    print("십원 ", money // 10, "개")
    money -= 10 * (money // 10)
    
if money >= 1:
    print("일원 ", money // 1, "개")
    money -= 1 * (money // 1)