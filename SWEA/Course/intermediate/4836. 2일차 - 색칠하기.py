import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    Datas = [list(map(int,input().split())) for z in range(N)]
    blue_array = [[0]*10 for _ in range(10)]
    red_array = [[0]*10 for _ in range(10)]
    result = 0

    for i in range(N):
        x0, x1 = Datas[i][0], Datas[i][2]
        y0, y1 = Datas[i][1], Datas[i][3]
        if Datas[i][4]==1:
            for j in range(y0,y1+1):
                for k in range(x0,x1+1):
                    blue_array[j][k] = 1
        else:
            for j in range(y0,y1+1):
                for k in range(x0,x1+1):
                    red_array[j][k] = 1

    for i in range(10):
        for j in range(10):
            if blue_array[i][j]== 1 and red_array[i][j]== 1:
                result+=1

    print(f"#{test_case} {result}")


