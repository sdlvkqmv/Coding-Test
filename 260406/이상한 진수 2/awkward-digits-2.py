a = input()

# Please write your code here.
def flip(i):
    if i == '0':
        return '1'
    return '0'


def get_digit_10(binary):
    digit_10 = 0    

    for i, val in enumerate(binary):
        digit_10 += (2 ** (len(binary) - i - 1)) * int(val)
    return digit_10

max = 0

for i, c in enumerate(a):
    temp = [p for p in a]
    c = flip(c)
    temp[i] = c
    #print(temp)
    temp = get_digit_10(temp)
    #print(temp)
    if temp > max:
        max = temp
print(max)
