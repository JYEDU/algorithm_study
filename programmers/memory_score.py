"""
추억 점수
link: https://school.programmers.co.kr/learn/courses/30/lessons/176963
"""

# 딕셔너리 활용
def solution(name, yearning, photo):
    answer = []
    score={name[i]:yearning[i] for i in range(len(name))}
    for person_list in photo:
        temp=0
        for person in person_list:
            if person in score:
                temp+=score[person]
        answer.append(temp)
    return answer

# 테스트 케이스
case1_pred=solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])
case1_true=[19, 15, 6]

case2_pred=solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]])
case2_true=[67, 0, 55]

case3_pred=solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"], ["kein", "deny", "may"], ["kon", "coni"]])
case3_true=[5, 15, 0]

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true, case3_pred==case3_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")