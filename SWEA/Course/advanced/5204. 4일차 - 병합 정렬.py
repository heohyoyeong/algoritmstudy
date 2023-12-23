import sys
sys.stdin = open("../../input.txt", "r")


def merge_sort(m):
    if len(m)<=1:
        return m

    mid = len(m)//2
    left = merge_sort(m[:mid])
    right = merge_sort(m[mid:])

    return merge(left, right)



def merge(left, right):
    global total

    size_left = len(left)
    size_right = len(right)
    total_size = size_left +size_right
    result = [0]*(total_size)
    idx = 0
    right_idx = 0
    left_idx = 0

    if left[-1]>right[-1]:
        total+=1

    while left_idx < size_left or right_idx < size_right:
        if left_idx < size_left and right_idx < size_right:
            if left[left_idx] <= right[right_idx]:
                result[idx] = left[left_idx]
                idx += 1
                left_idx += 1
            else:
                result[idx] = right[right_idx]
                idx += 1
                right_idx += 1

        elif left_idx < size_left:
            result[idx] = left[left_idx]
            idx += 1
            left_idx += 1
        elif right_idx < size_right:
            result[idx] = right[right_idx]
            idx += 1
            right_idx += 1

    return result


T = int(input())


for test_case in range(1, T+1):
    total = 0
    N = int(input())

    arrays = list(map(int,input().split(" ")))

    arrays = merge_sort(arrays)

    print(f"#{test_case} {arrays[N//2]} {total}")
