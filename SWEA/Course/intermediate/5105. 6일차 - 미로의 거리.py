import sys

sys.stdin = open("input.txt", "r")


from collections import deque

def checking(x,y):
    return 0<=x<N and 0 <= y < N and [x, y] not in visited and (meze_arary[y][x]==0 or meze_arary[y][x]==3)


dx_array = [0, 0, -1, 1]

dy_array = [1, -1, 0, 0]
def BFS(x, y):

    global min_num
    cost = 0
    queue = deque([[x, y, cost]])
    costs = []


    while queue:
        x, y, cost = queue.popleft()


        for i in range(4):
            new_x = x + dx_array[i]
            new_y = y + dy_array[i]
            if checking(new_x, new_y):
                if meze_arary[new_y][new_x] == 3:
                    if min_num > cost:
                        min_num = cost + 1
                        return
                visited.append([new_x, new_y])
                costs.append(cost)
                queue.append([new_x, new_y, cost + 1])




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    visited = []
    min_num = N*N
    meze_arary = []
    for i in range(N):
        case = []
        data = input()
        for j in range(N):
            case.append(int(data[j]))
            if int(data[j])==2:
                start_x = j
                stary_y = i
        meze_arary.append(case)

    BFS(start_x, stary_y)

    if min_num!=N*N:
        print(f"#{test_case} {min_num-1}")
    else:
        print(f"#{test_case} 0")


# def BFS(x, y, cost):
#     global min_num
#     cost += 1
#     visited.append([x,y])
#
#     if meze_arary[y][x]==3:
#         if min_num > cost:
#             min_num = cost
#             return
#
#     for i in range(4):
#         new_x = x + dx_array[i]
#         new_y = y + dy_array[i]
#
#         if checking(new_x,new_y):
#             BFS(new_x,new_y,cost)
#
#
#
#
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N = int(input())
#
#     min_num = N*N
#     visited = []
#     meze_arary = []
#     for i in range(N):
#         case = []
#         data = input()
#         for j in range(N):
#             case.append(int(data[j]))
#             if int(data[j])==2:
#                 start_x = j
#                 stary_y = i
#         meze_arary.append(case)
#
#     BFS(start_x, stary_y, 0)
#
#     if min_num!=N*N:
#         print(f"#{test_case} {min_num-1}")
#     else:
#         print(f"#{test_case} 0")
#
