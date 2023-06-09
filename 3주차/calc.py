print(" < 이것은 덧셈 계산기 입니다 > ")

try:
    input_num1 = int(input("첫 번째 숫자를 입력해주세요: "))
    input_num2 = int(input("두 번째 숫자를 입력해주세요: "))

    print(f"{input_num1} + {input_num2} = {input_num1 + input_num2}")

except ValueError:
    print("[ValueError]")
