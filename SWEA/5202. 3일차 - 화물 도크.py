import sys
sys.stdin = open("input.txt", "r")

T = int(input())




for test_case in range(1, T + 1):
    N = int(input())
    array = [[0 for _ in range(25)] for _ in range(25)]
    start = 24

    for _ in range(N):
        St, Et = list(map(int,input().split()))
        if sum(array[St])!=0:
            index = array[St].index(1)
            if index > Et:
                array[St][Et] = 1
                array[St][index] = 0
        else:
            array[St][Et] = 1
        if start > St:
            start = St

    result = 0

    for i in range(start, 24):
        new_start = i
        new_end = 0
        new_result = 0
        if sum(array[i])!=0:
            while new_end<24:
                new_result += 1
                new_end = array[new_start].index(1)
                while sum(array[new_end])==0 and new_end<24:
                    new_end+=1
                new_start = new_end
            if result<new_result:
                result=new_result
    print(result)
