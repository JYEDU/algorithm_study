"""
달리기 경주
link: https://school.programmers.co.kr/learn/courses/30/lessons/178871

players: (list) 선수 이름
callings: (list) 추월한 경우 이름 불림
"""
# 제출 코드
def solution(players, callings):
    # 딕셔너리 생성
    player_rank = {player:idx for idx, player in enumerate(players)}
    # 호출에 따라 순위 바꾸기
    for calling in callings:
        # 호출된 플레이어의 순위
        idx = player_rank[calling]
        # 순위 변경
        overtaker = players[idx]
        players[idx] = players[idx-1]
        players[idx-1] = overtaker
        # 딕셔너리 업데이트
        player_rank[calling] = idx-1
        player_rank[players[idx]] = idx
    return players

# 테스트 케이스
case1_players = ["mumu", "soe", "poe", "kai", "mine"]
case1_callings = ["kai", "kai", "mine", "mine"]
case1_answer = ["mumu", "kai", "mine", "soe", "poe"]
case1_pred = solution(case1_players, case1_callings)

# 채점 결과
isanswer = [case1_pred==case1_answer]
print(isanswer.count(True),"/",len(isanswer))