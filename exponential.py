# Exponential
expo = 2 ** 3


def expo(base_num, raise_num):
    result = 1
    for index in range(raise_num):
        result *= base_num
    return result


print(expo(2, 3))
