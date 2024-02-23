'''
정수 삼각형
link : https://school.programmers.co.kr/learn/courses/30/lessons/43105
'''

def solution(triangle):
    # 삼각형의 크기
    size = len(triangle)

    # 삼각형의 각 위치에 도달했을 때의 최댓값을 저장할 DP 배열 초기화
    dp = [[0] * i for i in range(1, size + 1)]
    dp[0][0] = triangle[0][0]

    # 다이나믹 프로그래밍을 통해 최댓값 계산
    for i in range(1, size):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
            
    # 마지막 행에서 최댓값 반환
    return max(dp[-1])


triangle = [
    [7], 
    [3, 8], 
    [8, 1, 0], 
    [2, 7, 4, 4], 
    [4, 5, 2, 6, 5]
]

print(solution(triangle)) # 30