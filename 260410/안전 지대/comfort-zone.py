n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# K값 포문으로 늘려가기
# 각 포문 안에서  DFS

safe = [[True for _ in row] for row in grid] # True = Safe

def update_safe_building(K, safe_building):
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if grid[i][j] <= K and safe[i][j]:
                safe[i][j] = False
                safe_building -= 1 #이부분에서 이미 false였던 애들도 false 로 바뀌면서 카운팅이 중복으로 들어감

    return safe_building


def in_range(i,j):
    if 0 <= i and i < n:
        return 0 <= j and j < m
    return False

def can_go(i, j):
    if in_range(i, j) and not visited[i][j] and safe[i][j]:
        return True
    return False

dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]

def DFS(i, j):
    for di, dj in zip(dis, djs):
        new_i = i + di
        new_j = j + dj
        if can_go(new_i, new_j):
            visited[new_i][new_j] = True
            DFS(new_i, new_j)
    

max_regions = 0
safe_buildings = n * m
K = 1
max_K = 1

while safe_buildings > 0:
    safe_buildings = update_safe_building(K, safe_buildings)
    #print(safe_buildings)
    
    #Init for each K
    safe_regions = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if can_go(i, j):
                ##print("Safe Map")
                #print(safe)

                #print(i, j)
                safe_regions += 1
                DFS(i, j)
    #print(f"K : {K}, safe_regions : {safe_regions}, safe_buildings: {safe_buildings}")
    
    if max_regions < safe_regions:
        max_regions = safe_regions
        max_K = K
    K += 1
    #print()

print(max_K, max_regions)
