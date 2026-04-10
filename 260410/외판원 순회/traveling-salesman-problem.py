n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# i에서 j

#0애서 시작, 0으로 돌아오기
# visited 배열 두고 방문하면 

visited = [False for _ in range(n)]
visited[0] = True

ans = float('inf')
#moves = []
def find_min(curr_pos, cost, visited_count):
    global ans
    #print(moves, cost, visited_count)
    if visited_count == n: # 마지막 0 제외하고 다 방문 완료
        cost += A[curr_pos][0]
        #print("Total: ", cost)
        ans = min(ans, cost)
        return
    
    for next_pos in range(n):
        if not visited[next_pos] and A[curr_pos][next_pos] != 0:
            visited[next_pos] = True
            #moves.append(next_pos)
            find_min(next_pos, cost + A[curr_pos][next_pos], visited_count + 1)
            #moves.pop()
            visited[next_pos] = False
    
find_min(0, 0, 1)

print(ans)