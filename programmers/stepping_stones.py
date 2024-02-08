def solution(distance, rocks, n):
    rocks.sort()
    answer = 0
    start, end = 0, distance
    
    while start <= end:
        mid=(start+end)//2
        prev_rock=0
        removed_rocks=0
        
        for rock in rocks:
            if rock - prev_rock < mid :
                removed_rocks += 1
            else:
                prev_rock = rock
        
        if distance - prev_rock < mid:
            removed_rocks += 1
        
        if removed_rocks <= n:
            answer=mid
            start=mid+1
        else:
            end = mid - 1   
    return answer

print(solution(25, [2,14,11,21,17], 2)) # 4