n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
def in_range(i, j):
    global n
    if 0 <= i and i < n:
        return 0 <= j and j < n
    return False

def can_go(x, i, j):
    if in_range(i, j):
        return x > grid[i][j] and visited[i][j] == False

def push(i, j):
    q.append((i, j))
    visited[i][j] = True

def BFS(i, j):
    '''
    이게 한번의 움직임을 찾는것 -> k번 반복
    Returns: 
    move_result
    '''

    push(i, j)

    max_value = [(-1, (-1, -1))] #for managing largest movable point


    dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]

    point_value = grid[i][j] #for can_go logic
    #print(point_value)


    while q:
        #print("queue:", q)
        i, j = q.popleft()

        for di, dj in zip(dis, djs):
            new_i, new_j = i + di, j + dj
            if can_go(point_value, new_i, new_j):
                new_value = grid[new_i][new_j]
                push(new_i, new_j)
                
                if max_value[0][0] < new_value:
                    max_value = [(new_value, (new_i, new_j))]
                elif max_value[0][0] == new_value:  #같은 최댓값있는 경우 처리
                    max_value.append((new_value, (new_i, new_j)))
            #print("max", max_value)
    
    #print("max before sort", max_value)
    max_value.sort(key = lambda x: x[1]) #최댓값 여러개인 경우 row, index 순으로 오름차순
    #print("max after sort", max_value)

    move_result = max_value[0][1] #tuple (i, j)

    return(move_result)

from collections import deque
q = deque()

r -= 1
c -= 1

for _ in range(k):
    visited = [[False for _ in range(n)] for _ in range(n)]

    r, c = BFS(r, c)
    #print(f"after {_} times", r, c)

#최종 결과: K번 반복한 후 위치
print(r + 1, c + 1)