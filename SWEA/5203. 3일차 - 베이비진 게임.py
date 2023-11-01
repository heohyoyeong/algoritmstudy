import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    Array = list(map(int,input().split()))
    result = []
    A = []
    B = []
    for j in range(len(Array)):
        cut = j%2
        if cut ==0:
            A.append(Array[j])
            A.sort()
            if len(A)>=3:
                for i in range(len(A)-2):
                    if (A[i] == A[i + 1] and A[i] == A[i + 2]) or (A[i] + 1 == A[i + 1] and A[i] + 2 == A[i + 2]) or (A[i] - 1 == A[i + 1] and A[i] - 2 == A[i + 2]):
                        result.append(1)
                        break
        else:
            B.append(Array[j])
            B.sort()
            if len(B) >= 3:
                for i in range(len(B) - 2):
                    if (B[i]==B[i+1] and B[i]==B[i+2]) or (B[i]+1 == B[i+1] and B[i]+2 == B[i+2]) or (B[i]-1 == B[i+1] and B[i]-2 == B[i+2]):
                        result.append(2)
                        break

    if len(result)==0:
        print(f"#{test_case} 0")
    else:
        print(f"#{test_case} {result[0]}")

