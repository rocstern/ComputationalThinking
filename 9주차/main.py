if True:
    print("조건이 참이에요")
else:
    print("조건은 거짓이에요")

score = 100

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

if score >= 90:
    print("A")
if score >= 80 and score < 90:
    print("B")
if score >= 70 and score < 80:
    print("C")
if score >= 60 and score < 70:
    print("D")
if score < 60:
    print("F")


# 위와 아래는 결과는 같지만 쓰임새가 다르다
# 조건에 대한 결과가 1개인 경우는 elif를 주로 사용한다




# 조건1 F -> 조건2 판별 ... 이런 방식으로 작동한다
score = 70

if score >= 60:
    print("D")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 90:
    print("A")
else:
    print("F")



























