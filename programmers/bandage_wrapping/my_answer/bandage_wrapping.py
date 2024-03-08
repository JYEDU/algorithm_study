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