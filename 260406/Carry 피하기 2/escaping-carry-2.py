n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
arr = [str(i) for i in arr]
#print(arr)

def in_range(n, string):
    return 0 <= n and n < len(string)

max = -float('inf')
for i, n1 in enumerate(arr):
    for j, n2 in enumerate(arr[i + 1:]):
        for k, n3 in enumerate(arr[i + j + 2:]):

            available = True

            list = [n1, n2, n3]

            list.sort(key = lambda x: len(x))
            #print(list)
            #print(len(list[-1]))

            if len(list[0]) < len(list[2]):
                list[0] = (len(list[2]) - len(list[0])) * "0" + list[0]
                #print(list[0])
            if len(list[1]) < len(list[2]):
                list[1] = (len(list[2]) - len(list[1])) * "0" + list[1]
                #print(list[0])

            #print(list)

            for digit in range(len(list[-1])):
                sum = 0
                sum = int(list[0][digit]) + int(list[1][digit]) + int(list[2][digit])
                #print(sum)
                if sum >= 10:
                    available = False
                    break

            if available:
                #print(n1, n2, n3)
                result = int(n1) + int(n2)+ int(n3)
                #print(result)
                if max < result:
                    max = result
            
print(max)