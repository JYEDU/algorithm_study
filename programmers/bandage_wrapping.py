"""
붕대감기
link: https://school.programmers.co.kr/learn/courses/30/lessons/250137?language=python3

bandage: (list) [시전시간, 초당 회복량, 추가 회복량]
health: (int) 최대 체력
attacks: (list) [[공격 시간, 피해량], ...]
"""
# 제출 코드
def solution(bandage, health, attacks):
    # 초기 설정
    current_health = health             # 현재 체력
    max_heal = bandage[0]*bandage[1]    # 붕대감기 t초 연속시 최대 회복량
    heal_count = 0                      # 연속 성공
    attack_time = []                    # 공격받은 시간 리스트
    attack_damage = []                  # 공격받은 데미지 리스트
    for time, damage in attacks:
        attack_time.append(time)
        attack_damage.append(damage) 
    # 몬스터의 마지막 공격까지 초세기
    for i in range(1, max(attacks)[0]+1):
        # 몬스터에게 공격을 받는 경우
        if i in attack_time:
            # 붕대감기 초기화
            heal_count=0
            # 몬스터의 공격을 받으면 피해량만큼 현재 체력량 감소
            current_health-=attack_damage[attack_time.index(i)]
            # 몬스터의 공격을 받은 후 체력이 0이하인 경우 캐릭터 죽음
            if current_health <= 0:
                return -1          
        # 몬스터에게 공격을 받지 않는 경우
        else:
            # 최대 체력보다 체력이 낮은 경우
            if current_health<health:
                # 체력 회복하고 연속 성공 시간 증가
                heal_count+=1
                current_health+=bandage[1]   
                # 만약 최대 체력 회복값이 붕대 감기보다 많은 경우, 현재 체력=최대 체력
                if current_health>health:
                    current_health=health
                # 최대 체력 회복시 추가 회복, 붕대 감기 초기화, 
                if heal_count==bandage[0]:
                    current_health+=bandage[2]
                    heal_count=0
                    # 만약 최대 체력 회복값이 붕대 감기보다 많은 경우, 현재 체력=최대 체력
                    if current_health>health:
                        current_health=health
            # 최대 체력보다 체력이 높은 경우 연속 성공 시간만 증가
            elif current_health>=health:
                heal_count+=1
    return current_health

# 테스트 케이스
case1_bandage = [5, 1, 5]
case1_health = 30
case1_attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]
case1_answer = 5
case1_pred = solution(case1_bandage, case1_health, case1_attacks)

case2_bandage = [3, 2, 7]
case2_health = 20
case2_attacks = [[1, 15], [5, 16], [8, 6]]
case2_answer = -1
case2_pred = solution(case2_bandage, case2_health, case2_attacks)

case3_bandage = [4, 2, 7]
case3_health = 20
case3_attacks = [[1, 15], [5, 16], [8, 6]]
case3_answer = -1
case3_pred = solution(case3_bandage, case3_health, case3_attacks)

case4_bandage = [1, 1, 1]
case4_health = 5
case4_attacks = [[1, 2], [3, 2]]
case4_answer = 3
case4_pred = solution(case4_bandage, case4_health, case4_attacks)

case5_bandage = [3, 10, 1]
case5_health = 100
case5_attacks = [[1, 5], [3, 5]]
case5_answer = 95
case5_pred = solution(case5_bandage, case5_health, case5_attacks)

# 채점 결과
isanswer = [case1_pred==case1_answer, case2_pred==case2_answer, case3_pred==case3_answer, case4_pred==case4_answer, case5_pred==case5_answer]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")