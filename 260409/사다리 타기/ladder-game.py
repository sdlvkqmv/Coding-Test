n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
#N개 세로, M개 가로
#주어진 상태와 똑같은 결과 내는 최소 가로줄

def get_ladders(edge):
    '''
    list of tuple (edges) 받아서 list of boolean 리턴
    '''
    global n, m
    ladders = [[False for _ in range(n - 1)] for _ in range(m)]

    for a, b in edges:
        ladders[b - 1][a - 1] = True

    return ladders

def get_result(edge_combs):
    '''
    사다리 combi이랑 결과 저장할 리스트 받아서 최종 결과 순서 출력
    '''
    global n, m
    result = [i + 1 for i in range(n)]
    ladders = get_ladders(edge_combs)

    if len(edge_combs) == 0:
        return result

    for i, row in enumerate(ladders):
        for j, edge in enumerate(row):
            if edge:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

init_result = get_result(edges)

def find_edge_cases(i, edge_comb):
    '''
    가능한 모든 edge 달수 있는 경우에 대해서 result 찾고, 최솟 값이면 리턴
    '''
    global m, min
    comb_result = get_result(edge_comb)
    if comb_result == init_result:
        min = len(comb_result)
        return
    elif i == len(edges):
        return

    edge_comb.append(edges[i])
    find_edge_cases(i + 1, edge_comb)
    edge_comb.pop()
    find_edge_cases(i + 1, edge_comb)
find_edge_cases(0, [])
print(min)
