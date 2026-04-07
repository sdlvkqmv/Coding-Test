n = int(input())

# Please write your code here.
count = 0


def search(i, comb):
    '''
    i : current index
    '''
    global n, count
    #print(i, comb, len(comb))

    if i == n:
        if is_wonderful(comb):
            count += 1
        return

    for _ in range(1, 5):
        comb.append(_)
        search(i + 1, comb)
        comb.pop()

def is_wonderful(r):
    i = 0

    while i < n:
        if i + r[i] - 1 >= n:
            return False
            
        for _ in range(i, i + r[i]):
            if r[_] != r[i]:
                return False
        i += r[i]
    return True
                  
search(0, [])
print(count)