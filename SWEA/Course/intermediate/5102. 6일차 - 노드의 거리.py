import sys

sys.stdin = open("input.txt", "r")

from collections import deque

def DFS(Start, Goal):
    global min_range

    score = 0

    que = deque()
    que.append([Start,score])
    visited[Start] = 1


    while que:
        now, score = que.popleft()

        for i in range(1, V+1):
            if array[now][i] != 0 and visited[i] != 1:
                if i==Goal:
                    min_range = score + 1
                    return
                else:
                    que.append([i,score+1])
                    visited[i] = 1




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V, E = list(map(int,input().split()))
    min_range = V*V
    visited = [0] * (V + 1)
    array = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for i in range(E):
        y, x = list(map(int, input().split()))
        array[y][x] = 1
        array[x][y] = 1

    Start, Goal = list(map(int, input().split()))
    DFS(Start, Goal)
    if min_range!=V*V:
        print(f"#{test_case} {min_range}")
    else:
        print(f"#{test_case} 0")