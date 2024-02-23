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