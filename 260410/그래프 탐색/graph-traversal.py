n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
adjacency = [[False for _ in range(n)] for _ in range(n)]
#print(edges)

for (i, j) in edges:
    adjacency[i - 1][j - 1] = True
    adjacency[j - 1][i - 1] = True
#0-based
#print(adjacency)

count = 0

visited = [False for _ in range(n)]
visited[0]= True

def BFS(curr_v):
    global count
   #print(curr_v, count)
    for next_v in range(n):
        if adjacency[curr_v][next_v] and not visited[next_v]:
            visited[next_v] = True  
            count += 1
            BFS(next_v)
    
BFS(0)
print(count)


    