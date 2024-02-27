'''
성격 유형 검사하기
link: https://school.programmers.co.kr/learn/courses/30/lessons/118666

지표: 1번(R/T), 2번(C/F), 3번(J/M), 4번(A/N)
지표(A/B)에 대한 점수: 1(A+3), 2(A+2), 3(A+1), 4(0), 5(B+1), 6(B+2), 7(B+3)
'''

def solution(surveys, choices):
    # 성격 유형 점수 계산
    table = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    nos = len(surveys)
    for num in range(nos):
        score=choices[num]
        type1=surveys[num][0]
        type2=surveys[num][1]
        if score==1: 
            table[type1]+=3            
        elif score==2:
            table[type1]+=2  
        elif score==3:
            table[type1]+=1             
        elif score==5:
            table[type2]+=1             
        elif score==6:        
            table[type2]+=2    
        elif score==7:    
            table[type2]+=3
    # 성격 유형 결과    
    answer = ''
    if table['R']>=table['T']: answer+='R'
    else: answer+='T'
    if table['C']>=table['F']: answer+='C'
    else: answer+='F'
    if table['J']>=table['M']: answer+='J'
    else: answer+='M'
    if table['A']>=table['N']: answer+='A'
    else: answer+='N'    
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])) #"TCMA"
print(solution(["TR", "RT", "TR"], [7, 1, 3])) #"RCJA"
