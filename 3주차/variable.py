val1 = 1234
val2 = 4321

print(f"val1 type: {type(val1)}")
print(f"val2 type: {type(val2)}")

result = val1 / val2

print(f"result type: {type(result)}")
print(result)

print(val1, val2, result, "문자열도 가능", 100 + 200, val1 + val2, sep="\n", end="\n\n\n")

m1 = "+"
m2 = "="

print(val1 , m1, val2, m2, val1 + val2, end="\n\n\n")

str1 = "안녕하세요."
str2 = "OOO입니다."

str1 = input("뭐라고 인사할까요?")
str2 = input("이름을 입력하세요")

greet_word = str1 + "하세요." + str2 + "입니다."

print(str1.isdigit())
print(greet_word)













