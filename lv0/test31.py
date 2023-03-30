# https://school.programmers.co.kr/learn/courses/30/lessons/120895
# 인덱스 바꾸기

# 문제 설명
# 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, 
# my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 
# return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 1 < my_string의 길이 < 100
# 0 ≤ num1, num2 < my_string의 길이
# my_string은 소문자로 이루어져 있습니다.
# num1 ≠ num2

my_string = "I love you"
num1 = 3
num2 = 6

# 인덱스 num1과 num2를 바꾸는 방법

# for문사용
answer=''
for i in range(len(my_string)):
    if i==num1: 
        i=num2
    elif i==num2:
        i=num1
    answer+=my_string[i]
print(answer)

# 제출용 함수
def solution(my_string, num1, num2):
    answer=''
    for i in range(len(my_string)):
        if i==num1: 
            i=num2
        elif i==num2:
            i=num1
        answer+=my_string[i]
    return answer