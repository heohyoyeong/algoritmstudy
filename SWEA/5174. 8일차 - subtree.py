import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def dfs(M):
    global result

    now = array[M]
    result += len(now)

    if len(now)==0:
        return

    for i in range(len(now)):

        new = now[i]
        dfs(new)




for test_case in range(1, T + 1):
    E, M = list(map(int,input().split()))
    Data = list(map(int,input().split()))
    max_node = max(Data)
    result = 1
    array = []
    for _ in range(max_node+1):
        array.append([])

    for i in range(0,E*2,2):
        mo = Data[i]
        ch = Data[i+1]
        array[mo].append(ch)


    dfs(M)
    print(f"#{test_case} {result}")