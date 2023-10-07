import sys

sys.stdin = open("input.txt", "r")

from collections import deque


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = list(map(int,input().split()))

    Datas = deque(map(int,input().split()))
    nums = deque([i for i in range(1,M+1)])

    queue = deque()
    for i in range(N):
        queue.append([Datas.popleft(),nums.popleft()])

    while queue:
        Cheeze, num =queue.popleft()
        Cheeze = Cheeze//2
        if Cheeze!=0:
            queue.append([Cheeze,num])
        elif Cheeze==0 and len(Datas)!=0:
            queue.append([Datas.popleft(), nums.popleft()])
    print(f"#{test_case} {num}")