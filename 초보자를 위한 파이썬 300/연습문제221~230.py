# 221
# 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.
#
# print_reverse("python")
# nohtyp
# 정답확인
# 222
# 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.
#
# print_score ([1, 2, 3])
# 2.0
# 정답확인
# 223
# 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
#
# print_even ([1, 3, 2, 10, 12, 11, 15])
# 2
# 10
# 12
def print_even(a):
    for b in a:
        if b%2 ==0:
            print(b)
print_even([1,3,2,10,12,11,15])


# 224
# 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
#
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})
# 이름
# 나이
# 성별
def print_keys(dic):
    for keys in dic.keys():
        print(keys)
print_keys ({"이름":"김말똥", "나이":30, "성별":0})


# 225
# my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.
#
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.
#
# print_value_by_key  (my_dict, "10/26")
# [100, 130, 100, 100]
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
# def print_value_by_key(dic):
#     for keys in print_value_by_key.key():
#         print(print_value_by_key.value())
# print_value_by_key  (my_dict, "10/26")
def print_value_by_key(my_dict, a):
    print(my_dict[a])
print_value_by_key  (my_dict, "10/26")



# 226
# 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
#
# print_5xn("아이엠어보이유알어걸")
# 아이엠어보
# 이유알어걸

# def print_5xn(string):
#     print(string[:5])
#     print(string[5:])
# print_5xn("아이엠어보이유알어걸")

def print_5xn(line):
    chunk_num = int(len(line) / 5)
    for x in range(chunk_num + 1) :
        print(line[x * 5: x * 5 + 5])

# 227
# 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
#
# printmxn("아이엠어보이유알어걸", 3)
# 아이엠
# 어보이
# 유알어
# 걸
def printmxn(line, num):
    chunk_num = int(len(line)/num) #10 > 3, 11 >3
    for x in range(chunk_num+1):
        print(line[x*3:(x+1)*3])
printmxn("아이엠어보이유알어걸", 3)

# 228
# 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
#
# calc_monthly_salary(12000000)
# 1000000
def calc_monthly_salary(a):
    a = int(a)
    print(int(a/12))

calc_monthly_salary(12000001)

# 229
# 아래 코드의 실행 결과를 예측하라.
#
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
#
# my_print(a=100, b=200)


# 230
# 아래 코드의 실행 결과를 예측하라.
#
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
#
# my_print(b=100, a=200)
# 정답확인