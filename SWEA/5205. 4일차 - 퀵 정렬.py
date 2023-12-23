import sys
sys.stdin = open("input.txt", "r")

T = int(input())


for test_case in range(1, T+1):
    total = 0
    N = int(input())

    arrays = list(map(int,input().split(" ")))

    arrays = merge_sort(arrays)

    print(f"#{test_case} {arrays[N//2]} {total}")
