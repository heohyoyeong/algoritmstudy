import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def DFS(start, end):

    visited = [0]*(V+1)

    visited[start] = 1
    stack = [start]
    while stack:
        now = stack.pop()
        visited[now] = 1
        for i in range(1,V+1):
            if not visited[i] and node[now][i]==1:
                stack.append(i)
    if visited[end]==1:
        return 1
    else:
        return 0




# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V, E = list(map(int,input().split()))
    node = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        x, y = list(map(int, input().split()))
        node[x][y] = 1

    start, end = list(map(int, input().split()))
    result = DFS(start, end)
    print(f"#{test_case} {result}")

