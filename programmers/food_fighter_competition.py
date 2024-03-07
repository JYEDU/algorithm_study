"""
푸드 파이트 대회
link: https://school.programmers.co.kr/learn/courses/30/lessons/134240
"""

def solution(food):
    left=""
    right=""
    for i in range(1, len(food)):
        num=food[i]//2
        left = left + str(i)*num
        right= str(i)*num + right
    answer = left+"0"+right
    return answer

# 테스트 케이스
case1_pred=solution([1, 3, 4, 6])
case1_true="1223330333221"

case2_pred=solution([1, 7, 1, 2])
case2_true="111303111"

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")