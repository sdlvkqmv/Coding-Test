n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

def in_range(i, j):
    '''
    입력한 좌표가 격자 벗어났는지
    '''
    global n, m

    if i < 0 or i >= n:
        return False
    elif j < 0 or j >= m:
        return False
    else:
        return True



def can_go(i, j):
    '''
    입력된 좌표가 갈수 있는지 체크
    '''
    if in_range(i, j):
        if a[i][j] == 1 and visited[i][j] == False:
            return True
    
    else:
        return False

def push(i, j):
    '''
    q에 푸시하는 함수
    visited 바꿔주고 푸시해줌
    '''

    q.append((i, j))
    visited[i][j] = True
    return

#변수 초기화
visited = [[False for _ in range(m)] for _ in range(n)]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
q = deque()


def bfs():
    push(0,0)
    while q:
        #print(q)
        i, j = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_i = i + dx
            new_j = j + dy
            
            if can_go(new_i, new_j):
                push(new_i, new_j)

        #print(i,j)

bfs()

if visited[n - 1][m - 1]:
    print(1)
else: 
    print(0)