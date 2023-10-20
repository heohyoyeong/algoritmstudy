def dfs(x,y,n):
    n += array[y][x]
    if x ==len(array)-1 and y== len(array)-1:
        result.append(n)
    else:
        if x<len(array)-1:
            next_x= x+1
            dfs(next_x,y,n)
        if y<len(array)-1:
            next_y= y+1
            dfs(x,next_y,n)
    return result


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    array = [list(map(int,input().split())) for _ in range(n)]
    result = []
    result = dfs(0, 0, 0)
    print(f"#{test_case} {min(result)}")