n = int(input())
grid = [list(input()) for _ in range(n)]

# Please write your code here.
#S에서 시작, 최소 3개 수집해서 E에 도달
#번호 증가하는 순서로 수집해야함
#지나가도 수집 안해도됨
#두번 지나가도됨

#1. 증가하는 순서 동전 조합 구하기  <- 같은 곳 도달 가능, 지나가도 안주워도된다는 점에서 착안
# 2. 각 조합에 따라 (최소?) 경로 설정
# 3. 최소 이동거리 출력

coins = []
for i, row in enumerate(grid):
    for j , val in enumerate(row):
        if val == 'S':
            S = (i,j)
        elif val == 'E':
            E = (i, j)
        elif val != '.':
            coins.append((i, j))

coins.sort(key = lambda x : grid[x[0]][x[1]])
#print(coins, S, E)

result = float('inf')
combs = []

def get_coins_combs(curr_i, count):
    global S, E, result

    if count == 3:
        path = find_min_path(S, E, combs)
        result = min(path, result)
        return
    
    elif curr_i == len(coins):
        return

    combs.append(coins[curr_i])
    get_coins_combs(curr_i + 1, count + 1)
    combs.pop()
    get_coins_combs(curr_i + 1, count)
    
def find_min_path(S, E, combs):
    path = 0
    curr_i, curr_j = S

    for point in combs:
        path += abs(curr_i - point[0]) + abs(curr_j - point[1])
        curr_i, curr_j = point[0], point[1]

    path += abs(curr_i - E[0]) + abs(curr_j - E[1])

    return path

get_coins_combs(0, 0)

if result == float('inf'):
    print(-1)
else:
    print(result)