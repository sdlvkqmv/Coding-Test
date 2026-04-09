K, N = map(int, input().split())

# Please write your code here.
def print_result(res):
    for i in res:
        print(i, end = " ")
    print()

def choose(count):
    global K, N
    if count == N :
        print_result(result)
        return
    
    
    for select in range(1, K + 1):
        if count in (0, 1) or select != result[-1] or select != result[-2]:
            result.append(select)
            choose(count + 1)
            result.pop()

result = []
choose(0)
        
