n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
# abs(A -2* 한그룹의 합)을 최소화
def get_sum(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

total_sum = get_sum(num)

set_a = []
ans = float('inf')

def get_combs(count, curr_i):
    global ans

    if count == n:
        sum = get_sum(set_a)
        ans = min(abs(total_sum - sum * 2), ans)
        return

    elif curr_i == len(num):
        return

    set_a.append(num[curr_i])
    get_combs(count+ 1, curr_i + 1)
    set_a.pop()
    get_combs(count, curr_i + 1)

get_combs(0, 0)
print(ans)