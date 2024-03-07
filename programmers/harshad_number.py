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

# 테스트 케이스
case1_pred=solution(10)
case1_true=True

case2_pred=solution(12)
case2_true=True

case3_pred=solution(11)
case3_true=False

case4_pred=solution(13)
case4_true=False

case5_pred=solution(10000)
case5_true=True

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true, case3_pred==case3_true, case4_pred==case4_true, case5_pred==case5_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")