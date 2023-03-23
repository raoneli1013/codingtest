# https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 양꼬치

# 문제 설명
# 머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 
# 양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다. 
# 정수 n과 k가 매개변수로 주어졌을 때, 
# 양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 
# return 하도록 solution 함수를 완성해보세요.

# 제한 사항
# 0 < n < 1000
# n/10 <= k < 1000
# 서비스로 받은 음료수는 모두 마신다

def solution(n,k):
    answer = 12000 * n + 2000 * (k-n//10)
    return answer

