a, b, c = map(int, input().split())

# Please write your code here.
start_mins = 11 * 24 * 60 + 11 * 60 + 11

end_mins = A * 24 * 60 + B * 60 + C

print(start_mins - end_mins)