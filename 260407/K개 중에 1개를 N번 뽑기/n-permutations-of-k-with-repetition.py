K, N = map(int, input().split())

# Please write your code here.
def combination(i, result, K, N):
    #print(i, result)

    if len(result) == N:
        for n in result:
            print(n, end = " ")
        print()
        return
    elif i > K and len(result) != N:
    
    for _ in range(1, K + 1):
        result.append(_)
        combination(i + 1, result, K, N)
        result.pop()

combination(1, [], K, N)
