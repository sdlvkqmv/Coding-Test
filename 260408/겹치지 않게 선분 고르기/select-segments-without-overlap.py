n = int(input())
lines = []
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))
    x1.append(a)
    x2.append(b)

# Please write your code here.
# 뽑을 수 있는 가장 많은 선분의 수 -> 그냥 냅다 모든 조합 구할수가 없음
# N은 1에서 15 -> 걍 해볼까...는 아닌것 같은데

# 아 중복 조합이 아니니까 해볼수 있을것 같기도
# len(lines)부터 거꾸로 내려올까? -> 모든 선분 포함 -> 하나씩 빼가기
    # 조금 나을듯, 아닌가 문제 조건에 따라 다를듯
# 1. 모든 조합 구하기
# 1-1. 조건 만족하면 바로 리턴 하고 출력
#print(lines)

def check_overlap(lines):
    '''
    Lines(list): 선분 조합
    '''
    for i, (x1, x2) in enumerate(lines):
        #print(x1, x2)
        #앞에부터 하니까 앞쪽은 체크할 필요 없음
        for x3, x4 in lines[i + 1:]:
            #print(x3, x4)
            # 모든 겹치는 조건 체크
            if (x1 <= x3 and x3 <= x2) or (x3 <= x1 and x1<= x4):
                return True
        
    return False


max = 0
#모든 선분(lines)에서 빼가면서 체크하려고 했는데 pop하고 append하는 로직을 짜는 방식이 생각이 안나 기본0부터 세는 방식으로 바꿈
def search(idx, combs):
    #print(combs)
    global max, n
    
    #현재 최대 개수 보다 조합 길이가 긴 경우에만 겹치는거 체크
    if max < len(combs):
        if not check_overlap(combs):
            #print(len(lines))
            max = len(combs)
        else:
            return
        
    if idx == n:
        return
    
    combs.append(lines[idx])
    search(idx + 1, combs)
    combs.pop()
    search(idx + 1, combs)


search(0, [])

print(max)