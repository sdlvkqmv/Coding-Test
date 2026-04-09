n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
#'최대' 점프 가능 거리니까 최대 안에서 다 찾아봐야할듯
n -= 1 # 0-based idx

result = float('inf')

def jump(num_jumps, position):
    global result
    if position == n:
        result = min(result, num_jumps)
        return
    
    elif position > n:
        return
    
    for j in range(1, num[position] + 1):
        jump(num_jumps + 1, position + j)

jump(0, 0)

if result == float('inf'):
    print(-1)

else:
    print(result)
