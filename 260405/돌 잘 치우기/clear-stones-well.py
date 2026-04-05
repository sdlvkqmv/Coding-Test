n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r = []
c = []
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

# Please write your code here.
from collections import deque

start_points = [(i, j) for i, j in zip(r, c)]
#m개 치워서 최대한 많이 도달
def in_range(i, j):
    '''
    옮길 때 최우선으로 체크
    '''
    if 0 <= i and i < n:
        return 0 <= j and j < n
    return False

def can_go(grid_case, i, j, visited: list):
    '''
    Returns: True if 갈수 있는길, 'stone' if 돌덩이 있으면
    '''
    if in_range(i, j):
        if visited[i][j] == False and grid_case[i][j] == 0:
            return True
    return False

def push(i, j, visited: list, q: deque()):
    if in_range(i, j):
        q.append((i, j))
        visited[i][j] = True

def get_stones_id():
    '''
    returns stone ids in list
    '''
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                stones_idx_list.append((i, j))


def get_stone_combination(n, comb):
    '''
    Saves possible combinations to stone_combination
    '''
    global m
    #base
    if n == len(stones_idx_list):
        #조합 길이 만족시
        if len(comb) == m:
            temp = [i for i in comb] #pop 때문에 스냅샷을 찍어놔야함
            stone_combination.append(temp)
        return
    #resursive
    #1. 포함
    comb.append(stones_idx_list[n])
    get_stone_combination(n + 1, comb)

    #2. 포함 X
    comb.pop()
    get_stone_combination(n + 1, comb)


def get_grid_case(i):
    '''
    Gets: i (index for stone combination)
    returns grid case for single cleaned stone combination
    '''

    grid_case = [[n for n in row] for row in grid]

    for n, m in stone_combination[i]:
        grid_case[n][m] = 0
    return grid_case


def BFS(grid_case: list, start_points: list):
    reachable_count = len(start_points)

    q = deque()
    dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]
    visited = [[False for _ in range(n)] for _ in range(n)]
    for point in start_points:
        push(point[0], point[1], visited, q)

    while q:
        i, j = q.popleft()
        for di, dj in zip(dis, djs):
            new_i = i + di
            new_j = j + dj
            if can_go(grid_case, new_i, new_j, visited):
                push(new_i, new_j, visited, q)
                reachable_count += 1
    return reachable_count

###########
stones_idx_list = []
get_stones_id()
#print(stones_idx_list)

stone_combination = []
get_stone_combination(0, [])
#print(stone_combination)

for i in range(len(stone_combination)):
    #print(stone_combination[i])
    grid_case = get_grid_case(i)
    #print(grid_case)
    max = 0
    reachable = BFS(grid_case, start_points)
    if max < reachable:
        max = reachable

print(max)