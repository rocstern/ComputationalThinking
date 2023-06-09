# str1 = '\"어떤 글자를 \\\"강조\\\"하는 효과1\"'
# print(str1)


str1 = "트와이스"
slen = len(str1)
rev_str = str1[slen-1] + str1[slen-2] + str1[slen-3] + str1[slen-4]

print("원본 문자열 ==> ", str1)
print("반대 문자열 ==> ", rev_str)
