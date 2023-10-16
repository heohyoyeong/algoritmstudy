import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    Array = list(map(int,input().split()))
    data = [0 for i in range(N + 1)]

    trees = [[] for i in range(N+1)]

    row = 0
    total = 0
    while True:
        if total + 2**row <N:
            total += row
            row +=1
        else:
            break

    start = 0
    i = 1
    while True:
        start+=1

        if i>N:
            break

        for _ in range(2):
            i+=1
            if i<=N:
                trees[start].append(i)
            else:
                break

    start = 0
    idx = 0
    final = 0

    data[1] = Array[0]

    while True:
        start += 1
        if start>=len(data):
            break
        if len(trees[start])!=0:
            for i in range(len(trees[start])):
                final= start
                new_point = trees[start][i]
                idx +=1
                if data[start]>Array[idx]:
                    data[new_point] = data[start]
                    data[start] = Array[idx]
                else:
                    data[new_point] = Array[idx]

    result = [final]

    while True:
        if final == 1:
            break

        for i in range(final,0,-1):
            for j in range(len(trees[i])):
                if trees[i][j] == final:
                    result.append(i)
                    final=i

    total = 0
    for i in result:
        total += data[i]



    print(f'#{test_case} {total}')


# def min_heap(node):
#     up_node = node // 2
#     if up_node < 0:  # 루트노드에 도달하면 리턴
#         return  # return 안하면 maxdepth exceed 나옴
#     else:
#         # 부모노드가 더 크면 위치 바꿔줌
#         if tree[up_node] > tree[node]:
#             tree[node], tree[up_node] = tree[up_node], tree[node]
#             min_heap(up_node)  # 함수에 부모노드 대입해서 반복
#
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())  # 노드갯수
#     tree = [0]
#     node_num = 1
#     for num in map(int, input().split()):
#         tree.append(num)
#         min_heap(node_num)
#         node_num += 1
#
#     sum_value = 0
#     while N:  # N(마지막)노드의 조상노드 값들 더함
#         N //= 2
#         sum_value += tree[N]
#
#     print(f'#{tc} {sum_value}')