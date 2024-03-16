"""
나머지가 1이 되는 수 찾기
link: https://school.programmers.co.kr/learn/courses/30/lessons/87389
"""

def solution(n):
    for i in range(1,1000000):
        if n%i==1:
            return i
    
# 테스트 케이스
case1_pred=solution(10)
case1_true=3

case2_pred=solution(12)
case2_true=11

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")
