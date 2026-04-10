n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 상하좌우 adjacent 같은 숫자 -> 하나의 블럭 
# 칸수 4개이상 -> 터짐

#출력 : (터지게 되는 불럭 개수) (가장 큰 블럭 크기)

# 움직이는 기준 : 같은 숫자가 옆에 있다

### BFS 풀이 ###

def in_range(i, j):
    if 0 <= i and i < n:
        return 0 <= j and j < n

    return False

def can_go(i, j):
    if in_range(i, j) and not visited[i][j]:
        return True
    return False


def BFS(i, j):
    global block_size 
    
    for di, dj in zip(dis, djs):
        new_i = i + di
        new_j = j + dj

        if can_go(new_i, new_j) and grid[i][j] == grid[new_i][new_j]:
            visited[new_i][new_j] = True
            block_size += 1
            BFS(new_i, new_j)

visited = [[False for _ in range(n)] for _ in range(n)]
dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]

num_explosion = 0
max_blocks = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            block_size = 1
            visited[i][j] = True
            BFS(i, j)
            max_blocks = max(block_size, max_blocks)
            if block_size >= 4:
                num_explosion += 1

print(num_explosion, max_blocks)

##########################
#### BFS 풀이 ########
def in_range(i, j):
    if 0 <= i and i < n:
        return 0 <= j and j < n

    return False

def can_go(i, j):
    if in_range(i, j) and not visited[i][j]:
        return True
    return False

def push(i, j):
    q.append((i, j))
    visited[i][j] = True

from collections import deque
def BFS():
    global block_size

    while q:
        i, j = q.popleft()
        for di, dj in zip(dis, djs):
            new_i = i + di
            new_j = j + dj
            if can_go(new_i, new_j) and grid[i][j] == grid[new_i][new_j]:
                push(new_i, new_j)
                block_size += 1

visited = [[False for _ in range(n)] for _ in range(n)]
dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]

num_explosion = 0
max_blocks = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            block_size = 1
            q = deque()
            push(i, j)
            BFS()
            max_blocks = max(block_size, max_blocks)
            if block_size >= 4:
                num_explosion += 1

print(num_explosion, max_blocks)
