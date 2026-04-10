n = int(input())

# Please write your code here.
def print_ans():
    for i in ans:
        print(i, end = " ")
    print()

ans = []
visited = [False for _ in range(n + 1)]

def find_perm(count):
    if count == n + 1:
        print_ans()
        return
    
    for i in range(1, n + 1):
        if visited[i]:
            continue
        
        ans.append(i)
        visited[i] = True
        find_perm(curr_i + 1)
        ans.pop()
        visited[i] = False