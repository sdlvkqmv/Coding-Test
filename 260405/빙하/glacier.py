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
    checks 
    1. in-range, 
    2. has visited or not
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
    dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]
    
    ice_count = count_ice(a)
    total_melted_count = 0

    while True:
        last_melted_count = 0
        visited = [[False for _ in range(m)] for _ in range(n)]
        push(0, 0, q, visited)
        ##print(time)
        #print(a)
        while q:
            i, j = q.popleft()

            for di, dj in zip(dis, djs):
                new_i = i + di
                new_j = j + dj

                if can_go(new_i, new_j, visited):
                    if a[new_i][new_j] == 0:
                        push(new_i, new_j, q, visited)

                    elif a[new_i][new_j] == 1:
                        total_melted_count += 1
                        last_melted_count += 1
                        visited[new_i][new_j] = True
                        a[new_i][new_j] = 0

                        if total_melted_count == ice_count:
                            return time + 1, last_melted_count
        time += 1


time, last_melted_count = BFS(water_idx)
print(time, last_melted_count)
