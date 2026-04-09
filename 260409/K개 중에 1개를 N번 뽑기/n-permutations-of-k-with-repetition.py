K, N = map(int, input().split())

# Please write your code here.
def print_result(lst):
    for i in lst:
        print(i, end = " ")
    print()

def find_comb(curr_i, lst):
    global K, N
    if len(lst) == N:
        print_result(lst)
        return
    if curr_i == N + 1:
        return

    for i in range(1, K + 1):
        lst.append(i)
        find_comb(curr_i + 1, lst)
        lst.pop()

find_comb(1, [])