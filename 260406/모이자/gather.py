n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
min = float('inf')

for house in range(n):
    total_dist = 0
    for people in A:
        total_dist += abs(house - move) * people
    if total_dist < min:
        min = total_dist
print(min)