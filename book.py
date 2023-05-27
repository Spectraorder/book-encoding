import decimal
import math


def read_txt(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        output_ref = {}
        for line in infile:
            data_line = line.strip("\n")
            output_ref.update({data_line[:1]: data_line[2:]})
        return output_ref


def encode_book_str(str, en_ref):
    out_str = ""
    for cur in str:
        if cur not in en_ref.keys():
            raise SyntaxError("Not correctly syntax")
        out_str += en_ref.get(cur)
    if out_str.isdecimal():
        return decimal.Decimal("0." + out_str)
    raise SyntaxError("Encode unavailable")


def encode_book_dec(dec):
    # direct way: time consumption problem
    # a = decimal.Decimal(1.0)
    # b = decimal.Decimal(1.0)
    # while a / b != dec:
    #     if a / b < dec:
    #         a += 1
    #     elif a / b > dec:
    #         b += 1
    #     print(str(a)+", "+str(b)+" : "+str(a/b))
    key = str(dec).split(".")[1]
    a = decimal.Decimal(key)
    # b = decimal.Decimal(math.pow(10, len(key)))
    b = decimal.Decimal("1" + "0" * len(key))
    print('{0:f}'.format(b))
    ded = gcd(a, b)
    a = a / ded
    b = b / ded
    result = decimal.Decimal(a / b)
    print(str(a) + ", " + str(b) + " : " + str(result))
    return a, b


def gcd(m, n):
    m = abs(m)
    n = abs(n)
    while m % n != 0:
        r = m % n
        m = n
        n = r
    return n


# a = input().split()
# x = min(eval(a[0]), eval(a[1]))
# y = max(eval(a[0]), eval(a[1]))
# k = 1
# result = []
# while (k / int(a[2]) < y):
#     if k / int(a[2]) > x and gcd(k, int(a[2])) == 1:
#         result.append(str(k) + '/' + str(int(a[2])))
#     k += 1
# print(" ".join(result))

if __name__ == "__main__":
    input_path = 'corpus/ref.txt'
    phrase = "i hiniaskdjfhlaskdh"
    en_ref = read_txt(input_path)
    dec = encode_book_str(phrase, en_ref)
    print(dec)
    encode_book_dec(dec)
