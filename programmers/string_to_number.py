"""
문자열을 정수로 바꾸기
link: https://school.programmers.co.kr/learn/courses/30/lessons/12925

문제 설명
- 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

제한 조건
- s의 길이는 1 이상 5이하입니다.
- s의 맨앞에는 부호(+, -)가 올 수 있습니다.
- s는 부호와 숫자로만 이루어져있습니다.
- s는 "0"으로 시작하지 않습니다.
"""
# 제출 코드
def solution(s):
    answer = 0
    if s[0]=="+":
        return int(s[1:])
    elif s[0]=="-":
        return -1*int(s[1:])
    else:
        return int(s)

# 테스트 케이스    
case1_s = "1234"
case1_answer = 1234
case1_pred = solution(case1_s)

case2_s = "-1234"
case2_answer = -1234
case2_pred = solution(case2_s)

# 채점 결과
isanswer = [case1_pred==case1_answer, case2_pred==case2_answer]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")