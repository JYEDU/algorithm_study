from my_answer.number_couple import solution

# 테스트 케이스
case1_X = "100"
case1_Y= "2345"
case1_answer = "-1"
case1_pred = solution(case1_X, case1_Y)

case2_X = "100"
case2_Y= "203045"
case2_answer = "0"
case2_pred = solution(case2_X, case2_Y)

case3_X = "100"
case3_Y= "123450"
case3_answer = "10"
case3_pred = solution(case3_X, case3_Y)

case4_X = "12321"
case4_Y= "42531"
case4_answer = "321"
case4_pred = solution(case4_X, case4_Y)

case5_X = "5525"
case5_Y= "1255"
case5_answer = "552"
case5_pred = solution(case5_X, case5_Y)

case6_X = "3403"
case6_Y= "13203"
case6_answer = "330"
case6_pred = solution(case6_X, case6_Y)

# 채점 결과
isanswer = [case1_pred==case1_answer, 
            case2_pred==case2_answer, 
            case3_pred==case3_answer, 
            case4_pred==case4_answer, 
            case5_pred==case5_answer, 
            case6_pred==case6_answer]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")