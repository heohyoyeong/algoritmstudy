import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = list(map(int,input().split()))
    datas = list(map(int, input().split()))

    ChargeStation = [0]*N
    for i in datas:
        ChargeStation[i] = 1

    chance = 0
    start_point = 0
    limit = 0
    while True:
        if start_point+K >= N:
            print(f"#{test_case} {chance}")
            break
        elif limit>=K:
            print(f"#{test_case} {0}")
            break

        if ChargeStation[start_point+K-limit] == 1:
            start_point += K-limit
            limit = 0
            chance +=1
        else:
            limit +=1







