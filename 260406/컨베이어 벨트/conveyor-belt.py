n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
for _ in range(t):
    temp_u = u[-1]
    temp_d = d[-1]
    for i in range(n-1, 0, -1):
        u[i] = u[i - 1]
        d[i] = d[i - 1]
    u[0] = temp_d
    d[0] = temp_u

for i in u:
    print(i, end=" ")
print()
for i in d:
    print(i, end= " ")