
def climbingstairs(n):

    # 时间复杂度太高
    # if n == 1:
    #     return 1
    # elif n == 2:
    #     return 2
    # else:
    #     return climbingstairs(n-1) + climbingstairs(n-2)

    # 用斐波那契数列形式
    # a = 0
    # b = 1
    # while n:
    #     a,b = b ,a +b
    #     n -= 1
    # return b

    # 动态规划方式
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

s=climbingstairs(3)
print(s)