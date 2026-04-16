import sys
from collections import deque

# 방향: 1=상, 2=하, 3=좌, 4=우
DIR = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

# 1단계 우선순위 (현재 방향 기준: 직진, 좌회전, 우회전, 180도)
PREFERENCE = {
    1: [1, 3, 4, 2],
    2: [2, 4, 3, 1],
    3: [3, 2, 1, 4],
    4: [4, 1, 2, 3],
}

# 2단계 BFS 이동 우선순위: 좌, 하, 우, 상
BFS_PREF = [3, 2, 4, 1]


class GridManager:
    def __init__(self, n, grid):
        self.n = n
        self.grid = grid  # 0=바다, 1=암초, -1=방문됨

    def count_dirty_cell(self):
        return sum(row.count(0) for row in self.grid)

    def print_grid(self):
        for row in self.grid:
            print(' '.join(str(x) for x in row))


class Robot:
    def __init__(self, r, c, d, gm: GridManager):
        self.i = r
        self.j = c
        self.direction = d
        self.move_path = [(r, c)]
        self.gm = gm
        gm.grid[r][c] = -1

    def _in_bounds(self, ni, nj):
        return 0 <= ni < self.gm.n and 0 <= nj < self.gm.n

    def move(self):
        """한 스텝 이동. 인접 이동 가능하면 인접 이동, 아니면 BFS 호출.
        이동했으면 True, 더 이상 갈 곳 없으면 False."""
        # 현재 방향 기준 우선순위대로 인접 이동 시도
        for d in PREFERENCE[self.direction]:
            di, dj = DIR[d]
            ni, nj = self.i + di, self.j + dj
            if self._in_bounds(ni, nj) and self.gm.grid[ni][nj] == 0:
                self.i, self.j = ni, nj
                self.direction = d
                self.gm.grid[ni][nj] = -1
                self.move_path.append((ni, nj))
                return True

        # 인접 이동 불가 → BFS로 가장 가까운 미방문 바다로 이동
        return self.bfs()

    def bfs(self):
        """BFS로 (i, j, dist, direction) 큐에 저장하며 탐색"""
        n = self.gm.n
        grid = self.gm.grid

        visited = [[False] * n for _ in range(n)]
        visited[self.i][self.j] = True

        queue = deque()
        queue.append((self.i, self.j, 0, self.direction))

        # 후보: (dist, i, j, direction)
        candidates = []
        min_dist = float('inf')

        while queue:
            ci, cj, cd, cdir = queue.popleft()

            # 팝한 거리가 현재 최소보다 크면 더 볼 필요 없음
            if cd > min_dist:
                break

            # 좌, 하, 우, 상 순서로 탐색
            for d in BFS_PREF:
                di, dj = DIR[d]
                ni, nj = ci + di, cj + dj
                if not self._in_bounds(ni, nj):
                    continue
                if grid[ni][nj] == 1:
                    continue
                if visited[ni][nj]:
                    continue
                visited[ni][nj] = True

                if grid[ni][nj] == 0:
                    # 처음으로 닿는 미방문 바다 → 후보에 저장 (큐에는 안 넣음)
                    candidates.append((cd + 1, ni, nj, d))
                    if cd + 1 < min_dist:
                        min_dist = cd + 1
                else:
                    # 이미 방문한 바다(-1)는 계속 진행
                    queue.append((ni, nj, cd + 1, d))

        if not candidates:
            return False

        # 행 → 열 순 정렬 (거리는 전부 min_dist로 동일)
        candidates.sort(key=lambda x: (x[0], x[1], x[2]))
        _, ti, tj, tdir = candidates[0]

        self.i, self.j = ti, tj
        self.direction = tdir
        grid[ti][tj] = -1
        self.move_path.append((ti, tj))
        return True


def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    r = int(data[idx]); idx += 1
    c = int(data[idx]); idx += 1
    d = int(data[idx]); idx += 1
    grid = []
    for _ in range(N):
        row = [int(data[idx + k]) for k in range(N)]
        idx += N
        grid.append(row)

    gm = GridManager(N, grid)
    robot = Robot(r, c, d, gm)

    while gm.count_dirty_cell() > 0:
        if not robot.move():
            break

    out = '\n'.join(f'{ri} {ci}' for ri, ci in robot.move_path)
    print(out)


if __name__ == '__main__':
    main()