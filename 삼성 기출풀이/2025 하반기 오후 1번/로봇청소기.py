# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''
# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
sys.stdin = open("../택배하차/input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
from collections import deque
######## 그리드 관리 ###########
class GridManager:
    def __init__(self, grid):
        self.grid = grid
        self.robots = [[False for _ in range(N)] for _ in range(N)]

    def stack_dust(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j] > 0:
                    curr_dust = self.grid[i][j]
                    self.grid[i][j] = curr_dust + 5

    def splash_dust(self):
        temp_grid = [[p for p in row] for row in self.grid]# 디버깅할때 list comprehension 스킵 하는법알아보기

        dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):

                ## 모든 깨끗한 격자에 대해 ##
                if self.grid[i][j] == 0:
                    surrounding_dust_sum = 0
                    for di, dj in zip(dis, djs):
                        newi = i + di
                        newj = j + dj
                        if self._in_range(newi, newj):

                            ## 물건이 없는 격자에 대해 ##
                            if self.grid[newi][newj] != -1:
                                surrounding_dust_sum += self.grid[newi][newj]
                    ## 먼지는 최대 100!!!!
                    temp_grid[i][j] = surrounding_dust_sum // 10

        #self.grid = [[p for p in row] for row in temp_grid] # 왜이거 안되지??
        for i in range(len(temp_grid)):
            for j in range(len(temp_grid)):
                #temp =d
                self.grid[i][j] = temp_grid[i][j]

    def _in_range(self, i, j):
        global N
        if 0 <= i < N:
            return 0 <= j < N
        return False

    def print_dust_sum(self):
        sum = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j] != -1: # 물건 없는 케이스에서 전체 합
                    sum += self.grid[i][j]
        print(sum)

######## 그리드 관리 ###########



######### 로봇 #############
class Robot:
    def __init__(self, k, i, j):
        self.k = k
        self.i = i
        self.j = j
        self.dis = [-1, 0, 0, 1]
        self.djs = [0, -1, 1, 0]

    def move(self):
        if grid_manager.grid[self.i][self.j] > 0:
            return
        q= deque()
        visited = [[False for _ in range(N)] for _ in range(N)]
        min_dust_dist = float('inf')
        self._push(self.i, self.j, 0, q, visited) #visited 바꾸고, q에다 append
        move_points = []      #후보 움직일 곳 저장

        while q:
            i, j, dist = q.popleft()
            if dist >= min_dust_dist:
                break

            for di, dj in zip(self.dis, self.djs): #이 루프 끝나면 q에 다음 갈수 있는곳, move_points에 먼지 있는 곳 저장 -> move_points에 하나라도 저장되면 다음 while 루프에서 탈출
                ni = i + di
                nj = j + dj
                if self._can_go(ni, nj) and not visited[ni][nj]: # 가는 자리가 격자 안이고, 로봇, 물건이 없다면
                    visited[ni][nj] = True
                    if grid_manager.grid[ni][nj] > 0: #갈 자리가 먼지가 있는 곳이면
                        move_points.append((ni, nj)) # 후보 이동자리에 추가하고, 다음 이동은 안하도록 추가하지 않음
                        if min_dust_dist > dist + 1:
                            min_dust_dist = dist + 1
                    else: #먼지가 없는 곳이면 다음 움직이는 후보로 추가
                        if dist + 1 <= min_dust_dist:
                            self._push(ni, nj, dist + 1, q, visited)
        if move_points:
            move_points.sort(key= lambda x : x) # 이동거리 별로 탐색 끝났으면 move_points에 저장된 점들 정렬
            grid_manager.robots[self.i][self.j] = False
            self.i, self.j = move_points[0] #가장 우선순위로 이동
        grid_manager.robots[self.i][self.j] = True

    def _push(self, i, j, dist, q, visited):
        if self._in_range(i, j):
            q.append((i, j, dist))
            visited[i][j] = True

    def _in_range(self, i, j):
        global N
        if 0 <= i < N:
            return 0 <= j < N
        return False

    def _can_go(self, i, j):
        if self._in_range(i, j):
            if grid_manager.grid[i][j] != -1 and not grid_manager.robots[i][j]: #물건이랑 로봇위치가 아니면 #TODO
                return True
        return False

    def clean(self):
        dis, djs = [0, -1, 0, 1], [-1, 0, 1, 0] # 무시할 순서: 좌상우하 순서

        max_sum = 0
        max_clean_cell = []

        for _ in range(4): #3방향 어떻게 표현하지? -> # '_' 하나마다 제외할 방향임
            clean_cell = [(self.i, self.j)]
            m = 0 #무시할 방향
            for di, dj in zip(dis, djs):
                if _ != m:
                    cleani = self.i + di
                    cleanj = self.j + dj
                    if self._in_range(cleani, cleanj):
                        clean_cell.append((cleani, cleanj))
                m += 1

            curr_sum = self._get_cleanble_dust_sum(clean_cell)
            if max_sum < curr_sum:
                max_sum = curr_sum
                max_clean_cell = clean_cell

        for i, j in max_clean_cell:
            if grid_manager.grid[i][j] > 0:
                curr_dust = grid_manager.grid[i][j]
                grid_manager.grid[i][j] = max(0, curr_dust - 20)


    def _get_cleanble_dust_sum(self, clean_cell : list):
        '''
        닦을칸 리스트 받아서 최대 청소 가능 값 리턴
        '''
        clean_sum = 0
        for i, j in clean_cell:
            cell_dust = grid_manager.grid[i][j]
            if cell_dust > 0:
                clean_sum += min(20, cell_dust)
        return clean_sum


################# 로봇 ##############


######## 메인 실행부 #############
for test_case in range(1, T + 1):
    N, K, L = map(int, input().split())
    grid_manager = GridManager([[0 for _ in range(N)] for _ in range(N)])
    robots = []

    for _ in range(N):
        grid_manager.grid[_] = list(map(int, input().split()))

    for _ in range(K):
        i, j = list(map(int, input().split()))
        i -= 1
        j -= 1

        grid_manager.robots[i][j] = True
        robots.append(Robot(_, i, j))

    for _ in range(L):
        for robot in robots:
            robot.move()   ## 여기까지 동작

        for robot in robots:
            robot.clean()

        grid_manager.stack_dust() #디버깅할 때 실행 전으로 돌아가는 법 알아보기

        grid_manager.splash_dust()

        grid_manager.print_dust_sum()





