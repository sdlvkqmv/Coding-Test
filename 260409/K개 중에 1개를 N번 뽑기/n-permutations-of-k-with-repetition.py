# 변수 선언 및 입력
k, n = tuple(map(int, input().split()))
selected_nums = []


# 선택된 원소들을 출력해줍니다.
def print_permutation():
    for num in selected_nums:
        print(num, end = " ")
    print()


def find_permutations(cnt):
    # n개를 모두 뽑은 경우 답을 출력해줍니다.
    if cnt == n:
        print_permutation()
        return
    
    # 1부터 k까지의 각 숫자가 뽑혔을 때의 경우를 탐색합니다.
    for i in range(1, k + 1):
        selected_nums.append(i)
        find_permutations(cnt + 1)
        selected_nums.pop()


find_permutations(0)
