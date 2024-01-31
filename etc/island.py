def dfs(x, y):
    # N X M, no wall(0), wall(1)
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
    
graph=[
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
    ]

n, m = len(graph), len(graph[0])

outs=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            outs+=1

print(outs)
