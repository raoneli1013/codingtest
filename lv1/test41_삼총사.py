# https://school.programmers.co.kr/learn/courses/30/lessons/131705
# 삼총사

# 문제 설명
# 한국중학교에 다니는 학생들은 각자 정수 번호를 갖고 있습니다. 
# 이 학교 학생 3명의 정수 번호를 더했을 때 0이 되면 3명의 학생은 삼총사라고 합니다.
# 예를 들어, 5명의 학생이 있고, 각각의 정수 번호가 순서대로 -2, 3, 0, 2, -5일 때, 
# 첫 번째, 세 번째, 네 번째 학생의 정수 번호를 더하면 0이므로 
# 세 학생은 삼총사입니다. 또한, 두 번째, 네 번째, 다섯 번째 학생의 정수 번호를 
# 더해도 0이므로 세 학생도 삼총사입니다. 따라서 이 경우 한국중학교에서는 두 가지 
# 방법으로 삼총사를 만들 수 있습니다.

# 한국중학교 학생들의 번호를 나타내는 정수 배열 number가 매개변수로 주어질 때, 
# 학생들 중 삼총사를 만들 수 있는 방법의 수를 return 하도록
# solution 함수를 완성하세요.

# 제한사항
# 3 ≤ number의 길이 ≤ 13
# -1,000 ≤ number의 각 원소 ≤ 1,000
# 서로 다른 학생의 정수 번호가 같을 수 있습니다.

number = [-2, 3, 0, 2, -5]


answer = 0
# itertools의 combinations로 3명 조합을 구하고
from itertools import combinations
for i in combinations(number, 3):
    # 각 조합의 합이 0이면 answer +1 씩 해주면 될 듯
    if sum(i) == 0 : answer+=1

print(answer)

# 제출용 함수
from itertools import combinations
def solution(number):
    answer = 0
    for i in combinations(number, 3):
        if sum(i) == 0 : answer+=1
    return answer

# 근데 솔직히 itertools쓰면 노잼임
# 그냥 한번 풀어보자

# 3명 combinations(조합)을 구하는 방법은 의외로 쉽다
# 대신 노가다가 있을 뿐
arr = []
for i in range(len(number)-2):
    for j in range(i+1,len(number)-1):
        for k in range(j+1,len(number)):
            # number[i],number[j],number[k]가 이제 3명 combinations가 된다
            # 이걸 모두 더했을 때 0 이 되면 answer +1
            if number[i]+number[j]+number[k] == 0: answer +=1
print(answer)

# 제출용 함수2
def solution(number):
    answer = 0
    for i in range(len(number)-2):
        for j in range(i+1,len(number)-1):
            for k in range(j+1,len(number)):
                if number[i]+number[j]+number[k] == 0: answer +=1
    return answer

