# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
#
# 해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
#
#
# 예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.
import sys
sys.stdin = open("input.txt", "r")

def dfs(Start, End, Target, result):
    center = Start + (End-Start)//2

    if center<Target:
        Start = center
        result += 1
    elif center>Target:
        End = center
        result+=1
    elif center == Target:
        return result

    return dfs(Start, End, Target, result)

T = int(input())

for test_case in range(1, T + 1):
    P, Pa, Pb = list(map(int,input().split()))
    A = dfs(1, P, Pa, 0)
    B = dfs(1, P, Pb, 0)
    if A<B:
        print(f"#{test_case} A")
    elif A>B:
        print(f"#{test_case} B")
    elif A==B:
        print(f"#{test_case} 0")

