import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, K = list(map(int,input().split()))
    array = list(map(int,input().split()))

    start = 0
    # start += M
    for _ in range(K):
        start += M
        if start>len(array):
            loc = start%(len(array))
            start =loc
        else:
            loc = start

        if loc==0:
            new = array[-1] + array[0]
            array = array + [new]
        else:
            head = array[:loc]
            tail = array[loc:]
            if len(tail)!=0:
                new = head[-1] + tail[0]
            else:
                new = head[-1] + head[0]
            array = head + [new] + tail


    array.reverse()

    str = f"#{test_case}"
    if len(array)>=10:
        for i in range(10):
            str = str + f" {array[i]}"
    else:
        for i in range(len(array)):
            str = str + f" {array[i]}"

    print(str)
