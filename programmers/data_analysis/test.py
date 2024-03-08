from my_answer.data_analysis import solution

# 테스트 케이스
case1_data =  [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
case1_ext = "date"
case1_val_ext = 20300501
case1_sort_by = "remain"
case1_answer = [[3,20300401,10,8],[1,20300104,100,80]]
case1_pred = solution(case1_data, case1_ext, case1_val_ext, case1_sort_by)

# 채점 결과
isanswer = [case1_pred==case1_answer]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")