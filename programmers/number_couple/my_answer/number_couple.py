def solution(X, Y):
    # X와 Y의 각 자리 숫자의 등장 횟수를 세어 배열에 저장
    count_X = [0] * 10
    count_Y = [0] * 10
    for digit in X:
        count_X[int(digit)] += 1
    for digit in Y:
        count_Y[int(digit)] += 1
    
    # 공통으로 등장하는 숫자들을 찾아 저장
    common_digits = []
    for i in range(10):
        common_digits.append(min(count_X[i], count_Y[i]))
    
    # 공통으로 등장하는 숫자가 없다면 -1을 반환
    if sum(common_digits) == 0:
        return "-1"
    
    # 가장 큰 수를 만들기
    result = ""
    for i in range(9, -1, -1):
        result += str(i) * common_digits[i]
    
    # 모든 숫자가 0으로만 이루어져 있다면 0을 반환
    if result == "0" * len(result):
        return "0"
    
    return result

