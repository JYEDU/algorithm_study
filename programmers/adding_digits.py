"""
자릿수 더하기
link: https://school.programmers.co.kr/learn/courses/30/lessons/12931
"""

def solution(n):
    answer = 0
    for i in str(n):
        answer+=int(i)
    return answer


# 테스트 케이스
case1_pred=solution(123)
case1_true=6

case2_pred=solution(987)
case2_true=24

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")