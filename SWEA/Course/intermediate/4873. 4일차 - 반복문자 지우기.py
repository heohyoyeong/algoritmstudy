import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str_list = list(input())
    start = 1

    while True:
        if start > len(str_list)-1 or len(str_list)<=1:
            break
        if str_list[start] == str_list[start-1]:
            str_list.pop(start-1)
            str_list.pop(start-1)
            start -= 1
            if start<1:
                start +=1

        else:
            start +=1

    print(f"#{test_case} {len(str_list)}")


