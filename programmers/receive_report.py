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

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)) #[2,1,1,0]
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)) #[0,0]
