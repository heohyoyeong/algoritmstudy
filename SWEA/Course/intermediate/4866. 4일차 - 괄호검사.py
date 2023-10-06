import sys
sys.stdin = open("input.txt", "r")

case = ["{","(","}",")"]

T = int(input())

for test_case in range(1, T + 1):
    data_list = list(input())

    result = []

    for i in range(len(data_list)):
        if data_list[i] == "{" or data_list[i] == "(":
            result.append(data_list[i])
        elif data_list[i] == "}" or data_list[i] == ")":
            if len(result)==0:
                result.append(1)
                break
            if result[-1] == "{" and data_list[i] == "}":
                result.pop()
            elif result[-1] == "(" and data_list[i] == ")":
                result.pop()
            else:
                break
    if len(result)==0:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")