n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 시작점 여러개 <- 포문으로 돌리기
# 방문할수 있는데 없으면 다음 시작점으로

visited  = [[False for _ in range(n)] for _ in range(n)]

def in_range(i, j):
    if 0 <= i and i < n:
        return 0 <= j and j < n
    return False

def can_go(i, j):
    if in_range(i, j):
        return grid[i][j] == 1
    return False

num_towns = 0
population = []

dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]


def DFS(i, j):
    global pops
    for di, dj in zip(dis, djs):
        new_i = i + di
        new_j = j + dj
        if can_go(new_i, new_j) and not visited[new_i][new_j]:
            visited[new_i][new_j] = True
            pops += 1
            DFS(new_i, new_j)

for i in range(n):
    for j in range(n):
        if can_go(i, j) and not visited[i][j]:
            #print(i, j)
            num_towns += 1
            pops = 1
            visited[i][j] = True
            DFS(i, j)
            population.append(pops)

population.sort()

print(num_towns)
for i in population:
    print(i)            