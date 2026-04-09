K, N = map(int, input().split())

# Please write your code here.
def print_result(res):
    for i in res:
        print(i, end = " ")
    print()

def choose(curr_i, result):
    global K, N
    if curr_i == N + 1:
        print_result(result)
        return
    
    for select in range(1, K + 1):
        if curr_i in (1, 2) or select != result[-1] or select != result[-2]:
            result.append(select)
            choose(curr_i + 1, result)
            result.pop()
            
        
choose(1, [])
        
