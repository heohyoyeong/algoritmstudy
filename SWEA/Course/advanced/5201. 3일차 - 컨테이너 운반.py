from collections import deque
T = int(input())

for test_case in range(1, T + 1):
    first = list(map(int,input().split()))
    N, M = first[0], first[1]
    container = list(map(int, input().split()))
    container.sort(reverse=True)
    container = deque(container)
    truck = list(map(int, input().split()))
    truck.sort(reverse=True)
    truck = deque(truck)
    a=0
    for i in range(M):

        if len(container)==0:
            break
        else:
            find_container = True
            new_truck = truck.popleft()
            while find_container:
                new_container = container.popleft()
                if new_truck>=new_container:
                    a+=new_container
                    find_container = False

                if len(container)==0:
                    break


    print(f"#{test_case} {a}")