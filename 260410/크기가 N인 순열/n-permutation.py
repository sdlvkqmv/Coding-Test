n = int(input())

# Please write your code here.
def print_ans():
    for i in ans:
        print(i, end = " ")
    print()

ans = []
visited = [False for _ in range(n)]

def find_perm(curr_i):
    if len(ans) == n:
        print_ans()
        return
    
    elif curr_i == n + 1:
        return
    
    for i in range(1, n + 1):
        if visited[i - 1]:
            continue
        
        ans.append(i)
        visited[i - 1] = True
        find_perm(curr_i + 1)
        ans.pop()
        visited[i - 1] = False
        find_perm(curr_i + 1)

find_perm(1)