'''
덧칠하기
link: https://school.programmers.co.kr/learn/courses/30/lessons/161989
'''

def solution(n, m, section):
    max_value=max(section)
    min_value=min(section)    
    # 한번에 페인트칠이 가능한 경우
    if max_value-min_value+1<=m:
        return 1
    # 한번에 페인트칠이 불가능한 경우
    else:  
        answer=1
        move=section[0]+m
        for i in section:
            if i>=move:
                answer+=1
                move=i+m
        return answer
    
# 테스트 케이스
case1_pred=solution(8,4,[2,3,6])
case1_true=2

case2_pred=solution(5,4,[1, 3])
case2_true=1

case3_pred=solution(4,1,[1, 2, 3, 4])
case3_true=4

case4_pred=solution(5,2,[1, 2, 5])
case4_true=2

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true, case3_pred==case3_true, case4_pred==case4_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")