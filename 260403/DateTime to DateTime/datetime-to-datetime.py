a, b, c = map(int, input().split())

# Please write your code here.
start_mins = 11 * 24 * 60 + 11 * 60 + 11

end_mins = a * 24 * 60 + b * 60 + c

print(start_mins - end_mins)