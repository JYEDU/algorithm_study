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