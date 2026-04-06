A = input()

# Please write your code here.
count = 0
for i, c in enumerate(A):
    if c == '(':
        for d in A[i + 1:]:
            if d == ')':
                count += 1

print(count)