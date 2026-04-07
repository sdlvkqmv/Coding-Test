n = int(input())

# Please write your code here.

result = []

def search(i, comb: list):
    '''
    i : current index
    '''
    global n
    #print(i, comb, len(comb))

    if len(comb) == n:
        #print(comb)
        temp = [_ for _ in comb]
        result.append(temp)
        #print(result)
        return


    for _ in range(1, 5):
        comb.append(_)
        search(i + 1, comb)
        comb.pop()

def in_range(i, len):
    return 0 <= i and i < len

search(0, [])
count = 0
for r in result:
    i = 0
    wonderful = True

    while wonderful:
        for _ in range(i + 1, i + r[i]):
            if in_range(_, n):
                if r[_] == r[i]:
                    continue
    
            wonderful = False
            break

        i += r[i]
        if not in_range(i, n):
            break

    if i == n and wonderful:
        #print(r)
        count += 1
            

print(count)
