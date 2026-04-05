n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

#물에 닿아있는 빙하 녹음
#빙하로 둘러싸인 물은 빙하를 못녹임
#빙하 전부 녹는데 걸리는 시간, 마지막으로 녹은 크기
def get_water_idx(a : list):
    water_idx = []
    for i, row in enumerate(a):
        for j, value in enumerate(row):
            if value == 0:
                water_idx.append((i, j))

    return water_idx

water_idx = get_water_idx(a)
#print(water_idx)

def in_range(i, j):
    global n, m
    #print(n, m)
    if 0 <= i and i < n:
        return 0 <= j and j < m
    return False

def can_melt(i, j):
    '''
    Input : ice's idx
    Returns if the water can melt the near ice
    '''
    pass

def check_end_of_grid(k, p):
    global n, m
    if k == 0 or k == n - 1:
        return True
    elif p == 0 or p == m - 1:
        return True
    return False

def get_water_not_surrounded():
    '''
    BFS
    Checks waters not surrounded with ice
    Returns grid of waters not surrounded(True)
    '''
    q = deque()
    dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]
    _visited = [[False for _ in range(m)] for _ in range(n)]

    q.append((0,0))

    while q:
        i, j = q.popleft()
        for di, dj in zip(dis, djs):
            new_i = i + di
            new_j = j + dj
            if in_range(new_i,new_j):
                if _visited[new_i][new_j] == False and a[new_i][new_j] == 0:
                    q.append((new_i, new_j))
                    _visited[new_i][new_j] = True

    return _visited

                

def push(i, j, q: deque(), visited: list):
    '''
    1. Push into queue
    2. Change visited to True
    3. Melt if ice
    '''
    q.append((i, j))
    visited[i][j] = True
    a[i][j] = 0

def can_go(i, j, visited):
    '''
    checks 1. in-range, 2. has visited or not
    '''
    if in_range(i, j):
        if visited[i][j] == False:
            return True
    return False

def count_ice(a):
    '''
    Returns number of ice remaining
    '''
    count = 0
    for i, row in enumerate(a):
        for j, value in enumerate(row):
            if value == 1:
                count += 1
    return count

def BFS(water_idx: list):
    time = 0
    q = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]

    original_members = []
    new_members = []
    melted_count = 0

    water_not_surrounded = get_water_not_surrounded()

    for i, water in enumerate(water_idx):
        if water_not_surrounded[water[0]][water[1]]:
            push(water[0], water[1], q, visited)
            original_members.append((water[0], water[1]))

    while q:

        if len(original_members) == 0: # 오리지널 멤버들이 다 빠짐 -> 하나의 시퀀스 끝
            original_members = [member for member in new_members] #오리지널 멤버를 이제 새 멤버로 교체
            new_members = []
            time += 1
            melted_count = 0

        i, j = q.popleft()

        for di, dj in zip(dis, djs):
            new_i = i + di
            new_j = j + dj
            if can_go(new_i, new_j, visited):
                if a[new_i][new_j] == 1:
                    melted_count += 1
                push(new_i, new_j, q, visited)
                new_members.append((new_i, new_j)) #새로운 멤버에 추가
                if count_ice(a) == 0:
                    return time + 1, melted_count # 시간 늘리는 분기 오기 전이니까 그전에 time늘려주고

        original_members.pop() #하나의 점에 대해 breadth  끝나면 pop


    return time, melted_count

time, melted_count = BFS(water_idx)
print(time, melted_count)
