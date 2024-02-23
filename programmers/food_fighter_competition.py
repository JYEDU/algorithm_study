"""
푸드 파이트 대회
link: https://school.programmers.co.kr/learn/courses/30/lessons/134240
"""

def solution(food):
    left=""
    right=""
    for i in range(1, len(food)):
        num=food[i]//2
        left = left + str(i)*num
        right= str(i)*num + right
    answer = left+"0"+right
    return answer


print(solution([1, 3, 4, 6])) #"1223330333221"
print(solution([1, 7, 1, 2])) #"111303111"



1223330333221