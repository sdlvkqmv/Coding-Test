n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
def in_range(i, j):
    if 0 <= i and i < n:
        return 0 <= j and j < n
    return False

def can_go(i, j):
    return visited[i][j] == False and grid[i][j] == 0

def push(i, j):
    global count
    #print(visited)
    if in_range(i, j) and can_go(i, j):
        q.append((i, j))   

        visited[i][j] = True
        count += 1
    return

dis, djs = [1, 0, -1, 0], [0, 1, 0, -1]

def bfs(point):
    i, j = point
    #print(i, j)
    #print(visited[i - 1][j - 1])

    push(i - 1, j - 1)
    
    while q:
        i, j = q.popleft()

        for di, dj in zip(dis, djs):
            new_i = i + di
            new_j = j + dj

            push(new_i, new_j)

from collections import deque
q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
count = 0

for point in points:
    bfs(point)

print(count)
    