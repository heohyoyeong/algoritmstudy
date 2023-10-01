# 자연수로 구성된 집합 S에 대해, 집합 S의 최대공약수 GCD(S)는, S의 모든 원소를 나눌 수 있는 자연수 중 가장 큰 것이다.
# 예를 들어, GCD({70,105,42}) = 7 이다.
# 두 자연수  A와 B (A ≤ B)가 주어질 때, A이상 B이하의 모든 자연수의 최대공약수, 즉 GCD({x : A ≤ x ≤ B})의 값을 구하는 프로그램을 작성하라.
#
# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 하나의 줄로 이루어진다. 각 줄에는 두 개의 자연수 A와 B (1≤A≤B≤10100)가 공백 하나를 사이로 두고 주어진다.
# 입력되는 자연수의 범위는 64비트 정수형(C/C++의 long long, Java의 long)으로 저장할 수 없을 정도로 상당히 큰 범위임에 유의하라.
#
# [출력]
# 각 테스트 케이스마다 한 줄에 하나씩, 최종적으로 만들 수 있는 최소 결함의 수를 출력하라.



import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def func(A,B):
    while True:
        C = B%A
        if C == 0:
            return A
        else:
            B = A
            A = C

for test_case in range(1, T + 1):
    A, B = list(map(int,input().split()))
    Num_list = [i for i in range(A,B+1)]

    while True:
        if len(Num_list)==1:
            print(f"#{test_case} {Num_list[0]}")
            break

        start = Num_list[0]
        result = []
        for i in range(1,len(Num_list)):
            result.append(func(start, Num_list[i]))


        else:
            Num_list = result



