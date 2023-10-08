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
    N, M = list(map(int,input().split()))
    array = [list(map(int,input().split())) for _ in range(M)]

    head = ListNode(array[0][0])

    curr_node = head
    for i in range(1,N):
        curr_node.next = ListNode(array[0][i])
        alpha = curr_node
        curr_node = curr_node.next
        curr_node.prev = alpha


    for i in range(1,M):
        curr_node = head
        data = array[i][0]


        plus_Node = ListNode(data)

        new_curr_Node = plus_Node
        for j in range(1, N):
            new_curr_Node.next = ListNode(array[i][j])
            alpha = new_curr_Node
            new_curr_Node = new_curr_Node.next
            new_curr_Node.prev = alpha
            if j==N-1:
                final_node = new_curr_Node

        while curr_node:
            if curr_node.val>data:
                last_node = curr_node.prev
                if last_node != None:
                    last_node.next = plus_Node
                plus_Node.prev = last_node
                final_node.next = curr_node
                curr_node.prev = final_node
                if last_node == None:
                    head = plus_Node
                break
            elif curr_node.next == None:
                curr_node.next = plus_Node
                plus_Node.prev = curr_node
                break
            curr_node = curr_node.next
    result = []
    while head:
        result.append(head.val)
        head = head.next
    result.reverse()

    str = f"#{test_case}"
    for i in range(10):
        str = str + f" {result[i]}"

    print(str)