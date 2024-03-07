"""
신고 결과 받기
link: https://school.programmers.co.kr/learn/courses/30/lessons/92334
"""

def solution(id_list, reports, k):
    # id_list 기준 메일 보낼 횟수 초기화
    answer = [0]*len(id_list)
    # 신고 기록 저장 딕셔너리 초기화 (중복제거)
    records = {}
    for id in id_list:
        records[id] = set()
    # 신고 기록 저장
    for report in reports:
        user, reported_user = report.split(" ")
        records[reported_user].add(user)
    # 신고 기록이 k 이상인 경우, 메일 보내기
    for record in records.values():
        if len(record)>=k:
            for i in record:
                answer[id_list.index(i)]+=1
    return answer

case1_pred=solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)
case1_true=[2,1,1,0]
case2_pred=solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
case2_true=[0,0]

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")