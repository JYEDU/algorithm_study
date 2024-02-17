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