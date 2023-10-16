import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = input().split()
    b=bin(int('0x'+a[1] ,16))[2:]
    if len(b) < int(a[0])*4:
        b = '0'+b
    print(f"#{test_case} {b}")

