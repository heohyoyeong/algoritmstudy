import sys
sys.stdin = open("input.txt", "r")

def function(N):
    if N%10==0:
        if N==10: #N=10일때 1반환
            return 1
        elif N==20: #20x20은 3반환
            return 3
        else:
            return function(N-10)+(2*function(N-20))
    else:
        print("10의 배수만 입력하세요")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    count=function(N)
    print(f"#{test_case} {count}")
