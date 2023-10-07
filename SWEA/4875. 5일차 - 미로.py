import sys
sys.stdin = open("input.txt", "r")

T = int(input())

dx_array = [1,-1, 0, 0]
dy_array = [0, 0, 1, -1]

def checking(x,y):
    return 0<= x <N and 0<= y < N and visited[y][x] != 1 and (maze_array[y][x] == 0 or maze_array[y][x] == 3)

def DFS(x,y):
    if maze_array[y][x] == 3:
        result.append(1)
        return result

    for i in range(4):
        dy = y + dy_array[i]
        dx = x + dx_array[i]
        if checking(dx, dy):
            visited[y][x] = 1
            DFS(dx, dy)


for test_case in range(1, T + 1):
    N = int(input())
    maze_array = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    result = []
    for i in range(N):
        data = input()
        end = data.find("3")
        start = data.find("2")
        if end != -1:
            end_x = end
            end_y = i
        if start != -1:
            start_x = start
            start_y = i
        array = []
        for j in range(N):
            array.append(int(data[j]))
        maze_array.append(array)

    DFS(start_x,start_y)
    print(f"#{test_case} {len(result)}")
