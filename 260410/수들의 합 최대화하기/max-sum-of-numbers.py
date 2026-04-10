n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 색칠된 칸에 적힌 수의 합의 최댓값

# 1. 가능한 색칠 칸 구하기 
# 2. 최댓값 구해서 갱신

visited_row, visited_col = [False for _ in range(n)], [False for _ in range(n)]

colored_points = []
maxi = 0

def get_sum():
    sum = 0
    for p in colored_points:
        sum += grid[p[0]][p[1]]
    return sum

def find_color(count):
    global maxi
    if count == n:
        maxi = max(maxi, get_sum())
        return

    for i in range(n):
        if not visited_row[i]: # 이미 방문했던 열과 행은 방문하면 안됨
            for j in range(n):
                if not visited_col[j]:
                    colored_points.append((i, j))
                    visited_row[i], visited_col[j] = True, True 
                    find_color(count + 1)
                    
                    colored_points.pop()
                    visited_row[i], visited_col[j] = False, False

find_color(0)

print(maxi)