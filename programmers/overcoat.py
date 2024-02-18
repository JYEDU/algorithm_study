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