K, N = map(int, input().split())

# Please write your code here.
def print_result(lst):
    for i in lst:
        print(i, end = " ")
    print()

def find_comb(curr_i, lst):
    global K, N
    if curr_i == N + 1:
        print_result(lst)

