n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

def in_range(i, j):
    global n, m
    if 0 <= i and i < n:
        return 0 <= j and j < m
    return False

def can_go(i, j, visited):
    if in_range(i, j):
        return a[i][j] == 1 and visited[i][j] == False
    return False

def push(i, j, q, visited):
    q.append((i, j))
    visited[i][j] = True

def BFS():
    q = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    distance = [[0 for _ in range(m)] for _ in range(n)]
    dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]

    push(0, 0, q, visited)
    
    while q:
        i, j = q.popleft()
        for di, dj in zip(dis, djs):
            new_i = i + di
            new_j = j + dj
            if can_go(new_i, new_j, visited):
                push(new_i, new_j, q, visited)
                distance[new_i][new_j] = distance[i][j] + 1
    if distance[-1][-1] == 0:
        distance[-1][-1] = -1
        
    return distance
            
dist = BFS()
print(dist[-1][-1])


    