'''
바탕화면 정리
link: https://school.programmers.co.kr/learn/courses/30/lessons/161990
'''

def solution(wallpaper):
    find_i=[]
    find_j=[]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j]=="#":
                find_i.append(i)
                find_j.append(j)
    answer=[min(find_i), min(find_j), max(find_i)+1, max(find_j)+1]
    return answer

# 테스트 케이스
case1_pred=solution([".#...", "..#..", "...#."])
case1_true=[0, 1, 3, 4]

case2_pred=solution(["..........", ".....#....", "......##..", "...##.....", "....#....."])
case2_true=[1, 3, 5, 8]

case3_pred=solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."])
case3_true=[0, 0, 7, 9]

case4_pred=solution(["..", "#."])
case4_true=[1, 0, 2, 1]

# 채점 결과
isanswer = [case1_pred==case1_true, case2_pred==case2_true, case3_pred==case3_true, case4_pred==case4_true]
#print(isanswer.count(True),"/",len(isanswer))
print(len(isanswer), "개 중에", isanswer.count(True),"개 성공")