"""
햄버거 만들기
link: https://school.programmers.co.kr/learn/courses/30/lessons/133502
"""

def solution(ingredient):
    answer=0
    new=[]
    for i in ingredient:
        new.append(i)
        if len(new)>=4:
            if new[-1]==1 and new[-2]==3 and new[-3]==2 and new[-4]==1:
                answer+=1
                for _ in range(4):
                    new.pop()
    return answer

# 테스트 케이스
case1_pred=solution([2, 1, 1, 2, 3, 1, 2, 3, 1])
case1_true=2

case2_pred=solution([1, 3, 2, 1, 2, 1, 3, 1, 2])
case2_true=0

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")