n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

#K 최대 3개니까 괜찮을듯
def get_combinations(i, curr_comb, n, k):
    #Base case
    #print(curr_comb)
    if len(curr_comb) == k:
        temp = [i for i in curr_comb]
        comb_result.append(temp)
        return
    elif i == n:
        return

    #Recusrsive
    curr_comb.append(i)
    get_combinations(i + 1, curr_comb, n, k)
    
    curr_comb.pop()
    get_combinations(i + 1, curr_comb, n, k)

def get_combinations_idx(comb_result, n):
    '''
    Converts int -> (i, j)
    '''
    for comb in comb_result:
        curr_comb = []
        for city in comb:
            i , j = city // n, city % n
            curr_comb.append((i, j))
        
        comb_ids.append(curr_comb)
        
#get_combinations_idx(comb_result, n)
#print(len(comb_ids))

def in_range(i, j):
    global n

    if 0 <= i and i < n:
        return 0 <= j and j < n
    return False

def can_go(i, j, new_i, new_j, visited: list):
    '''
    Checks
    1. in range
    2. not visited
    3. diff is D ~ D
    '''
    global u, d
    if in_range(new_i, new_j) and not visited[new_i][new_j]:
        diff = abs(grid[i][j] - grid[new_i][new_j])
        return u <= diff and diff <= d

    return False

def push(i, j, q : deque(), visited: list):
    q.append((i, j))
    visited[i][j] = True

def BFS(comb):

    q = deque()
    total_move = 0
    dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]

    moved = [[False for _ in range(n)] for _ in range(n)] #for counting
    
    for city in comb:
        visited = [[False for _ in range(n)] for _ in range(n)] # for BFS
        push(city[0], city[1], q, visited)
        total_move += 1
        moved[city[0]][city[1]] = True

        while q:
            #print(total_move)
            i, j = q.popleft()
            for di, dj in zip(dis, djs):
                new_i = i + di
                new_j = j + dj
                
                if can_go(i, j, new_i, new_j, visited):
                    push(new_i, new_j, q, visited)
                    if moved[new_i][new_j] == False:
                        moved[new_i][new_j] = True
                        total_move += 1    
    
    return total_move
        
comb_result = []
total_cities = n ** 2
get_combinations(0, [], total_cities, k)

comb_ids = []
get_combinations_idx(comb_result, n) # -> comb_ids

max_visit = 0
for comb in comb_ids:
    #print(comb)
    curr_visit_count = BFS(comb)
    #print(curr_visit_count)
    if max_visit < curr_visit_count:
        max_visit = curr_visit_count

print(max_visit)
