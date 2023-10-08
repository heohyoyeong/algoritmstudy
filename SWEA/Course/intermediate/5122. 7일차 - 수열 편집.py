import sys
sys.stdin = open("input.txt", "r")

def function(str,list,array):
    if str == "I":
        head = array[:int(list[0])]
        tail = array[int(list[0]):]
        array = head + [int(list[1])]+tail

    elif str == "D":
        head = array[:int(list[0])]
        tail = array[int(list[0])+1:]
        array = head+tail

    elif str == "C":
        array[int(list[0])] = int(list[1])

    return array

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, L = list(map(int,input().split()))
    array = list(map(int,input().split()))

    for _ in range(M):
        data = list(input().split())
        str, lists = data[0], data[1:]
        array = function(str,lists,array)

    if len(array)<=L:
        print(f"#{test_case} -1")
    else:
        print(f"#{test_case} {array[L]}")