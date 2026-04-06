n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def in_range(i, j):
    if 0 <= i and i < n:
        return 0 <= j and j < n

max = -1

for i in range(n):
    for j in range(n):
        count = 0
        if in_range(i + 2, j + 2):
            for i_ in range(i, i + 3):
                for j_ in range(j, j + 3):
                    if grid[i_][j_] == 1:
                        count += 1

        if count > max:
            max = count
print(max)
