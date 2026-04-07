n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
#모든 폭탄 놓인 곳에 대해 종ㄹㅍ별로 터뜨리고, 초토화 세고, 최대 초토화 출력
#폭탄 터진곳도 초토화임
#1. 폭탄 좌표 구하기 완료
#2. 폭탄 좌표 별로 조합 구하기
    # 2-1. 조합 나왔으면 함수 호출해서 바로 초토화 면적 구하기

bomb_explosions = [
    ([-2, -1,0, 1, 2], [0, 0, 0, 0, 0]),
    ([1, -1,0, 0, 0], [0, 0,0, 1, -1]),
    ([1, -1,0, -1, 1], [1, -1,0, 1, -1])]

#print(bomb_explosions[0][0], bomb_explosions[0][1])

bombs= []
for i, row in enumerate(grid):
    for j, value in enumerate(row):
        if value == 1:
            bombs.append((i, j))
            #오름차순으로 정렬돼있음 -> bomb_type이랑 안맞춰도됨

def in_range(i, j):
    global n
    if 0 <= i and i < n:
        return 0 <= j and j < n

def count_destroyed(bomb_type:list):
    '''
    폭탄 종류(x,x,x) 입력
    초토화 개수 리턴
    '''
    count = 0
    grids_destroyed = [[False for _ in range(n)] for _ in range(n)]
    
    for coord, type in zip(bombs, bomb_type):
        i, j = coord
        dis, djs = bomb_explosions[type][0], bomb_explosions[type][1]

        for di, dj in zip(dis, djs):
            new_i = i + di
            new_j = j + dj
            if not in_range(new_i, new_j):
                continue
            elif not grids_destroyed[new_i][new_j]:
                grids_destroyed[new_i][new_j] = True
                count += 1

    return count

max = 0

def find_bomb_combinations(num_bomb, combs):
    '''
    num_bomb(int) : 필요한 폭탄 개수
    combs(list): 현재 폭탄 조합
    리턴없이 글로벌 max 값 바꿔줌
    '''
    global max
    #종료 조건 : 폭탄 종류 다 채워졌을 때
    if len(combs) == num_bomb:
        #print(combs)
        count = count_destroyed(combs)
        if max < count:
            max = count
        return
    
    for type in range(3):
        combs.append(type)
        find_bomb_combinations(num_bomb, combs)
        combs.pop()

#print(len(bombs))
find_bomb_combinations(len(bombs), [])
print(max)
