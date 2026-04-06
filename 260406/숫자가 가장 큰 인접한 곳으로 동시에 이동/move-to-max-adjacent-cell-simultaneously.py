n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]

# Please write your code here.
def in_range(i, j):
    if 0 <= i and i < n:
        return 0 <= j and j < n

def init_count():
    count = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if (i + 1, j + 1) in marbles:
                count[i][j] += 1
    return count

def get_marble(count):
    marble_list = []
    for i in range(n):
        for j in range(n):
            if count[i][j] > 0:
                marble_list.append((i, j))

    return marble_list

#print(count)

count = init_count()
dis, djs = [-1, 1, 0, 0], [0, 0, -1, 1] #상하좌우
#print(count)

for _ in range(t):
    marble_list = get_marble(count)
    new_count = [[0 for _ in range(n)] for _ in range(n)]
    for m in marble_list:
        i, j = m
        max = 0
        max_i = 0
        max_j = 0

        for di, dj in zip(dis, djs):
            new_i = i + di
            new_j = j + dj
            if in_range(new_i, new_j):
                if max < a[new_i][new_j]:
                    max = a[new_i][new_j]
                    max_i, max_j = new_i, new_j
        new_count[max_i][max_j] += 1
    #print(new_count)
    
    for i in range(n):
        for j in range(n):
            if new_count[i][j] > 1:
                new_count[i][j] = 0
    
    
    count = [[i for i in row] for row in new_count]
    #print(count)
result = 0
for row in count:
    for i in row:
        result += i

print(result)