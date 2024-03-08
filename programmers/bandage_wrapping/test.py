from my_answer.bandage_wrapping import solution

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