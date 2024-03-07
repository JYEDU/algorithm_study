'''
N으로 표현
link : https://school.programmers.co.kr/learn/courses/30/lessons/42895
'''

def solution(N, number):
    # dp[i]: i번째로 만들 수 있는 모든 수의 집합
    dp = [set() for _ in range(9)]

    # 초기화: 5, 55, 555, ..., 55555까지 추가
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))

    # 사칙연산을 통한 계산
    for i in range(1, 9):
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)

        # 목표 숫자가 만들어지면 해당 사용 횟수 반환
        if number in dp[i]:
            return i

    # 목표 숫자를 만들 수 없는 경우 -1 반환
    return -1

# 테스트 케이스
case1_pred=solution(5, 12)
case1_true=4

case2_pred=solution(2, 11)
case2_true=3

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")