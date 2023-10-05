import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = list(map(int,input().split()))
    datas = [list(input().split()) for _ in range(N)]
    allow_point = N-M+1
    Cut=0
    while Cut==0:
        for i in range(N):
            for j in range(allow_point):
                coin = 0
                for k in range(M//2):
                    if datas[i][0][j+k] == datas[i][0][j+M-k-1]:
                        coin += 1
                if coin==M//2:
                    result = datas[i][0][j:j+M]
                    print(f"#{test_case} {result}")
                    Cut +=1
                    break

        for i in range(N):
            for j in range(allow_point):
                coin = 0
                for k in range(M//2):
                    if datas[j+k][0][i] == datas[j+M-k-1][0][i]:
                        coin += 1
                if coin==M//2:
                    result = []
                    for tt in range(M):
                       result.append(datas[j+tt][0][i])
                    result = "".join(result)
                    print(f"#{test_case} {result}")
                    Cut +=1
                    break