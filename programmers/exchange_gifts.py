'''
가장 많이 받은 선물
link: https://school.programmers.co.kr/learn/courses/30/lessons/258712
'''

def solution(friends, gifts):
    # 선물 지수 표 위한 초기 설정
    num_friends=len(friends)
    friends_idx={friends[i]:i for i in range(num_friends)}
    gifts_exchange=[[0]*num_friends for _ in friends]
    gifts_score=[[0,0] for _ in friends]
    # 주고 받은 선물과 선물 지수 표
    for gift in gifts:
        from_gift, to_gift = gift.split(" ")
        gifts_exchange[friends_idx[from_gift]][friends_idx[to_gift]]+=1
        gifts_score[friends_idx[from_gift]][0]+=1
        gifts_score[friends_idx[to_gift]][1]+=1
    # 선물 지수 계산 및 가장 많은 선물을 받는 친구가 받을 선물의 수 return
    answer=0
    for i in range(num_friends):
        count_gifts=0
        for j in range(num_friends):
            if i!=j:
                give_gifts, receive_gifts = gifts_exchange[i][j], gifts_exchange[j][i]         
                # 더 많은 선물을 준 사람이 선물을 하나 받음
                if give_gifts!=receive_gifts and give_gifts-receive_gifts>0:
                    count_gifts+=1
                # 주고 받은 수가 같다면, 선물 지수가 더 큰사람이 선물을 하나 받음
                elif give_gifts==receive_gifts and gifts_score[i][0]-gifts_score[i][1]>gifts_score[j][0]-gifts_score[j][1]:
                    count_gifts+=1  
        if answer<count_gifts:
            answer=count_gifts
    return answer

print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])) #2
print(solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"])) #4
print(solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"])) #0