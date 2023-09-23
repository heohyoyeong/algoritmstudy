# 어떤 국가에서는 자국 내 방송국에서 스파이가 활동하는 사실을 알아냈다. 스파이는 영상물에 암호 코드를 삽입하여 송출하고 있었다. 스파이의 암호 코드에 다음과 같은 규칙이 있음을 발견했다.
#
# 1. 암호코드는 8개의 숫자로 이루어져 있다.
#
# 2. 올바른 암호코드는 (홀수 자리의 합 x 3) + (짝수 자리의 합)이 10의 배수가 되어야 한다.
#
#     ex) 암호코드가 88012346일 경우,
#     ( ( 8 + 0 + 2 + 4 ) x 3 ) + ( 8 + 1 + 3 + 6) = 60은 10의 배수이므로 올바른 암호코드다.
#
#     ex) 암호코드가 19960409일 경우,
#     ( ( 1 + 9 + 0 + 0 ) x 3 ) + ( 9 + 6 + 4 + 9) = 58은 10의 배수가 아니므로 잘못된 암호코드다.
#
# 이 암호코드들을 빠르고 정확하게 인식할 수 있는 스캐너를 개발하려고 한다.
#
# 스캐너는 암호코드 1개가 포함된 직사각형 배열을 읽는다.
#
# 직사각형 배열은 1, 0으로만 이루어져 있고, 암호코드 이외의 부분은 전부 0으로 주어진다.
#
# 암호코드에서 숫자 하나는 7개의 비트로 암호화되어 주어진다. 따라서 암호코드의 가로 길이는 56이다.
#
# 암호코드의 각 숫자가 암호화되는 규칙은 다음과 같다.
#
# 비정상적인 암호코드(가로 길이가 56이 아닌 경우, 아래 규칙대로 해독할 수 없는 경우)는 주어지지 않는다.

import sys
sys.stdin = open("input.txt", "r")

num_array = ["0001101",
            "0011001",
            "0010011",
            "0111101",
            "0100011",
            "0110001",
            "0101111",
            "0111011",
            "0110111",
            "0001011"]

T = int(input())
for test_case in range(1, T + 1):
    Y, X  = list(map(int,input().split()))
    Matrix = [ input() for z in range(Y)]
    idx = 0
    while True:
        if int(Matrix[idx])!=0:
            break
        else:
            idx +=1
    end = X-Matrix[idx][::-1].find("1")-1
    start = end-7*8+1

    nums = []
    for i in range(8):
        data = Matrix[idx][start:start+7]
        for j in range(10):
            if data==num_array[j]:
                nums.append(j)
        start += 7
    sum_data = 0
    for i in range(len(nums)):
        if i%2 ==0:
            sum_data += nums[i]*3
        else:
            sum_data += nums[i]
    if sum_data%10 ==0:
        print(f"#{test_case} {sum(nums)}")
    else:
        print(f"#{test_case} {0}")
