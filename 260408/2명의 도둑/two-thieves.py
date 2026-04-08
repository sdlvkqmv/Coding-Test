n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

# 1. 특정 시작점(row, col)에서 길이 M의 구간 내 최대 가치를 찾는 함수
def get_max_value(row, col):
    # 해당 구간의 M개 원소만 따로 슬라이싱
    arr = weight[row][col : col + m]
    max_val = 0
    
    # 부분집합을 구하기 위한 재귀 함수 (DFS)
    def dfs(idx, curr_sum, curr_val):
        nonlocal max_val
        
        # [가지치기] 무게 합이 C를 넘으면 불가능하므로 즉시 종료
        if curr_sum > c:
            return
        
        # C 이하인 경우이므로 항상 최댓값을 갱신해줌
        max_val = max(max_val, curr_val)
        
        # M개의 원소를 모두 확인했으면 종료
        if idx == m:
            return
            
        # 경우의 수 1) 현재 인덱스의 물건을 훔치는 경우
        dfs(idx + 1, curr_sum + arr[idx], curr_val + (arr[idx] ** 2))
        
        # 경우의 수 2) 현재 인덱스의 물건을 훔치지 않고 넘어가는 경우
        dfs(idx + 1, curr_sum, curr_val)

    dfs(0, 0, 0) # 초기 상태에서 탐색 시작
    return max_val


result = 0

# 2. 겹치지 않는 두 구간 고르기
for i1 in range(n):
    # 첫 번째 구간이 격자를 벗어나지 않도록 (n - m + 1)까지만 순회
    for j1 in range(n - m + 1): 
        val1 = get_max_value(i1, j1)
        
        # 두 번째 구간 고르기 (i1번째 행부터 탐색 시작)
        for i2 in range(i1, n):
            # 같은 행(i1 == i2)이라면, 겹치지 않기 위해 j2는 j1 + m 부터 시작!
            # 다른 행이라면 처음(0)부터 시작해도 무방함.
            start_j2 = (j1 + m) if i1 == i2 else 0
            
            for j2 in range(start_j2, n - m + 1):
                val2 = get_max_value(i2, j2)
                result = max(result, val1 + val2)

print(result)