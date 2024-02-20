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