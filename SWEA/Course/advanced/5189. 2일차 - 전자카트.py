from itertools import permutations

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    total = [z for z in range(2,n+1)]
    perm = list(permutations(total,n-1))
    result = []
    for i in range(len(perm)):
        test = list(perm[i])
        test.append(1)
        test.insert(0,1)
        sum = 0
        for j in range(len(test)-1):
            sum += array[test[j]-1][test[j+1]-1]
        result.append(sum)
    print(f"#{test_case} {min(result)}")
