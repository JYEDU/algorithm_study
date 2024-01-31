from collections import deque

def dfs(graph, current, visited):
    visited[current] = True 
    print(current, end=' ') 
    for i in graph[current]: 
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True 
    while queue:    
        current = queue.popleft()   
        print(current, end=' ')     
        for i in graph[current]:    
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph=[
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
    ]

visited = [False] * 9 
print('DFS :', end=' ')
dfs(graph, 1, visited)  
# 1 2 7 6 8 3 4 5 

visited = [False] * 9 
print('BFS :', end=' ')
bfs(graph, 1, visited)
# 1 2 3 8 7 4 5 6