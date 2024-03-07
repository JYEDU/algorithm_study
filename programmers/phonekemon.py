'''
폰켓몬
link : https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3
'''

def solution(nums):
    max_get_nums=len(nums)//2
    type_nums=len(set(nums))
    if max_get_nums>=type_nums:
        return type_nums
    else:
        return max_get_nums

# 테스트 케이스
case1_pred=solution([3, 1, 2, 3])
case1_true=2

case2_pred=solution([3, 3, 3, 2, 2, 4])
case2_true=3

case3_pred=solution([3, 3, 3, 2, 2, 2])
case3_true=2

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true, case3_pred==case3_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")