n, m, k = map(int, input().split())
#n : 턴 수, m: 전체 칸수, k : 말수
nums = list(map(int, input().split()))

# Please write your code here.
positions = [1 for _ in range(k)]

ans = 0

def find_best_score(turn, score):
    global ans, n, m, k
    if turn == n:
        ans = max(ans, score)
        return
    
    for i in range(k):
        jump = nums[turn]
        
        if positions[i] < m and positions[i] + jump >= m: #여기 조건 처리가 어렵네
            score += 1
        positions[i] += jump

        find_best_score(turn + 1, score)
        if positions[i] >= m and positions[i] - jump < m:
            score -= 1
        
        positions[i] -= jump
            

find_best_score(0, 0)

print(ans)