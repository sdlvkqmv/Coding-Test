m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start_days = sum(day_in_month[:m1]) + d1
end_days = sum(day_in_month[:m2]) + d2

diff = end_days - start_days

print(days[diff % 7])