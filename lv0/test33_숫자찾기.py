# https://school.programmers.co.kr/learn/courses/30/lessons/120904
# 숫자 찾기

# 문제 설명
# 정수 num과 k가 매개변수로 주어질 때, 
# num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 
# 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 0 < num < 1,000,000
# 0 ≤ k < 10
# num에 k가 여러 개 있으면 가장 처음 나타나는 자리를 return 합니다.

num = 291831
k = 1

# find
str_num = str(num)
answer = str_num.find(str(k))
if answer>0:answer+=1
print(answer)

# 제출용 함수
def solution(num, k):
    str_num = str(num)
    answer = str_num.find(str(k))
    if answer>0:answer+=1
    return answer

# find 안쓰고
def solution2(num, k):
    count=1
    a=str(num)
    for i in a:
        if int(i)==k: break
        else : count+=1
    if (count-1)==len(a): count=-1
    answer=count
    return answer