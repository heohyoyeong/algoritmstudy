import sys

sys.stdin = open("input.txt", "r")


class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, L = list(map(int,input().split()))
    array = list(map(int,input().split()))


    head = ListNode(array[0])
    curr_node = head

    for i in range(1,N):
        curr_node.next = ListNode(array[i])
        curr_node.prev = curr_node
        curr_node = curr_node.next

    for i in range(M):
        index, value = list(map(int, input().split()))
        node = head
        for j in range(index-1):
            node = node.next
        nexter = node.next
        node.next = ListNode(value)
        node.next.next = nexter
        nexter.prev = node

    for i in range(L):
        head = head.next
    print(f"#{test_case} {head.val}")