# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
#
# 해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
#
#
# 예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.
import sys
from itertools import combinations
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
A = [1,2,3,4,5,6,7,8,9,10,11,12]

for test_case in range(1, T + 1):
    result = 0
    N, K = list(map(int,input().split()))
    New_array = []
    for i in A:
        if i <= K:
            New_array.append(i)
    New_array = list(combinations(New_array,N))
    for i in range(len(New_array)):
        sum = 0
        for j in range(N):
            sum +=New_array[i][j]

        if sum == K:
            result+=1

    print(f"#{test_case} {result}")

