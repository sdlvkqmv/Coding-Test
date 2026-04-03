a, b, c = map(int, input().split())

# Please write your code here.
start_mins = 11 * 24 * 60 + 11 * 60 + 11

end_mins = a * 24 * 60 + b * 60 + c

result = end_mins - start_mins

if result < 0:
    result = -1

print(result)