'''
의상
link: https://school.programmers.co.kr/learn/courses/30/lessons/42578
'''

from collections import Counter
from functools import reduce

def solution(clothes):
    # 각 종류별 의상 개수를 카운트
    counter = Counter([kind for name, kind in clothes])

    # 각 종류별 의상 개수에 1을 더하고 모두 곱함
    answer = reduce(lambda x, y: x * (y + 1), counter.values(), 1)

    # 아무것도 입지 않는 경우를 제외함
    return answer - 1