import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def func(num1,num2,data):
    if data == "+":
        return num1 + num2
    elif data == "*":
        return num1 * num2
    elif data == "-":
        return num1 - num2
    elif data == "/":
        return num1 / num2


for test_case in range(1, T + 1):
    N = list(input().split())
    N.pop()
    stack = []
    start = 0
    while True:
        if start>len(N)-1:
            if len(stack)==1:
                print(f"#{test_case} {int(stack.pop())}")
            else:
                print(f"#{test_case} error")
            break

        if N[start].isnumeric() == True:
            stack.append(int(N[start]))
        else:
            if len(stack)>=2:
                num2 = stack.pop()
                num1 = stack.pop()
                result = func(num1, num2, N[start])
                stack.append(result)
            else:
                print(f"#{test_case} error")
                break
        start+=1



