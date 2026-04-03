m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date1 = 0
for i in range(m1 + 1):
    date1 += days[i]

date1 += d1

date2 = 0 

for i in range(m2 + 1):
    date2 += days[i]

date2 += d2

print(date2 - date1)
