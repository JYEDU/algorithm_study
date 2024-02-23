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


# 테스트
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))  # 기댓값: 2
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))  # 기댓값: 0