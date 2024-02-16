import sys

sys.stdin = open('1223.txt', 'r')

for test_case in range(1, 11):
    N = int(input())
    formula = input()
    opr_dict = {'(': 3, '+': 2, '-': 2, '*': 1, '/': 1}
    opr, opd, result = [], [], []
    # convert formula to RPN
    for elem in formula:
        if elem in opr_dict.keys():
            if opr and opr_dict[opr[-1]] > opr_dict[elem]:
                opr.append(elem)
            elif opr and opr_dict[opr[-1]] <= opr_dict[elem]:
                    for i in range(len(opr)):
                        if opr_dict[elem] < opr_dict[opr[-1]]:
                            break
                        result.append(opr.pop())
                    opr.append(elem)
            elif not opr:
                opr.append(elem)
        else:
            result.append(elem)
    else:
        if opr:
            for elem in range(len(opr)):
                result.append(opr.pop())
    # evaluate RPN formula
    for elem in result:
        eval_v = 0
        if elem in opr_dict.keys():
            if len(opd) > 1:
                n1, n2 = opd.pop(), opd.pop()
                if elem == '+':
                    eval_v += int(n1) + int(n2)
                    opd.append(eval_v)
                elif elem == '*':
                    eval_v += int(n1) * int(n2)
                    opd.append(eval_v)
        else:
            opd.append(elem)
    else:
       result = opd.pop()
    print(f'#{test_case} {result}')
