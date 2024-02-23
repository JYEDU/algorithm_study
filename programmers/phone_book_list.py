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