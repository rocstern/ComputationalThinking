# print(10 + 10)
# print(type(10 + 10))
#
# print(type(10 + 0.1))
#
# # 정수 / 정수는 무조건 실수다
# print(type(10 / 10))
#
# print(int(10 / 3))
# print(type(int(10 / 3)))
#
# str1 = "String"
# print(str1[0])
# print(type(str1[0]))
#
# greet = "안녕! 안녕! 안녕! 하세요 저는 OOO입니다."
# print(greet)
#
# str1 += "hi"
# str1 += "hi"
# str1 += "hi"
# str1 += "hi"
# str1 += "hi"
# str1 += "hi"
# str1 += "hi"
#
# print(str1)
#
# # sayHi = '이거 오류 난다요 '치명적인' 문자열 오류다요'
# sayHi = '''이거 오류 난다요 '치명적인' 문자열 오류다요'''
# sayHi = """이거 오류 난다요 '치명적인' 문자열 오류다요"""
# sayHi = "이거 오류 난다요 '치명적인' 문자열 오류다요"
#
# sayHi = '''
#     이렇게 줄 변경도 된다
#     ㅇ으으라람ㄴㅇ미ㅏㅏㄴㅁㅇ
# '''
# print(sayHi)


# str_text = "가나다라마바사"
# str_len = len(str_text)
# print(str_len)
#
# print(str_text[str_len - 1])
#
# print(str_text[0], str_text[1], str_text[2], sep=" ", end="")


str2 = "AbcefG"
print(str2.upper())
print("this is also possible".upper())
print(str2.lower())

print("A".isupper())
print(str2.lower().isupper())

# find 문자열에서 해당 글자 인덱스 반환
print("가나다라마바사아자차카타파하".find("아"))

# count 문자열에서 해당 글자 몇번 나오지는지 반환
print("aaasdagslnajabfsdjfaacx".count("a"))



