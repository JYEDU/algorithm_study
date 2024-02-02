def solution(nums):
    '''
    폰켓몬
    link : https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3
    '''
    max_get_nums=len(nums)//2
    type_nums=len(set(nums))
    if max_get_nums>=type_nums:
        return type_nums
    else:
        return max_get_nums