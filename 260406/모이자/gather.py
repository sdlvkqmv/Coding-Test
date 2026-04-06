n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
min = float('inf')

for house in range(n):
    total_dist = 0
    for i, people in enumerate(A):
        total_dist += abs(house - i) * people
    if total_dist < min:
        min = total_dist
print(min)