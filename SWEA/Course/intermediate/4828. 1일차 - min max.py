#
# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
#
#
# [입력]
#
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
#
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
#
# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
#
# [출력]
#
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    datas = list(map(int,input().split()))
    start = 0
    while start < len(datas)-1:
        for i in range(len(datas)-1-start):
            if datas[i] > datas[i+1]:
                datas[i], datas[i+1] = datas[i+1], datas[i]
        start +=1
    print(f"#{test_case} {datas[-1]-datas[0]}")

