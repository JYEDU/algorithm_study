'''
공원 산책
link: https://school.programmers.co.kr/learn/courses/30/lessons/172928
'''

def solution(park, routes):
    # 시작점 이동 가능 경로 찾기
    max_h, max_w = len(park), len(park[0])
    visited= [[False] * max_w for _ in range(max_h)]
    for h in range(max_h):
        for w in range(max_w):
            if park[h][w]=="S":
                current=[h,w]
                visited[h][w]=True
            elif park[h][w]=="O":
                visited[h][w]=True
    # 이동 방향 정의
    moves = { "E": [0, 1], "W": [0, -1], "N": [-1, 0], "S": [1, 0] }
    # 이동 가능한지 확인 후 이동
    for route in routes:
        length = int(route[-1])
        move=moves[route[0]]
        for i in range(1, length+1):
            temp=[current[0]+move[0]*i, current[1]+move[1]*i]
            if (0<=temp[0]<max_h and 0<=temp[1]<max_w) and (visited[temp[0]][temp[1]]):
                if i==length:    
                    current=temp.copy()  
            else:
                break   
    return current

# 테스트 케이스
case1_pred=solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"])
case1_true=[2, 1]

case2_pred=solution(["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"])
case2_true=[0, 1]

case3_pred=solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"])
case3_true=[0, 0]

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true, case3_pred==case3_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")