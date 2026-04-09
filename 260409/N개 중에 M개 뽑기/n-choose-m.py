N, M = map(int, input().split())

# Please write your code here.
ans = []
def print_answer():
    for i in ans:
        print(i, end = " ")
    print()

def find(curr_n, count):
    if curr_n == N + 1:
        if count == M:
            print_answer()
        return
    
    ans.append(curr_n)
    find(curr_n + 1, count + 1)
    ans.pop()
    find(curr_n + 1, count)
find(1, 0)