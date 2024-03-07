'''
전화번호 목록
https://school.programmers.co.kr/learn/courses/30/lessons/42577
'''

def solution(phone_book):
    phone_book=sorted(phone_book)
    num=len(phone_book)
    for i in range(num-1):
        if phone_book[i+1].startswith(phone_book[i]):
            for j in range(i+1,num): 
                if phone_book[j].startswith(phone_book[i]):                
                    return False
    return True

# 테스트 케이스
case1_pred=solution(["119", "97674223", "1195524421"])
case1_true=False

case2_pred=solution(["123", "456", "789"])
case2_true=True

case3_pred=solution(["12", "123", "1235", "567", "88"])
case3_true=False

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true, case3_pred==case3_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")