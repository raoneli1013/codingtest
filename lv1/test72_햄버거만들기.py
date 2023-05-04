# https://school.programmers.co.kr/learn/courses/30/lessons/133502
# 햄버거 만들기

# 문제 설명
# 상수가 일하는 가게는 정해진 순서(아래서부터, 빵 – 야채 – 고기 - 빵)로 쌓인 
# 햄버거만 포장을 합니다. 상수는 손이 굉장히 빠르기 때문에 
# 상수가 포장하는 동안 속 재료가 추가적으로 들어오는 일은 없으며, 
# 재료의 높이는 무시하여 재료가 높이 쌓여서 일이 힘들어지는 경우는 없습니다.

# 예를 들어, 상수의 앞에 쌓이는 재료의 순서가 
# [야채, 빵, 빵, 야채, 고기, 빵, 야채, 고기, 빵]일 때, 
# 상수는 여섯 번째 재료가 쌓였을 때, 세 번째 재료부터 여섯 번째 재료를 이용하여 
# 햄버거를 포장하고, 아홉 번째 재료가 쌓였을 때, 두 번째 재료와 일곱 번째 재료부터
# 아홉 번째 재료를 이용하여 햄버거를 포장합니다. 즉, 2개의 햄버거를 포장하게 됩니다.

# 상수에게 전해지는 재료의 정보를 나타내는 정수 배열 ingredient가 주어졌을 때, 
# 상수가 포장하는 햄버거의 개수를 return 하도록 solution 함수를 완성하시오.

# 제한사항
# 1 ≤ ingredient의 길이 ≤ 1,000,000
# ingredient의 원소는 1, 2, 3 중 하나의 값이며, 순서대로 빵, 야채, 고기를 의미합니다.

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
# result = 2

arr = []
answer = 0
for i in ingredient:
    arr.append(i)
    if i == 1:
        if arr[-4:]==[1,2,3,1]:
            del arr[-4:]
            answer+=1
print(answer)

# def solution(ingredient):
#     answer = 0
#     s = ''.join(map(str,ingredient))
#     while True:
#         s_idx = s.find('1231')
#         if s_idx==-1: break
#         answer+=1
#         s=s[:s_idx]+s[s_idx+4:]
#     return answer

def solution(ingredient):
    arr = []
    answer = 0
    for i in ingredient:
        arr.append(i)
        if i == 1:
            if arr[-4:]==[1,2,3,1]:
                del arr[-4:]
                answer+=1
    return answer