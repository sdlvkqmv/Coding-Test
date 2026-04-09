n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1

# Please write your code here.
# 꼭 한칸만 움직이는거는 아님  i * di , i * j
dis, djs = [0, -1, -1, 0, 1, 1, 1, 0, -1], [0, 0, 1, 1, 1, 0, -1, -1, -1]

def in_range(i, j):
    if 0 <= i and i < n:
        return 0 <= j and j < n

def get_available_points(start_point):
    '''
    시작점 받아서 
    1. 격자안에 있고, 2. 현재 숫자보다 큰 숫자 가진, 가능한 좌표 리턴
    '''
    moves = 1
    i, j = start_point
    move_number = move_dir[i][j]
    new_i, new_j = i, j

    available_points = []

    while True:
        new_i = i + dis[move_number] * moves
        new_j = j + djs[move_number] * moves

        if not in_range(new_i, new_j):
            break
        
        if num[new_i][new_j] <= num[i][j]:
            moves += 1

            continue
        
        available_points.append((new_i, new_j))
        moves += 1
    return available_points

result = 0

def find_maximum_moves(start_point, count_moves):
    global result
    result = max(result, count_moves)

    curr_i, curr_j = start_point
    #print(count_moves, start_point)

    next_available = get_available_points((curr_i, curr_j))
    #print(next_available)

    if len(next_available) == 0:
        result = max(result, count_moves)
        return
    
    for point in next_available:
        i2, j2 = point
        
        find_maximum_moves((i2, j2), count_moves + 1)

find_maximum_moves((r, c), 0)
#print(get_available_points((1,1)))
print(result)