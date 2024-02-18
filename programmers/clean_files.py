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