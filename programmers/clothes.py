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

# 테스트 케이스
case1_pred=solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
case1_true=5

case2_pred=solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
case2_true=3

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")