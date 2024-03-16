"""
키패드 누르기
link: https://school.programmers.co.kr/learn/courses/30/lessons/67256
"""

def solution(numbers, hand):
    keypad={1:[0,0], 2:[0,1], 3:[0,2],
            4:[1,0], 5:[1,1], 6:[1,2],
            7:[2,0], 8:[2,1], 9:[2,2],
            0:[3,1]}
    left_position, right_position = [3,0], [3,2]
    answer = ''
    for num in numbers:
        # 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용
        if num in [1,4,7]:
            answer+="L"
            left_position=keypad[num]
        #오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용    
        elif num in[3,6,9]:
            answer+="R"
            right_position=keypad[num]
        # 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때
        else:
            # 더 가까운 엄지 손가락 사용을 위한 거리 계산
            left_distance=abs(left_position[0]-keypad[num][0])+abs(left_position[1]-keypad[num][1])
            right_distance=abs(right_position[0]-keypad[num][0])+abs(right_position[1]-keypad[num][1])
            # 왼손 엄지손가락이 더 가까운 경우
            if left_distance<right_distance:
                answer+="L"
                left_position=keypad[num]
            # 오른손 엄지손가락이 더 가까운 경우
            elif left_distance>right_distance:
                answer+="R"
                right_position=keypad[num]
            # 두 엄지손가락의 거리가 같은 경우
            else:
                # 왼손잡이는 왼손 엄지손가락 사용
                if hand=="left":
                    answer+="L"
                    left_position=keypad[num]
                # 오른손잡이는 오른손 엄지손가락 사용
                elif hand=="right":
                    answer+="R"
                    right_position=keypad[num]
    return answer


# 테스트 케이스
case1_numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
case1_hand="right"
case1_result="LRLLLRLLRRL"
case1_pred=solution(case1_numbers, case1_hand)		

case2_numbers=[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
case2_hand="left"
case2_result="LRLLRRLLLRR"
case2_pred=solution(case2_numbers, case2_hand)

case3_numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
case3_hand="right"
case3_result="LLRLLRLLRL"
case3_pred=solution(case3_numbers, case3_hand)

# 채점 결과
isanswer = [case1_pred==case1_result, case2_pred==case2_result, case3_pred==case3_result]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")