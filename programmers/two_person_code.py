'''
둘만의 암호
link: https://school.programmers.co.kr/learn/courses/30/lessons/155652
'''
# 제출 코드
def solution(s, skip, index):
    answer = ''
    # 전체 알파벳 중 skip에 있는 알파벳 제외
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(skip)):
        alpha.remove(skip[i])
    answer = ''
    # 문자열 s를 alpha의 위치로 찾은 후, index만큼 더하고, z를 넘어갈 경우 다시 a 로 돌아감
    for j in range(len(s)):
        answer += alpha[(alpha.index(s[j])+index)%len(alpha)]
    return answer

# 테스트 케이스
case1_pred = solution("aukks", "wbqd", 5)
case1_true = "happy"

# 채점 결과
isanswer = [case1_pred==case1_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")