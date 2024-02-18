'''
하샤드 수 구하기
link: https://school.programmers.co.kr/learn/courses/30/lessons/12947#

하샤드 수 : x의 자릿수의 합으로 x가 나누어져야 함
예시) x가 18이라면, 1+8=9, 18은 9로 나누어 떨어지므로 18은 하샤드 수
'''

def solution(x):
    answer=0
    for i in str(x):
        answer+=int(i)
    return x%answer==0