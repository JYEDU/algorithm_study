'''
입국심사
link : https://school.programmers.co.kr/learn/courses/30/lessons/43238
'''

def solution(n, times):
    answer=0
    times=sorted(times)
    # 이분탐색을 위한 범위 설정
    start=1             
    end=max(times)*n    
    
    while start <= end:
        # 중간값 계산
        mid = (start+end) //2
        total_people = 0
        
        # 각 심사대에서 처리 가능한 사람 수 계산
        for time in times:
            total_people += mid // time
        
        # 처리 사람 수와 n 비교를 통해 시간 확인
        if total_people >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer

print(solution(6, [7,10])) # 28
