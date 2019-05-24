
def divide(dividend, divisor):
    # 已经说明除数不为0
    # ******利用位运算代替除法

    negative = (dividend ^ divisor) < 0
    MaxValue = (1 << 31) - 1
    if divisor == -1 and abs(dividend) > MaxValue:
        return -MaxValue if negative else MaxValue

    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    for i in range(31,-1,-1):
        if dividend >> i >= divisor:
            res += 1 << i
            print(res)
            dividend -= divisor << i
    return -res if negative else res

dd = -2147483648
ds = 1
print(divide(dd,ds))