"""
삼총사
link: https://school.programmers.co.kr/learn/courses/30/lessons/131705

number (list) : 한국중학교 학생들의 번호를 나타내는 정수 배열
result (int) : 학생들 중 삼총사를 만들 수 있는 방법의 수
                 3명의 학생의 정수 번호의 합이 0인 경우, 삼총사
"""

def solution(number):
    result = 0
    total_student=len(number)
    for a in range(total_student):
        for b in range(a+1, total_student):
            for c in range(b+1, total_student):
                if number[a]+number[b]+number[c]==0:
                    result+=1
    return result

print(solution([-2, 3, 0, 2, -5])) #2
print(solution([-3, -2, -1, 0, 1, 2, 3])) #5
print(solution([-1, 1, -1, 1])) #0
