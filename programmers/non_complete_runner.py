'''
완주하지 못한 선수
link : https://school.programmers.co.kr/learn/courses/30/lessons/42576
'''

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

# 테스트 케이스
case1_pred=solution(["leo", "kiki", "eden"], ["eden", "kiki"])
case1_true="leo"

case2_pred=solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
case2_true="vinko"

case3_pred=solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
case3_true="mislav"

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true, case3_pred==case3_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")