n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.
temp = []
#print(blocks)

# 0이 가장 위
for i in range(len(blocks)):
    if not (s1 - 1 <= i and i < e1):
        temp.append(blocks[i])

#print(len(temp))

blocks = temp

temp = []
for i in range(len(blocks)):
    if not (s2 - 1 <= i and i < e2):
        temp.append(blocks[i])
print(len(temp))
for b in temp:
    print(b)
