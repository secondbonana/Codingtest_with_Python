# 211
# 함수의 호출 결과를 예측하라.
#
# def 함수(문자열) :
#     print(문자열)
#
# 함수("안녕")
# 함수("Hi")
def 함수(문자열) :
    print(문자열)

def print_coin():
    print("비트코인")

def 함수(문자열) :
    print(문자열)

# 함수("안녕")
#함수("Hi")
# 212
# 함수의 호출 결과를 예측하라.
#
# def 함수(a, b) :
#     print(a + b)
#
# 함수(3, 4)
# 함수(7, 8)
# 정답확인
# 213
# 아래와 같은 에러가 발생하는 원인을 설명하라.
#
# def 함수(문자열) :
#     print(문자열)
# 함수()
# TypeError: 함수() missing 1 required positional argument: '문자열'
# 정답확인
# 214
# 아래와 같은 에러가 발생하는 원인을 설명하라.
#
# def 함수(a, b) :
#     print(a + b)
#
# 함수("안녕", 3)
# TypeError: must be str, not int

# 215
# 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
def print_with_smile(a):
    print(a+":D")
print_with_smile("aaaaa")

# 216
# 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.
#

# 217
# 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
#
def print_upper_price(a):
    print(a*1.3)
print_upper_price(100)

# 218
# 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.
#
def print_sum(a, b):
    print(a+b)
print_sum(1, 3)

# 219
# 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.
#
# print_arithmetic_operation(3, 4)
# 3 + 4 = 7
# 3 - 4 = -1
# 3 * 4 = 12
# 3 / 4 = 0.75
# 정답확인
# 220
# 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.
#
print("0000000")
def print_max(a, b, c):
    if (a>b) and (a>c):
        print(a)
    elif (b>a) and (b>c):
        print(b)
    else:
        print(c)
print_max(1,2,3)

print("0000000")
def print_max2(a, b, c) :
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)
print_max2(10,2,1)
print_max2(10,20,1)
print_max2(10,20,30)