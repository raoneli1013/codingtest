# https://school.programmers.co.kr/learn/courses/30/lessons/120893
# 대문자와 소문자

# 문제설명
# 문자열 my_string이 매개변수로 주어질 때, 
# 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 
# return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 <= my_string의 길이 <= 1000
# my_sting은 영어 대문자와 소문자로만 구성되어 있습니다.

def solution(my_string):
    answer = ''
    for i in my_string:
        if i==i.upper(): answer += i.lower()
        else: answer += i.upper()
    return answer
