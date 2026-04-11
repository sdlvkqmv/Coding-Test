# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''
# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
sys.stdin = open("../AI 로봇 청소기/input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    boxes = []
    box_dict = {}
    num_box = M
    picked_boxes = []

    for m in range(M):
        k, h, w, c = map(int, input().split())
        boxes.append((k, h, w, c - 1)) # 0-based indexing
        box_dict[k] = (h, w, c - 1)

    grid = [[0 for _ in range(N)] for _ in range(N)] #k 택배 번호로 저장할 생각

    def check_bottom():
        '''
        들어온 박스가 바닥이나 다른 박스에 닿았는지 확인
        '''
        pass

    def init_drop_boxes():
        '''
        boxes안에 있는 순서대로 차곡차곡 grid에 쌓기
        # TODO? : temp 복사해서 붙여넣는 로직 comprehension 못하나?
        '''
        global N
        for box in boxes:
            k, h, w, j = box
            start_j = j

            temp = [[grid[i_][j_] for j_ in range(start_j, start_j + w)] for i_ in range(N)]
            can_drop = True
            drop_row = 0
            while drop_row < N:
                for j in range(w):
                    if temp[drop_row][j] != 0:
                        can_drop = False
                        break
                if not can_drop:
                    drop_row -= 1
                    break
                elif can_drop and drop_row == N - 1:
                    break
                drop_row += 1



            temp[drop_row - h + 1: drop_row+ 1] = [[k for _ in range(w)] for _ in range(h)]


            for c in range(start_j, start_j + w):
                for i in range(N):
                    grid[i][c] = temp[i][c - start_j] # 이거 comprehension 못하나?

    def pop_left():
        '''
        Grid에서 박스 순회 한다음에 왼쪽으로 뺼수 있는거 빼기 (여러개면 k 작은 순) -> 이후 drop_boxes
        1. row위에 부터 순회 ->
        '''
        global N, num_box
        pop_available_boxes = []
        i = 0
        while i < N:
            is_block = False
            for (j, k) in enumerate(grid[i]):
                if k != 0:  #왼쪽부터 순회하다가 박스 마주치면
                    if can_pop_left(k, i, j):
                        pop_available_boxes.append((k, i, j))
                        i += box_dict[k][0] # h만큼 다음 row에서 순회
                        is_block = True
                        break
                    break
            # 이번 층이 비어있었으면
            if not is_block:
                i += 1

        pop_available_boxes.sort(key = lambda x: x)

        if len(pop_available_boxes) == 0:
            return

        pop_k, pop_i, pop_j = pop_available_boxes[0]
        pop_h, pop_w = box_dict[pop_k][0], box_dict[pop_k][1]
        for i_ in range(pop_i, pop_i + pop_h):
            for j_ in range(pop_j, pop_j + pop_w): #pop_right에선 여기 수정
                grid[i_][j_] = 0
        num_box -= 1
        picked_boxes.append(pop_k)

    def can_pop_left(k, i, j):
        '''
        박스 번호, 시작 좌표 입력받아서 현재 그리드 상태에서 왼쪽으로 뺼수 있는지 체크
        '''
        can_pop = True
        h, w, _ = box_dict[k]
        for i_ in range(i, i + h):
            for j_ in range(j):
                if grid[i_][j_] != 0:
                    can_pop = False
                    break

            if not can_pop:
                break
        return can_pop

    def pop_right():
        global N, num_box
        pop_available_boxes = []
        i = 0
        while i < N:
            is_block = False
            for j in range(len(grid[i]) - 1, -1, -1): #오른 쪽 부터 순회
                k = grid[i][j]
                if k != 0:
                    if can_pop_right(k, i, j):
                        pop_available_boxes.append((k, i, j))
                        i += box_dict[k][0]
                        is_block = True
                        break
                    break
            if not is_block: #이번층이 비어있었거나, 택배는 있었는데 뺼수 없는 택배였던 경우
                i += 1

        pop_available_boxes.sort(key = lambda x: x)

        if len(pop_available_boxes) == 0:
            return
        pop_k, pop_i, pop_j = pop_available_boxes[0]
        pop_h, pop_w = box_dict[pop_k][0], box_dict[pop_k][1]
        for i_ in range(pop_i, pop_i + pop_h):
            for j_ in range(pop_j - pop_w + 1, pop_j + 1):  # pop_right에선 여기 수정
                grid[i_][j_] = 0
        num_box -= 1
        picked_boxes.append(pop_k)

    def can_pop_right(k, i, j):
        '''
        k: 박스번호
        i: 박스 상단 row
        j: 박스 오른쪽 끝 col
        '''
        global N
        can_pop = True
        h, w, _ = box_dict[k]
        for i_ in range(i, i + h):
            for j_ in range(j + 1, N):
                if grid[i_][j_] != 0:
                    can_pop = False
                    break
            if not can_pop:
                break
        return can_pop



    def drop_box():
        '''
        다 배치되어있는 그리드 상태에서 박스 떨굴수 있는거 있으면 떨구는 함수
        아래row 부터 순회하면서 떨구는 로직이 좋을듯
        '''
        global N
        dropped_boxes = [] # 이미 drop한 박스 번호들 저장 -> 위층에서 걸렸을 때 또 체크하지 않도록
        for i in range(N - 1, -1, -1): #아래부터 순회
            for j in range(0, N): #왼쪽부터 순회
                can_drop = False
                k = grid[i][j] #drop 가능한지 확인할 박스 번호 지정
                if k != 0 and k not in dropped_boxes: #여기서 걸리는 인덱스는 아래 왼쪽임 유의
                    dropped_boxes.append(k) # 체크한 박스 번호 추가해서 중복 체크 안되게
                    drop_h, drop_w, _ = box_dict[k]

                    temp = [[grid[i_][j_] for j_ in range(j, j + drop_w)] for i_ in range(N)] # 복사할 임시 배열
                    drop_i = i
                    for i_ in range(i + 1, N): #위에서 아래로 순회(현재 블럭의 최소 높이(j) 까지)
                        is_droppable = True
                        drop_i = i_
                        for j_ in range(drop_w):
                            if temp[i_][j_] != 0: #비어있는 층아니면
                                is_droppable = False
                                break

                        if not is_droppable: #현재 층이 떨어 뜨릴수 없으면 가장 낮게 떨어뜨릴수 있는 층은 그위에
                            drop_i = i_ - 1
                            break
                    if drop_i != i:

                        temp[drop_i - drop_h + 1 : drop_i + 1] = [[k for _ in range(drop_w)] for _ in range(drop_h)]
                        #temp[drop_i - drop_h + 1 : drop_i + 1][:] = [[k for _ in range(drop_w)] for _ in range(drop_h)] <- 얘는 뭐가 다른거지


                        temp[i - drop_h + 1: drop_i - drop_h+ 1] = [[0 for _ in range(drop_w)] for _ in range(drop_i - i)]
                        for r in range(N):
                            for c in range(drop_w):
                                grid[r][c + j] = temp[r][c] # 여기 문제

                         ######################
                    '''
                        if is_bottom: #떨어질수 있을만큼(drop_w) 비어있었으면 (0)
                            temp[i_ - drop_h + 1: i_ + 1] = [[k for _ in range(drop_h)] for _ in range(drop_w)]
                            #내려온 만큼 위에를 0 배열로 만들어야 함
                            #내려온 만큼을 어떻게 구하냐?
                            temp[i - drop_h + 1: i_ - drop_h + 1] = [[0 for _ in range(drop_w)] for _ in range(i_ - i)]
                            can_drop = True
                            break
                    '''

                    #grid[:][j: j + drop_w] = [[temp[i_][j_] for j_ in range(drop_w)] for i_ in range(N)] <- 왜 복사가 안되지?


    init_drop_boxes()
    while num_box > 0:
        #print(num_box)
        pop_left()
        drop_box()
        pop_right()
        drop_box()
    for box in picked_boxes:
        print(box)
    print()