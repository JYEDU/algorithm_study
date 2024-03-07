"""
삼총사
link: https://school.programmers.co.kr/learn/courses/30/lessons/131705

number (list) : 한국중학교 학생들의 번호를 나타내는 정수 배열
result (int) : 학생들 중 삼총사를 만들 수 있는 방법의 수
                 3명의 학생의 정수 번호의 합이 0인 경우, 삼총사
"""
# 제출 코드
def solution(number):
    result = 0
    total_student=len(number)
    for a in range(total_student):
        for b in range(a+1, total_student):
            for c in range(b+1, total_student):
                if number[a]+number[b]+number[c]==0:
                    result+=1
    return result

# 테스트 케이스
case1_pred=solution([-2, 3, 0, 2, -5])
case1_true=2
case2_pred=solution([-3, -2, -1, 0, 1, 2, 3])
case2_true=5
case3_pred=solution([-1, 1, -1, 1])
case3_true=0

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true, case3_pred==case3_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")