N = int(input())
A = list(map(int, input().split()))

# Please write your code here.
count = 0
for i, c1 in enumerate(A):
    for j, c2 in enumerate(A[i + 1:]):
        #print(c1, c2, c1 <= c2)
        if c1 <= c2:
            for c3 in A[i + j + 2:]:
                if c2 <= c3:
                    #print(c1, c2, c3)
                    count += 1

print(count)