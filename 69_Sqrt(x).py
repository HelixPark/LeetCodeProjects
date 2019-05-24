

def sqrt_x(x):
    if x <= 1:
        return x
    r = x
    # 首先随便猜一个近似值r，然后不断令r等于r和x / r的平均数，迭代个六七次后r的值就已经相当精确了
    while r > x / r:
        r = (r + x / r) // 2
    return int(r)

a=sqrt_x(8)
print(a)