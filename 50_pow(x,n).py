
def mypow1(x,n):
    # 快速幂（倍降指数） 迭代的方式
    res, i = 1, abs(n)
    while i:
        if i % 2 == 0:
            x *= x
            i //= 2
        else:
            res *= x
            i -= 1
    return res if n > 0 else 1 / res

def mypow2(x,n):
    # 快速幂（倍降指数） 递归方式
    if n < 0:
        return mypow2(1/x, -n)
    if n == 0:
        return 1
    if n %2 == 0:
        return mypow2(x*x, n//2)
    else:
        return x * mypow2(x*x, n//2)

def mypow3(x,n):
    # 库函数（传统方式） 迭代方式
    if n < 0:
        x = 1/x
        n = -n
    if n == 0:
        return 1
    res = 1
    for _ in range(n):
        res *= x
    return res

def mypow4(x,n):
    # 库函数（传统方式） 递归方式
    if n < 0:
        return mypow4(1/x, -n)
    if n == 0:
        return 1
    if n == 1:
        return x
    return x * mypow4(x,n-1)

x, n = 3, 5
# x, n = 2,-2
print(mypow1(x,n))
print(mypow2(x,n))
