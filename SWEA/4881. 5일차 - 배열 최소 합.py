import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def Backtracking(row,now_sum,visited):
    global result

    if row==N:
        if now_sum < result:
            result = now_sum
    elif now_sum > result:
            return
    else:
        for col in range(N):
            if not visited[col]:
                visited[col] = 1
                Backtracking(row+1,now_sum+maze_array[row][col],visited)
                visited[col]=0



for test_case in range(1, T + 1):
    N = int(input())
    maze_array = [list(map(int,input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    result = 1000
    Backtracking(0, 0, visited)
    print(result)
