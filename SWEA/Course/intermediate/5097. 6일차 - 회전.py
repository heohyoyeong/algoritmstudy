import sys
sys.stdin = open("input.txt", "r")
class Queue(object):

    def __init__(self):
        self.queue = []

    def dequeue(self,n):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)

    def enqueue(self,n):
        self.queue.append(n)
        pass

    def printqueue(self):
        print(self.queue)



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = list(map(int,input().split()))
    Datas = list(map(int, input().split()))
    Case = M%N

    print(f"#{test_case} {Datas[Case]}")


