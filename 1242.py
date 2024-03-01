import sys

sys.stdin = open("1242.txt", "r")
T = int(input())
code_table = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9,
}


def find_back(start):
    for back_idx in range(start, 53, -1):
        if bin_code[back_idx] == "1":
            return back_idx
    else:
        return -1


for t_c in range(1, T + 1):
    N, M = map(int, input().split())
    enc_set = set([input().strip() for _ in range(N)])
    enc_set.remove("0" * M)
    res_set = set()
    not_found = False
    for item in enc_set:
        mul = 1
        bin_code = bin(int(item, 16)).rstrip()
        back = find_back(len(bin_code) - 1)
        while back >= 54:
            dec_l = []
            j = back
            for k in range(8):
                w2 = w3 = w4 = 0
                while bin_code[j] == "1":
                    w4 += 1
                    j -= 1
                while bin_code[j] == "0":
                    w3 += 1
                    j -= 1
                while bin_code[j] == "1":
                    w2 += 1
                    j -= 1
                w1 = 7 * mul - (w2 + w3 + w4)
                dec_t = (w1 // mul, w2 // mul, w3 // mul, w4 // mul)
                if k == 0 and code_table.get(dec_t, -1) == -1:
                    not_found = True
                    break
                dec_l.append(code_table[dec_t])
                j -= w1
            if not_found:
                mul += 1
                not_found = False
                continue
            odd = dec_l[1] + dec_l[3] + dec_l[5] + dec_l[7]
            even = dec_l[2] + dec_l[4] + dec_l[6]
            if not (odd * 3 + even + dec_l[0]) % 10:
                res_set.add(tuple(dec_l))
            back -= 56 * mul - 1
            mul = 1
            back = find_back(back)
    print(f"#{t_c} {sum(map(lambda x: sum(x), res_set))}")
