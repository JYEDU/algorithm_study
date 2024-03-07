"""
징검다리
link: https://school.programmers.co.kr/learn/courses/30/lessons/43236
"""

def solution(distance, rocks, n):
    rocks.sort()
    answer = 0
    start, end = 0, distance
    
    while start <= end:
        mid=(start+end)//2
        prev_rock=0
        removed_rocks=0
        
        for rock in rocks:
            if rock - prev_rock < mid :
                removed_rocks += 1
            else:
                prev_rock = rock
        
        if distance - prev_rock < mid:
            removed_rocks += 1
        
        if removed_rocks <= n:
            answer=mid
            start=mid+1
        else:
            end = mid - 1   
    return answer

# 테스트 케이스
case1_pred=solution(25, [2,14,11,21,17], 2)
case1_true=4

# 채점 결과
isanswer = [case1_pred==case1_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")