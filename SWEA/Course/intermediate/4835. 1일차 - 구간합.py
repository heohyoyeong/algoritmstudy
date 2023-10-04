import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    datas = list(map(int, input().split()))

    end = int(N - M + 1)
    sum_result = []
    for idx in range(end):
        sums = 0
        for i in range(idx, idx + M):
            sums += datas[i]
        sum_result.append(sums)
    max_data = max(sum_result)
    min_data = min(sum_result)
    print(f"#{test_case} {int(max_data - min_data)}")