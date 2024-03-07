'''
개인정보 수집 유효기간
link: https://school.programmers.co.kr/learn/courses/30/lessons/150370
모든 달은 28일까지 있다고 가정
'''

def solution(today, terms, privacies):
    # today 정의
    now=[int(i) for i in today.split(".")]
    # terms 정의
    check_t={}
    for term in terms:
        term_t, term_m = term.split(" ")
        check_t[str(term_t)]=int(term_m)
    # 파기할 개인정보 찾기
    answer=[]
    # 수집된 개인정보
    for num in range(len(privacies)):
        collect_d, collect_t = privacies[num].split(" ")
        col=[int(i) for i in collect_d.split(".")]
        # terms에 따른 유효기간 계산
        exp=[col[0], col[1]+check_t[collect_t], col[2]]
        while exp[1]>12:
            exp=[exp[0]+1, exp[1]-12, exp[2]]
        # now와 exp 비교
        if now[0]>exp[0]:
            answer.append(num+1)
        elif now[0]==exp[0] and now[1]>exp[1]:
            answer.append(num+1)
        elif now[0]==exp[0] and now[1]==exp[1] and now[2]>=exp[2]:
            answer.append(num+1)
    return answer

# 테스트 케이스
case1_pred=solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
case1_true=[1, 3]

case2_pred=solution("2023.01.01", ["A 6"], ["2022.07.01 A", "2022.07.01 A", "2022.07.01 A"])
case2_true=[1, 2, 3]

case3_pred=solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
case3_true=[1, 4, 5]

case4_pred=solution("2019.12.09", ["A 12"], ["2018.12.10 A", "2010.10.10 A"])
case4_true=[2]

case5_pred=solution("2009.12.28", ["A 13"], ["2008.11.03 A"])
case5_true=[1]

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true, case3_pred==case3_true, case4_pred==case4_true, case5_pred==case5_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")