'''
기사단원의 무기
link: https://school.programmers.co.kr/learn/courses/30/lessons/136798
'''
import math
def solution(number, limit, power):
    # 기사단원번호들의 약수 개수
    def common_divisor(number):
        out=[]
        for num in range(1,number+1):
            count=0
            max_value=int(math.sqrt(num))
            for i in range(1, max_value+1):
                if num%i==0 and i**2==num:
                    count+=1
                elif num%i==0:
                    count+=2
            out.append(count)
        return out
    powers=common_divisor(number)
    # 공격력의 제한수치와 비교
    answer=0
    for i in powers:
        if i>limit:
            answer+=power
        else:
            answer+=i
    return answer