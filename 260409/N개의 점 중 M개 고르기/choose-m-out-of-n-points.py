n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
#가장 거리 먼 두 점 거리 최소
#1. 가능한 모든조합
#2. 그 안에서 최대 거리 값 리턴


def get_largest_dist(combs):
    maxi = 0
    for i, point1 in enumerate(combs):
        for point2 in combs[i + 1:]:
            dist = (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
            maxi = max(dist, maxi)

    return maxi

combs = []
ans = float('inf')

def find_all_combs(count, curr_i):
    global ans
    #print(combs)
    if count == m:
        #print('hi')
        max_dist = get_largest_dist(combs)
        ans = min(max_dist, ans)
        return

    elif curr_i == len(points):
        return

    combs.append(points[curr_i])
    find_all_combs(count + 1, curr_i + 1)
    combs.pop()
    find_all_combs(count, curr_i + 1)

find_all_combs(0, 0)

print(ans)