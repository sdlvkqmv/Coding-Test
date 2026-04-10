n = int(input())

# Please write your code here.
def print_ans():
    for i in ans:
        print(i, end = " ")
    print()

visited = [False for _ in range(n + 1)]
ans = []

def find_perm(count):
    global n
    if count == n:
        print_ans()
        return
        
    for i in range(n, 0, -1):
        if not visited[i]:
            ans.append(i)
            visited[i] = True
            find_perm(count + 1)
            ans.pop()
            visited[i] = False

find_perm(0)
