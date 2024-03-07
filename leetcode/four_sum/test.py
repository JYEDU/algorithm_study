from my_answer.four_sum import Solution

solution = Solution()
test_cases=[]

#test_case1
input_nums = [1,0,-1,0,-2,2]
input_target = 0
expected_output = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
actual_output = solution.fourSum(input_nums, input_target)
test_cases.append(expected_output==actual_output)

#test_case2
input_nums = [2,2,2,2,2]
input_target = 8
expected_output = [[2,2,2,2]]
actual_output = solution.fourSum(input_nums, input_target)
test_cases.append(expected_output==actual_output)

# 채점 결과
print(len(test_cases), "개 중에", test_cases.count(True),"개 성공")