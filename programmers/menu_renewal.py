'''
메뉴 리뉴얼
link : https://school.programmers.co.kr/learn/courses/30/lessons/72411
'''

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for course_size in course:
        course_candidates = []
        for order in orders:
            order_combinations = combinations(sorted(order), course_size)
            course_candidates.extend(order_combinations)

        if not course_candidates:
            continue

        counter = Counter(course_candidates)
        max_count = max(counter.values())

        if max_count >= 2:
            answer += [''.join(course) for course, count in counter.items() if count == max_count]

    return sorted(answer)

# 테스트 케이스
case1_pred=solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
case1_true=["AC", "ACDE", "BCFG", "CDE"]

case2_pred=solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])
case2_true=["ACD", "AD", "ADE", "CD", "XYZ"]

case3_pred=solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
case3_true=["WX", "XY"]

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true, case3_pred==case3_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")