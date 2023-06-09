# 369 게임
# 숫자 중 3의 또는 6 9가 나오면 짝! 아니면 숫자를 말해요
# 3의 배수는 고려하지 않는다

# 애는 369가 2번 나오는 경우를 고려하지 못한다
# for num in range(100):
#     word = str(num)
#     if '3' in word:
#         print("짝")
#     elif '6' in word:
#         print("짝")
#     elif '9' in word:
#         print("짝")
#     else:
#         print(num)

for num in range(100):
    word = str(num)

    if '3' in word or "6" in word or "9" in word:
        print("짝" * (word.count("3") + word.count("6") + word.count("9")), "(", num, ")")

        # 아니면 이렇게 해도 된다
        # for clap in range(word.count("3") + word.count("6") + word.count("9")):
        #     print("짝!", end="")
        #
        # print()

    else:
        print(num)


print("\n\nwhile문으로 무한 369 출력")

num = 1
while True:
    word = str(num)

    if '3' in word or "6" in word or "9" in word:
        print("짝" * (word.count("3") + word.count("6") + word.count("9")), "(", num, ")")
    else:
        print(num)
    num += 1