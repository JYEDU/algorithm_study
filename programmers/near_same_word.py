"""
가장 가까운 같은 글자
link: https://school.programmers.co.kr/learn/courses/30/lessons/142086
"""

def solution(s):
    answer = []
    words = ""
    for word in s:
        if word not in words:
            answer.append(-1)
            words+=word
        else: 
            temp=len(words)-words.rindex(word)
            answer.append(temp)
            words+=word
    return answer

# 테스트 케이스
case1_pred=solution("banana")
case1_true=[-1, -1, -1, 2, 2, 2]

case2_pred=solution("foobar")
case2_true=[-1, -1, 1, -1, -1, -1]

case3_pred=solution("abcda")
case3_true=[-1, -1, -1, -1, 4]

case4_pred=solution("acacddd")
case4_true=[-1, -1, 2, 2, -1, 1, 1]

case5_pred=solution("aabba")
case5_true=[-1, 1, -1, 1, 3]

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true, case3_pred==case3_true, case4_pred==case4_true, case5_pred==case5_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")