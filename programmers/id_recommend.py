'''
신규 아이디 추천
link : https://school.programmers.co.kr/learn/courses/30/lessons/72410#

3<=length of id <= 15
The ID can only contain lowercase letters, numbers, minus (-), underscore (_), and period (.) characters.
However, the period (.) cannot be used at the beginning and end, and cannot be used consecutively.
'''

import re

def solution(new_id):

    out = new_id.lower()
    out = re.sub(r'[^a-z0-9-_.]', '', out)
    out = re.sub(r'\.{2,}', '.', out)
    out = re.sub(r'^\.|\.$', '', out)
    if not out:
        out = 'a'
    if len(out)>=16:
        out = out[:15]    
        if out[-1]=='.':
            out = out[:-1]
    if len(out)<=2:
        out=out+out[-1]*(3-len(out))
    return out

# 테스트 케이스
case1_pred=solution("...!@BaT#*..y.abcdefghijklm")
case1_true="bat.y.abcdefghi"

case2_pred=solution("z-+.^.")
case2_true="z--"

case3_pred=solution("=.=")
case3_true="aaa"

case4_pred=solution("123_.def")
case4_true="123_.def"

case5_pred=solution("abcdefghijklmn.p")
case5_true="abcdefghijklmn"

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true, case3_pred==case3_true, case4_pred==case4_true, case5_pred==case5_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")