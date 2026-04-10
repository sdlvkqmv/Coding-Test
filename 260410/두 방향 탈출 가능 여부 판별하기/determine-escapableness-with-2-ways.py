n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False for _ in range(n)] for _ in range(m)]

def in_range(i, j):
    global n, m
    if 0 <= i and i < n:
        return 0 <= j and j < m
    return False

def can_go(i, j):
    if in_range(i, j):
        return grid[i][j] == 1
    return False

def print_v():
    for row in visited:
        print(row)

dis, djs = [1, 0], [0, 1]

def DFS(i, j):
    #print(visited)
    global n, m

    for di, dj in zip(dis, djs):
        new_i = i + di
        new_j = j + dj
        if can_go(new_i, new_j):
            if not visited[new_i][new_j]:
                visited[new_i][new_j] = True
                DFS(new_i, new_j)

DFS(0,0)

print(int(visited[n - 1][m - 1]))