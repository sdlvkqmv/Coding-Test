n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 1. 가능한 모든 조합에서
# 2.  최솟값구해서 최댓값 업데이트

ans = 0
visited_cols = [False for _ in range(n)]

def find_min(count, nums_min):
    global ans
    if count == n:
        ans = max(nums_min, ans)
        return
    
    for row in range(n):
        for j in range(n):
            if not visited_cols[j]:
                visited_cols[j] = True
                find_min(count + 1, min(nums_min, grid[row][j]))
                visited_cols[j] = False

find_min(0, float('inf'))

print(ans)