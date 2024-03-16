"""
부족한 금액 계산하기
link: https://school.programmers.co.kr/learn/courses/30/lessons/82612
"""

def solution(price, money, count):
    pay=0
    for i in range(1,count+1):
        pay+=price*i
    if pay>money:
        return pay-money
    else:
        return 0
    

# 테스트 케이스
case1_pred=solution(3, 20, 4)
case1_true=10

case2_pred=solution(3, 20, 2)
case2_true=0

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")