import sys

sys.stdin = open('1223.txt', 'r')

for test_case in range(1, 11):
    N = int(input())
    formula = input()
    opr_dict = {'(': 3, '+': 2, '-': 2, '*': 1, '/': 1}
    opr, opd, result = [], [], []
    for elem in formula:
        if elem in opr_dict.keys():  # 연산자인 경우
            if opr:
                tmp = opr.pop()
                if opr_dict[tmp] < opr_dict[elem]:  # top 보다 우선순위가 더 높은 경우
                    opr.append(elem)
                else:
                    for item in opr:
                        if opr_dict[item] < opr_dict[elem]:
                            result.append(opr.pop())
                            break
            else:
                opr.append(elem)
        else:  # 피연산자인 경우
            result.append(elem)
    print(''.join(result))
    print(opr)
